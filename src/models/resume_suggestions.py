class ResumeSuggestions:

    def generate(self, score, missing_skills):

        suggestions = []

        if score < 50:
            suggestions.append(
                "Your resume matches only a small portion of the required skills. Consider adding more technical projects."
            )

        elif score < 75:
            suggestions.append(
                "Your resume is good, but adding more relevant skills and certifications can improve your chances."
            )

        else:
            suggestions.append(
                "Excellent resume! Focus on advanced skills and real-world projects to stand out."
            )

        if len(missing_skills) > 0:

            suggestions.append(
                f"Learn these important skills: {', '.join(missing_skills[:5])}"
            )

        suggestions.append(
            "Add measurable achievements (e.g., 'Improved accuracy by 20%')."
        )

        suggestions.append(
            "Keep your resume limited to one page."
        )

        suggestions.append(
            "Include GitHub and LinkedIn profile links."
        )

        return suggestions