import streamlit as st
from google import genai
import os
import json


client = genai.Client(api_key="API KEY")

#input = input("What book would you like summarized")
user_input = st.text_area("📘 Enter your text, note, or highlight:")

if st.button("🔍 Analyze"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[F"Match the following text to a known mental model {user_input}"]
            )
            st.subheader("Here is the response")
            st.title(response.text)
