import PyPDF2

def extract_text(uploaded_file):
    text = ""

    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    else:
        text = uploaded_file.read().decode("utf-8")

    return text
