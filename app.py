import streamlit as st
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
from nltk.corpus import stopwords

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer (Offline NLP)")
st.write("Analyze resumes using AI techniques without any API or billing.")

resume_text = st.text_area("Paste your resume here", height=300)

skills_db = [
    "python", "java", "c++", "react", "node", "sql", "mongodb",
    "machine learning", "data analysis", "html", "css", "javascript"
]

def analyze_resume(text):
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    tfidf = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()

    found_skills = [skill for skill in skills_db if skill in text.lower()]
    score = min(100, len(found_skills) * 8)

    suggestions = []
    if score < 50:
        suggestions.append("Add more relevant technical skills.")
    if "project" not in text.lower():
        suggestions.append("Include a projects section.")
    if "internship" not in text.lower():
        suggestions.append("Mention internships or hands-on experience.")

    return score, found_skills, keywords[:10], suggestions

if st.button("Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please paste your resume.")
    else:
        score, skills, keywords, suggestions = analyze_resume(resume_text)

        st.success("Analysis Complete!")

        st.subheader("📊 Resume Score")
        st.write(f"{score}/100")

        st.subheader("🧠 Detected Skills")
        st.write(", ".join(skills) if skills else "No common skills detected")

        st.subheader("🔑 Important Keywords")
        st.write(", ".join(keywords))

        st.subheader("🛠 Suggestions")
        for s in suggestions:
            st.write("- " + s)