import streamlit as st  # Import Streamlit for web-based UI
from transformers import pipeline  # Import pipeline for NLP
import nltk  # Import Natural Language Toolkit
from nltk.corpus import stopwords  # Import stopwords from NLTK

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")

# Define healthcare-specific response logic (or use a model to generate responses)
def healthcare_chatbot(user_input):
    # Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        # Use AI model to generate a response
        response = chatbot(user_input, max_length=100, do_sample=True)
        return response[0]['generated_text']

# Streamlit UI
st.title("AI Healthcare Assistant")
user_input = st.text_input("Ask me anything about healthcare")

if user_input:
    response = healthcare_chatbot(user_input)
    st.write(response)
