from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    def generate(self, result, output_path="Resume_Report.pdf"):

        doc = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph("<b>SmartHire AI Report</b>", styles["Title"])
        )

        story.append(
            Paragraph(
                f"<b>Resume Score:</b> {result['resume_score']:.2f}%",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Best Matching Job:</b> {result['best_job']}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"])
        )

        for skill in result["matched_skills"]:
            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )

        story.append(
            Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"])
        )

        for skill in result["missing_skills"]:
            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )

        story.append(
            Paragraph("<br/><b>Top Recommendations</b>", styles["Heading2"])
        )

        for _, row in result["recommendations"].head(5).iterrows():

            story.append(

                Paragraph(

                    f"{row['Job Title']} ({row['Score']:.2f}%)",

                    styles["Normal"]

                )

            )

        story.append(
            Paragraph("<br/><b>Suggestions</b>", styles["Heading2"])
        )

        for suggestion in result["suggestions"]:

            story.append(

                Paragraph(

                    f"• {suggestion}",

                    styles["Normal"]

                )

            )

        doc.build(story)

        return output_path