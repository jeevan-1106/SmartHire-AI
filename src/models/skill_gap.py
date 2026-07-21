import pandas as pd


class SkillGapAnalyzer:

    def analyze(self, resume_text, recommendations):

        # Load master skill list
        skills_db = pd.read_csv("data/raw/skills.csv")

        resume_lower = resume_text.lower()

        found_skills = []

        for skill in skills_db["Skill"]:

            if skill.lower() in resume_lower:
                found_skills.append(skill)

        # Best Matching Job
        best_job = recommendations.iloc[0]

        job_skills = [
            skill.strip()
            for skill in best_job["Skills"].split(",")
        ]

        matched = []

        missing = []

        for skill in job_skills:

            if skill in found_skills:
                matched.append(skill)
            else:
                missing.append(skill)

        return {

            "matched": sorted(matched),

            "missing": sorted(missing),

            "best_job": best_job["Job Title"]

        }