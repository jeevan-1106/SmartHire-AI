import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from src.features.tfidf_vectorizer import TFIDFVectorizer
from src.data.preprocess import clean_text


class RecommendationEngine:

    def __init__(self):
        self.vectorizer = TFIDFVectorizer()

    def recommend_jobs(self, resume_text, jobs_path):

        jobs = pd.read_csv(jobs_path)

        # Clean resume
        resume_clean = clean_text(resume_text)

        # Clean job skills
        jobs["Clean Skills"] = jobs["Skills"].apply(clean_text)

        # TF-IDF
        job_vectors = self.vectorizer.fit_transform(
            jobs["Clean Skills"].tolist()
        )

        resume_vector = self.vectorizer.transform(
            [resume_clean]
        )

        tfidf_scores = cosine_similarity(
            resume_vector,
            job_vectors
        )[0]

        # Skill Matching
        resume_words = set(resume_clean.split())

        skill_scores = []

        for skills in jobs["Clean Skills"]:

            job_words = set(skills.split())

            if len(job_words) == 0:
                skill_scores.append(0)
                continue

            matched = len(
                resume_words.intersection(job_words)
            )

            score = matched / len(job_words)

            skill_scores.append(score)

        # Final Score
        final_scores = []

        for tfidf, skill in zip(tfidf_scores, skill_scores):

            score = (0.30 * tfidf) + (0.70 * skill)

            final_scores.append(score)

        jobs["Score"] = final_scores

        # Convert to %
        jobs["Score"] = (
            jobs["Score"] * 100
        ).round(2)

        jobs = jobs.sort_values(
            by="Score",
            ascending=False
        ).reset_index(drop=True)

        return jobs