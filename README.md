# Resume Matching & Screening System 📄🤖

## 📌 Project Overview
The **Resume Matching & Screening System** is a **Flask-based NLP web application** designed to automatically match and rank resumes against a given job description.

The system helps recruiters and placement teams **reduce manual resume screening effort** by using **Natural Language Processing (NLP)** techniques to identify the most relevant resumes based on skills, experience, and keywords.

---

## 🎯 Objectives
- Automate resume shortlisting process
- Rank resumes based on relevance to job description
- Support multiple resume formats (PDF, DOCX, TXT)
- Provide additional insights such as internship intent, certifications, and projects
- Improve accuracy and efficiency in recruitment workflows

---

## 🚀 Key Features
- Upload **multiple resumes at once**
- Supports **PDF, DOCX, and TXT** resume formats
- **TF-IDF vectorization** for text processing
- **Cosine similarity** for resume ranking
- Displays **top matching resumes with scores**
- Detects:
  - Internship intent
  - Certifications
  - Relevant courses
  - Project mentions
  - Experience timelines
- Simple and user-friendly web interface

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **Flask** (Web Framework)

### NLP & ML
- **scikit-learn**
- TF-IDF Vectorizer
- Cosine Similarity

### File Processing
- **PyPDF2** (PDF text extraction)
- **docx2txt** (DOCX text extraction)
- Text file handling

### Frontend
- HTML (Jinja templates)
- Basic form-based UI

---

## ⚙️ How the System Works
1. User enters a **job description**
2. User uploads **multiple resumes**
3. Resume text is extracted based on file type
4. Job description and resumes are converted into **TF-IDF vectors**
5. **Cosine similarity** is calculated between job description and each resume
6. Resumes are ranked based on similarity scores
7. Additional NLP analysis is performed for deeper insights
8. Results are displayed on the web interface

---

## 📐 NLP Techniques Used
- **TF-IDF (Term Frequency–Inverse Document Frequency)**  
  Converts text into numerical vectors based on word importance.

- **Cosine Similarity**  
  Measures how closely a resume matches the job description.

- **Regex-based pattern matching**  
  Detects internship intent, certifications, and experience mentions.

---

## 📊 Output Provided
- Top matching resumes (ranked)
- Similarity score for each resume
- Internship intent detection
- Certification presence
- Course keywords detection
- Project mentions extracted from resumes

---

## 🧠 What I Learned
- Applying NLP techniques to real-world problems
- Resume text extraction from different file formats
- Implementing similarity-based ranking systems
- Using Flask for backend development
- Handling file uploads and processing
- Designing practical ML-driven applications

---

## 🔮 Future Improvements
- Skill-based ranking using Named Entity Recognition (NER)
- Admin dashboard for recruiters
- Resume ranking visualization
- PDF report generation
- Database integration for storing resume data
- Authentication for recruiters and admins

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install flask scikit-learn PyPDF2 docx2txt
python app.py
http://localhost:5000

