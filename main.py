from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

@app.route("/")
def matchresume():
    return render_template('matchresume.html')

@app.route('/matcher', methods=['POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_files = request.files.getlist('resumes')

        resumes = []
        for resume_file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            resumes.append(extract_text(filename))

        if not resumes or not job_description:
            return render_template('matchresume.html', message="Please upload resumes and enter a job description.")

        # Vectorize job description and resumes
        vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
        vectors = vectorizer.toarray()

        # Calculate cosine similarities
        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity([job_vector], resume_vectors)[0]

        # Get top 3 resumes and their similarity scores
        top_indices = similarities.argsort()[-5:][::-1]
        top_resumes = [resume_files[i].filename for i in top_indices]
        similarity_scores = [round(similarities[i], 2) for i in top_indices]
        # Extra NLP Analysis for project goals
        extra_details = []

        keywords_courses = ['python', 'machine learning', 'data science', 'ai', 'deep learning']
        keywords_internship = ['internship', 'open to internship', 'available for internship']
        keywords_certification = ['certification', 'certified', 'course completed', 'badge']
        keywords_dates = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', '2020', '2021', '2022', '2023', '2024']

        import re

        def contains_internship(text):
            patterns = [
                r'\binternship\b',
                r'intern(ed|ship)?\b',
                r'completed (an )?internship\b',
                r'open to internship',
                r'internship at',
                r'internship in'
            ]
            for pattern in patterns:
                if re.search(pattern, text.lower()):
                    return True
            return False

        def extract_projects(text):
            project_lines = []
            lines = text.split('\n')
            for line in lines:
                if 'project' in line.lower():
                    project_lines.append(line.strip())
            return project_lines

        # NLP check for each resume
        for text in resumes:
            info = {
                'Courses Found': any(word in text.lower() for word in keywords_courses),
                'Internship Intent': contains_internship(text),
                'Certifications': any(word in text.lower() for word in keywords_certification),
                'Project Dates Mentioned': any(word in text.lower() for word in keywords_dates),
                'Projects': extract_projects(text)
            }
            extra_details.append(info)

        return render_template('matchresume.html',
                               message="Top matching resumes:",
                               top_resumes=top_resumes,
                               similarity_scores=similarity_scores,
                               extra_details=extra_details)

    return render_template('matchresume.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
