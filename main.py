import os
import streamlit as st
from ai71 import AI71
import firebase_admin
from firebase_admin import credentials, firestore
from google.oauth2 import service_account
from prompts import *
import json

TITLE = "WaitLessCare"
MODEL_NAME = "tiiuae/falcon-11b"

st.set_page_config(page_title=TITLE, page_icon="🤖", layout="wide")
st.title("🤖 " + TITLE)

# Firebase setup
try:
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="waitlesscare")
except Exception as e:
    st.error(f"Firebase setup error: {e}")

# API key setup
try:
    os.environ["AI71_API_KEY"] = st.secrets["AI71_API_KEY"]
except KeyError:
    st.error("Secrets not found")

# Initialize AI71 client
try:
    client = AI71(os.environ["AI71_API_KEY"])
except Exception as e:
    st.error(f"Client error: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_INITIAL_PROMPT},
        {"role": "assistant", "content": "Hello, I am WaitLessCare, a virtual assistant that will help and guide you in your care at this hospital. What are your current symptoms?"},
    ]

if "patient_data" not in st.session_state:
    st.session_state.patient_data = {
        "symptoms": "",
        "medical_history": "",
        "allergies": "",
        "family_history": ""
    }

if "current_question" not in st.session_state:
    st.session_state.current_question = "symptoms"

if "summary" not in st.session_state:
    st.session_state.summary = "The summary is not done yet"


def validate_response(question, answer):
    prompt = VALID_RESPONSE_PROMPT.format(question=question, answer=answer)
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    # print(prompt)
    return response.choices[0].message.content


def get_summary(patient_data):
    prompt = SYSTEM_SUMMARY_PROMPT.format(patient=str(patient_data))
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


st.sidebar.title('About')
st.sidebar.info("""### Disclaimer:
The implementation of WaitLessCare is designed to complement, not replace, professional medical care. While the system can collect and store information securely and efficiently, there is always a risk of errors or inaccuracies in the data provided by patients. It is essential that patients and medical staff use this tool as an additional aid and not as an exclusive source for diagnosis and treatment. Using WaitLessCare implies acceptance of these terms and an understanding of its limitations.""")

tab_chat, tab_reco, tab_about = st.tabs(["Chat (for patients)", "Recommendations (for Doctors)", "About"])

with tab_chat:
    chat_tab_container = st.container()

    with chat_tab_container:
        chat_container = st.container(height=400)

        # Mostrar mensajes previos
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == 'system':
                    continue
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        
        # if prompt := st.chat_input(questions[st.session_state.current_question]):
        if prompt := st.chat_input("Say something..."):
            with chat_container.chat_message('user'):
                st.markdown(prompt)

            st.session_state.messages.append({"role": 'user', "content": prompt})

            # Validar la respuesta usando AI71
            validation_result = validate_response(questions[st.session_state.current_question], prompt)
            # print(validation_result)

            try:
                validation_result = float(validation_result)
            except:
                validation_result = 0
            
            if validation_result >= 0.5:
                # Actualizar los datos del paciente si la respuesta es válida
                st.session_state.patient_data[st.session_state.current_question] = prompt

                # Preparar la siguiente pregunta o finalizar
                keys = list(questions.keys())
                current_index = keys.index(st.session_state.current_question)
                if current_index < len(keys) - 1:
                    st.session_state.current_question = keys[current_index + 1]
                    response_content = f"Thanks for providing this information. {questions[st.session_state.current_question]}"
                else:
                    response_content = "Thank you for providing all this information. I will save it so that the medical staff can assist you better. Please wait for your turn 😊."
                    
                    # Guardar en Firebase
                    db.collection("patients").add(st.session_state.patient_data)
                    st.session_state.summary = get_summary(str(st.session_state.patient_data))
                    
                    # Resetear para el próximo paciente
                    st.session_state.patient_data = {key: "" for key in st.session_state.patient_data}
                    st.session_state.current_question = "symptoms"
            else:
                # Si la respuesta no es válida, pedir clarificación
                response_content = f"Sorry, I didn't quite understand your response. Could you please answer the question again: {questions[st.session_state.current_question]}"

            with chat_container.chat_message('assistant'):
                st.markdown(response_content)

            st.session_state.messages.append({"role": 'assistant', "content": response_content})

        # Desplazamiento automático al final del chat
        st.markdown(
            """
            <script>
            const chatContainer = parent.document.querySelector('.element-container');
            chatContainer.scrollTop = chatContainer.scrollHeight;
            </script>
            """,
            unsafe_allow_html=True,
        )

with tab_reco:
    with st.expander("Explanation",expanded=True):
        st.markdown("This is a view that the doctor could see when treating the person.")
    with st.expander("Summary",expanded=True):
        st.markdown(st.session_state.summary)
    

with tab_about:
    st.markdown(ABOUT)