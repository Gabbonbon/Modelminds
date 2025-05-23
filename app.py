import streamlit as st
import google.generativeai as genai

# Load the Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Set up the Gemini model
model = genai.GenerativeModel("gemini-pro")

st.title("🧠 ModelMind")
st.write("Find mental models based on book notes, summaries, or highlights.")

# Text input from user
user_input = st.text_area("📘 Enter your text, note, or highlight:")

# Analyze button
if st.button("🔍 Analyze"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(
                    f"Match the following text to a known mental model: {user_input}"
                )
                st.subheader("🔎 Gemini's Response")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
