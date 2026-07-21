from src.parsing.resume_parser import ResumeParser
from src.models.recommendation_engine import RecommendationEngine
from src.models.resume_scorer import ResumeScorer
from src.models.skill_gap import SkillGapAnalyzer
from src.models.resume_suggestions import ResumeSuggestions
from src.models.skill_statistics import SkillStatistics
from src.models.recommendation_explainer import RecommendationExplainer


class SmartHireAnalyzer:

    def __init__(self):

        self.parser = ResumeParser()

        self.recommender = RecommendationEngine()

        self.scorer = ResumeScorer()

        self.skill_gap = SkillGapAnalyzer()

        self.suggestions = ResumeSuggestions()

        self.statistics = SkillStatistics()

        self.explainer = RecommendationExplainer()

    def analyze_resume(self, resume_path, jobs_path):

        resume_text = self.parser.extract_text(
            resume_path
        )

        recommendations = self.recommender.recommend_jobs(
            resume_text,
            jobs_path
        )

        score = self.scorer.calculate_score(
            recommendations
        )

        gap = self.skill_gap.analyze(
            resume_text,
            recommendations
        )

        stats = self.statistics.calculate(
            gap["matched"],
            gap["missing"]
        )

        tips = self.suggestions.generate(
            score,
            gap["missing"]
        )

        explanation = self.explainer.explain(
            gap["matched"],
            gap["missing"]
        )

        return {

            "resume_score": score,

            "best_job": gap["best_job"],

            "matched_skills": gap["matched"],

            "missing_skills": gap["missing"],

            "recommendations": recommendations,

            "suggestions": tips,

            "skill_statistics": stats,

            "explanation": explanation

        }