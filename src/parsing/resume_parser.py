"""
Resume Parser
-------------
Extracts text from PDF, DOCX, and TXT resumes.
"""

from pathlib import Path
import pdfplumber
from docx import Document


class ResumeParser:

    def extract_text(self, file_path):

        file_path = Path(file_path)

        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            return self._read_pdf(file_path)

        elif suffix == ".docx":
            return self._read_docx(file_path)

        elif suffix == ".txt":
            return self._read_txt(file_path)

        else:
            raise ValueError(f"Unsupported file type: {suffix}")

    def _read_pdf(self, file_path):

        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    def _read_docx(self, file_path):

        doc = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    def _read_txt(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()