# AI Resume Analyzer (Offline NLP Project)

An AI-based Resume Analyzer built using Natural Language Processing (NLP) techniques. This project analyzes resume text, extracts important keywords, detects skills, scores the resume, and provides improvement suggestions—all **without using any paid APIs or billing**.

---

## 📌 Features
* **Resume Text Analysis:** Parses and processes raw text from resumes.
* **Skill Extraction:** Automatically identifies technical and soft skills.
* **Keyword Extraction:** Uses TF-IDF (Term Frequency-Inverse Document Frequency) to find key terms.
* **Resume Scoring:** Generates a score based on content density and keyword relevance.
* **Improvement Suggestions:** Provides actionable feedback for the user.
* **Fully Offline:** No OpenAI or external API keys required.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** Streamlit (for the UI)
* **NLP Libraries:** NLTK, Scikit-learn
* **Data Handling:** Pandas, NumPy

---

## 📂 Project Structure
```text
ai-resume-analyzer/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation

```

🚀 How to Run the Project
1️⃣ Clone the Repository
Bash
git clone [https://github.com/your-username/ai-resume-analyzer.git](https://github.com/your-username/ai-resume-analyzer.git)
cd ai-resume-analyzer
2️⃣ Create Virtual Environment
Bash
python -m venv venv
3️⃣ Activate Virtual Environment
Windows:

Bash
venv\Scripts\activate
Mac/Linux:

Bash
source venv/bin/activate
4️⃣ Install Dependencies
Bash
pip install -r requirements.txt
5️⃣ Run the Application
Bash
streamlit run app.py
The app will open automatically in your browser at http://localhost:8501.

🧠 Project Description (For Academic Submission)
This project demonstrates the application of Artificial Intelligence and Natural Language Processing concepts for resume analysis. It processes raw resume text, applies TF-IDF vectorization to extract important keywords, identifies relevant skills, and provides a resume score along with improvement suggestions. The system works completely offline and does not depend on any third-party AI APIs, making it a privacy-focused and cost-effective solution.

🎯 Objectives
Understand NLP preprocessing techniques (Tokenization, Stop-word removal).

Apply machine learning-based text vectorization.

Build a functional AI-based scoring system.

Develop an end-to-end Python project with a web-based UI.

🔮 Future Enhancements
Job Matching: Compare resumes against specific Job Descriptions (JD).

Classification: Categorize resumes into domains (e.g., Data Science, Web Dev).

PDF Parsing: Enhanced support for complex PDF layouts.

LLM Integration: Adding local Llama or Mistral models for deeper insights.

👩‍💻 Author
Komal Nile

📄 License
This project is created for educational purposes.
