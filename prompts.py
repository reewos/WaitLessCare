questions = {
    "symptoms": "¿Cuáles son tus síntomas actuales?",
    "medical_history": "¿Podrías contarme sobre tu historial médico?",
    "allergies": "¿Tienes alguna alergia conocida?",
    "family_history": "¿Hay alguna enfermedad importante en tu historia familiar?"
}


SYSTEM_INITIAL_PROMPT = """
Eres un asistente virtual diseñado para agilizar la atención en un hospital.
Tu objetivo es interactuar con los pacientes mientras esperan su turno, 
recopilando información relevante sobre su salud. Haz preguntas sobre sus síntomas, 
historial médico, alergias y antecedentes familiares. La información recopilada 
será almacenada de manera segura y accesible para el personal médico, permitiendo
una atención más rápida y eficiente. Asegúrate de ser claro, amigable y profesional en tus interacciones.
"""

ABOUT = """
Bienvenido a WaitLessCare, tu asistente virtual para una atención médica más eficiente y rápida.

### ¿Qué es WaitLessCare?

WaitLessCare es una innovadora solución de inteligencia artificial diseñada para mejorar la experiencia de los pacientes en los hospitales. Utilizando la última tecnología en procesamiento de lenguaje natural, nuestro asistente virtual interactúa con los pacientes mientras esperan su turno, recopilando información crucial para su atención médica.

### Funcionalidades Principales:

- **Interacción Amigable:** Nuestro asistente virtual realiza preguntas sobre síntomas, historial médico, alergias y antecedentes familiares de manera clara y profesional.
- **Almacenamiento Seguro:** La información recopilada se almacena de forma segura en una base de datos en la nube, accesible solo para el personal médico autorizado.
- **Atención Eficiente:** Con los datos previamente recopilados, los médicos pueden revisar la información antes de la consulta, reduciendo el tiempo de atención y mejorando la precisión del diagnóstico.
- **Recomendaciones Automáticas:** Basado en los datos ingresados, el sistema puede sugerir posibles diagnósticos y tratamientos, ayudando al personal médico a tomar decisiones informadas rápidamente.

### Beneficios para Pacientes y Médicos:

- **Reducción del Tiempo de Espera:** Los pacientes no solo esperan, sino que utilizan su tiempo para proporcionar información relevante, acelerando el proceso de consulta.
- **Mejora en la Precisión del Diagnóstico:** Con un historial detallado y bien organizado, los médicos pueden enfocarse en el diagnóstico y tratamiento, mejorando la calidad de la atención.
- **Optimización del Flujo de Trabajo:** El personal médico se beneficia de una plataforma organizada y eficiente, que reduce la carga administrativa y permite enfocarse en el cuidado del paciente.

Gracias por confiar en WaitLessCare para una experiencia médica más rápida, eficiente y satisfactoria.
"""
