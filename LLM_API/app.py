import streamlit as st
from huggingface_hub import login
from nlp.pipeline import run_pipeline
from llm.generator import generate_answer

# Get token from Streamlit Secrets
# HF_TOKEN = st.secrets["HF_TOKEN"]
HF_TOKEN = "wertyuiopasdfghjkzxcvbnm"

# Login to Hugging Face
login(HF_TOKEN)

st.set_page_config(
    page_title="Knowledge Base Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Knowledge Base Chatbot")
st.write("Ask questions based on your training data.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            nlp_result = run_pipeline(prompt)

            answer = generate_answer(
                query=prompt,
                intent=nlp_result["intent"],
                entities=nlp_result["entities"],
                documents=nlp_result["documents"],
                api_token=HF_TOKEN
            )

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )