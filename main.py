from src.parsing.resume_parser import ResumeParser
from src.models.recommendation_engine import RecommendationEngine
from src.models.resume_scorer import ResumeScorer
from src.utils.logger import logger


def main():

    try:

        logger.info("Starting SmartHire AI...")

        resume_path = "data/raw/sample_resume.txt"
        jobs_path = "data/raw/jobs.csv"

        # Parse Resume
        parser = ResumeParser()
        resume_text = parser.extract_text(resume_path)

        logger.info("Resume Loaded Successfully.")

        # Recommend Jobs
        recommender = RecommendationEngine()
        recommendations = recommender.recommend_jobs(
            resume_text,
            jobs_path
        )

        # Resume Score
        scorer = ResumeScorer()
        score = scorer.calculate_score(recommendations)

        print("\n" + "=" * 70)
        print("                     🤖 SMART HIRE AI")
        print("=" * 70)

        print(f"\n🎯 Resume Score : {score:.2f}%")

        print("\n🏆 Best Matching Job")
        print("-" * 70)

        best_job = recommendations.iloc[0]

        print(f"💼 Job Title : {best_job['Job Title']}")
        print(f"📂 Category  : {best_job['Category']}")
        print(f"📊 Match     : {best_job['Score']:.2f}%")

        print("\n" + "=" * 70)
        print("🏆 TOP 5 JOB RECOMMENDATIONS")
        print("=" * 70)

        for i, (_, row) in enumerate(recommendations.head(5).iterrows(), start=1):

            print(f"\n{i}. {row['Job Title']}")
            print(f"   📂 Category : {row['Category']}")
            print(f"   📊 Match    : {row['Score']:.2f}%")

        print("\n" + "=" * 70)
        print("✅ Analysis Completed Successfully")
        print("=" * 70)

    except FileNotFoundError:
        print("\n❌ Resume file or Jobs file not found.")

    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()