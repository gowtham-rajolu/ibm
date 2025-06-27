import streamlit as st
import fitz  # PyMuPDF
import requests
from chatbot import show_floating_chatbot
st.title("Smart SDLC - Requirement Classifier")
st.write("Upload a requirements PDF file to classify content into SDLC phases.")

# Upload PDF
file = st.file_uploader("Upload Requirements File", type="pdf")

if file is not None:
    st.success("✅ File uploaded successfully!")

    # Read and extract PDF text
    doc = fitz.open(stream=file.read(), filetype="pdf")
    all_text = ""
    for page in doc:
        all_text += page.get_text()
    all_text = ''.join(all_text.split())
    st.subheader("📄 Extracted Requirements Text")
    st.text_area("Raw Text Extracted", all_text, height=200)

    if st.button("🔍 Classify Requirements"):
        with st.spinner("Sending data to backend for classification..."):
            response = requests.post(
                "http://127.0.0.1:8000/reqclass", 
                json={"prompt": all_text}
            )

            if response.status_code == 200:
                data = response.json()
                print(data)
                if data:
                    print(data)
                    st.markdown(data["choices"][0]["message"]["content"])
                else:
                    st.error("❌ Error from backend: " + data.get("error", "Unknown"))
            else:
                st.error("❌ Failed to connect to backend.")
show_floating_chatbot()
