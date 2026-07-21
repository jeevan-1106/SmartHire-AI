import os
import tempfile
import streamlit as st
import pandas as pd
import plotly.express as px

from src.services.analyzer import SmartHireAnalyzer
from src.utils.report_generator import ReportGenerator

st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 SmartHire AI Pro")
st.caption("AI Resume Analyzer | ATS Score | Career Recommendation")

st.markdown("---")

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    with st.spinner("Analyzing Resume..."):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(uploaded_file.name)[1]
        ) as temp:

            temp.write(uploaded_file.read())
            resume_path = temp.name

        analyzer = SmartHireAnalyzer()

        result = analyzer.analyze_resume(
            resume_path,
            "data/raw/jobs.csv"
        )

        os.remove(resume_path)

    score = result["resume_score"]
    stats = result["skill_statistics"]

    c1, c2, c3 = st.columns(3)

    c1.metric("🎯 ATS Score", f"{score:.2f}%")
    c2.metric("🏆 Best Match", result["best_job"])
    c3.metric("📊 Skill Match", f"{stats['match_percent']}%")

    st.progress(min(score / 100, 1.0))

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Skills Found")

        for skill in result["matched_skills"]:
            st.success(skill)

    with right:

        st.subheader("❌ Skills Missing")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.error(skill)
        else:
            st.success("Excellent!")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💡 Why this Job?")

        for reason in result["explanation"]["reasons"]:
            st.write(reason)

    with col2:

        st.subheader("🚀 Improve by Learning")

        for skill in result["explanation"]["improvements"]:
            st.write(skill)

    st.divider()

    st.subheader("📊 Top Job Recommendations")

    recommendations = result["recommendations"].head(5)

    st.dataframe(
        recommendations[
            [
                "Job Title",
                "Category",
                "Score"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        recommendations,
        x="Score",
        y="Job Title",
        orientation="h",
        color="Score",
        text="Score"
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    pie = pd.DataFrame({

        "Category": [
            "Matched",
            "Missing"
        ],

        "Count": [
            stats["matched_count"],
            stats["missing_count"]
        ]

    })

    fig2 = px.pie(
        pie,
        names="Category",
        values="Count",
        hole=0.5
    )

    st.subheader("🥧 Skill Coverage")

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    st.subheader("📝 Resume Suggestions")

    for tip in result["suggestions"]:
        st.info(tip)

    st.divider()

    if st.button("📄 Generate PDF Report"):

        report = ReportGenerator()

        filename = report.generate(result)

        st.success(f"Report generated successfully: {filename}")

else:

    st.info("⬆ Upload your resume to begin analysis.")