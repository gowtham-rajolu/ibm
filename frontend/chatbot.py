import streamlit as st
import requests

def show_floating_chatbot():
    st.markdown("---")
    with st.expander(" Ask the SDLC chat bot", expanded=False):
        user_prompt = st.text_input("Ask something about SDLC:", key="chat_input_nohistory")

        if st.button("Ask AI", key="submit_chat_nohistory"):
            if not user_prompt.strip():
                st.warning(" Please enter a question.")
            else:
                with st.spinner(" Thinking..."):
                    try:
                        res = requests.post("http://127.0.0.1:8000/chatbot", json={"prompt": user_prompt})
                        if res.status_code == 200:
                            reply = res.json()["choices"][0]["message"]["content"]
                        else:
                            reply = f" Error: {res.status_code}"
                    except:
                        reply = " Could not connect to backend."

                st.subheader(" Bot Response")
                st.markdown(reply)
    st.markdown("---")

