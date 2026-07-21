from src.parsing.resume_parser import ResumeParser
from src.data.preprocess import clean_text

parser = ResumeParser()

# Read resume
text = parser.extract_text("src/data/sample_resume.txt")

print("=" * 50)
print("ORIGINAL TEXT")
print("=" * 50)
print(text)

# Clean text
cleaned = clean_text(text)

print("\n" + "=" * 50)
print("CLEANED TEXT")
print("=" * 50)
print(cleaned)