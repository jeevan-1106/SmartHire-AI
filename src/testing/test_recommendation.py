from src.parsing.resume_parser import ResumeParser
from src.models.recommendation_engine import RecommendationEngine

parser = ResumeParser()
engine = RecommendationEngine()

resume = parser.extract_text("data/raw/sample_resume.txt")

recommendations = engine.recommend_jobs(
    resume,
    "data/raw/jobs.csv"
)

print("\nTOP JOB RECOMMENDATIONS\n")
print(recommendations)
