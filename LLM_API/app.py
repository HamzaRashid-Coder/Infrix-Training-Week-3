

import streamlit as st
import os
from dotenv import load_dotenv
from nlp.pipeline import run_pipeline
from llm.generator import generate_answer


load_dotenv(override=True)
HF_TOKEN = "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"
print("Token loaded:", HF_TOKEN[:10] if HF_TOKEN else "NOT FOUND")
print("Token repr:", repr(HF_TOKEN))
print("Token length:", len(HF_TOKEN) if HF_TOKEN else 0)
print("DEBUG raw bytes:", HF_TOKEN.encode())

print("DEBUG raw bytes:", HF_TOKEN.encode())
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

if not HF_TOKEN:
    st.error("⚠️ HUGGINGFACE_API_TOKEN not set. Add it to your environment or .env file.")
    st.stop()

st.set_page_config(page_title="Knowledge Base Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 AI Knowledge Base Chatbot")
st.write("Ask questions based on your training data.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            nlp_result = run_pipeline(prompt)
            print("APP TOKEN:", repr(HF_TOKEN))
            answer = generate_answer(
                query=prompt,
                intent=nlp_result["intent"],
                entities=nlp_result["entities"],
                documents=nlp_result["documents"],
                api_token=HF_TOKEN
            )
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
