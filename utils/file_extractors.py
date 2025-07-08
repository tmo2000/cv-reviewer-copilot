import PyPDF2

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()


def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8").strip()

def clean_text(text):
    return " ".join(text.split()).strip()