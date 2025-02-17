import streamlit as st
import requests

# Set Backend API URL (Replace with actual VM2 IP)
BACKEND_URL = "http://VM2_IP:8000/generate"

st.title("🤖 Free AI Chatbot")

question = st.text_input("Enter Your Question:")

if st.button("Get Answer") and question:
    with st.spinner("Generating answer..."):
        response = requests.get(BACKEND_URL, params={"question": question})
        if response.status_code == 200:
            st.subheader("Answer:")
            st.write(response.json()["answer"])
        else:
            st.error("Error: Could not fetch response from backend.")