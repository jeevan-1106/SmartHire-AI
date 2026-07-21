class RecommendationExplainer:

    def explain(self, matched_skills, missing_skills):

        reasons = []

        for skill in matched_skills[:5]:
            reasons.append(f"✔ {skill}")

        improvements = []

        for skill in missing_skills[:5]:
            improvements.append(f"✖ {skill}")

        return {

            "reasons": reasons,

            "improvements": improvements

        }