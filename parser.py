import pdfplumber
from docx import Document


def parse_pdf(file_stream):
    text = ""
    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text


def parse_docx(file_stream):
    doc = Document(file_stream)
    return "\n".join([p.text for p in doc.paragraphs])


def parse_txt(file_stream):
    return file_stream.read().decode("utf-8", errors="ignore")


def extract_text(file_stream, filename: str):
    name = filename.lower()
    if name.endswith(".pdf"):
        return parse_pdf(file_stream)
    if name.endswith(".docx"):
        return parse_docx(file_stream)
    if name.endswith(".txt"):
        return parse_txt(file_stream)
    return ""