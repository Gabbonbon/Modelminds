import streamlit as st
import google.generativeai as genai

# Setup API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Create the model (this one works for generate_content)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # or gemini-1.5-pro

# Streamlit UI
st.title("🧠 ModelMind")
st.write("Find mental models based on book notes, summaries, or highlights.")

user_input = st.text_area("📘 Enter your text, note, or highlight:")

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
