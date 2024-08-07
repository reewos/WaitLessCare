questions = {
    # "identity": "What is ID or order code?",
    "symptoms": "What are your current symptoms?",
    "medical_history": "Could you tell me about your medical history?",
    "allergies": "Do you have any known allergies?",
    "family_history": "Is there any significant disease in your family history?"
}

VALID_RESPONSE_PROMPT = """
Question: {question}
User's answer: {answer}

Evaluate the answer's relevance and appropriateness. 
Return a value from 0 to 1:
0: Irrelevant or incoherent
1: Relevant and appropriate, or user indicates they don't know/won't answer
(0-1): Partially relevant/appropriate

Provide only the numerical score.
"""

SYSTEM_SUMMARY_PROMPT = """
Patient Data: {patient}

Make a summary with the following data:
* Symptoms
* Medical history
* Allergies or contraindications
* Family history

In addition, given the above data, make a recommendation of:
* Possible diagnosis
* Possible procedures (medicines and treatments)

Generate in markdown format.
"""

SYSTEM_INITIAL_PROMPT = """
You are a virtual assistant designed to streamline care in a hospital.
Your goal is to interact with patients while they wait their turn,
gathering relevant information about their health. Ask questions about their symptoms,
medical history, allergies, and family history. The information collected
will be stored securely and accessible to medical staff, allowing
faster and more efficient care. Make sure to be clear, friendly, and professional in your interactions.
"""

ABOUT = """
Welcome to WaitLessCare, your virtual assistant for faster and more efficient healthcare.

### What is WaitLessCare?

WaitLessCare is an innovative artificial intelligence solution designed to improve the patient experience in hospitals. Using the latest technology in natural language processing, our virtual assistant interacts with patients while they wait for their turn, collecting crucial information for their healthcare.

### Key Features:

- **Friendly Interaction:** Our virtual assistant asks questions about symptoms, medical history, allergies, and family history in a clear and professional manner.
- **Secure Storage:** The information collected is securely stored in a cloud database, accessible only to authorized medical staff.
- **Efficient Care:** With previously collected data, doctors can review the information before the consultation, reducing care time and improving diagnostic accuracy.
- **Automatic Recommendations:** Based on the data entered, the system can suggest possible diagnoses and treatments, helping medical staff make informed decisions quickly.

### Benefits for Patients and Doctors:

- **Reduced Waiting Time:** Patients don't just wait, they use their time to provide relevant information, speeding up the consultation process.
- **Improved Diagnostic Accuracy:** With a detailed and well-organized history, doctors can focus on diagnosis and treatment, improving the quality of care.
- **Workflow Optimization:** Medical staff benefits from an organized and efficient platform, which reduces administrative burden and allows them to focus on patient care.

Thank you for trusting WaitLessCare for a faster, more efficient and more satisfying medical experience.
"""