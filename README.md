# 🤖 Smart Recruitment AI System

## 🌟 Project Overview

A powerful **AI-powered recruitment system** that automates the hiring process by:

* 📄 Parsing candidate CVs (PDF)
* 🧠 Extracting skills, experience, and key information
* 🎯 Matching candidates with job descriptions using AI
* 📊 Ranking multiple candidates based on relevance

> 💡 Built to simulate real-world recruitment systems used by top companies.

---

## 🏗️ Technical Stack

### 🧠 Backend (AI Engine)

* **Framework**: FastAPI
* **Language**: Python 3.10+
* **ML/NLP**: Sentence Transformers (`all-MiniLM-L6-v2`)
* **Server**: Uvicorn
* **File Handling**: UploadFile (multipart/form-data)

---

### 📊 AI & Matching Logic

* **Semantic Similarity** (NLP embeddings)
* **Skills Matching Algorithm**
* **Experience Extraction via Regex**
* **Weighted Scoring System**

---

## ⚙️ Core Features

### 📄 1. CV Parsing

* Extract:

  * Name
  * Email
  * Phone
  * Skills
  * Experience
  * Education

---

### 🎯 2. Job Matching

* Compare CV with job description
* Generate:

  * Match Score (%)
  * Decision (ACCEPT / REVIEW / REJECT)
  * Skills Score
  * Experience Score

---

### 🏆 3. Candidate Ranking

* Upload multiple CVs
* Rank candidates based on:

  * Skills relevance
  * Experience match
  * Semantic similarity

---

## 📸 API Demo (Swagger UI)

### 🔗 Access API Docs

```
http://127.0.0.1:8000/docs
```

### Example Response

```json
{
  "match_score": 89.31,
  "decision": "REVIEW",
  "skills_score": 0.97,
  "experience_score": 0.46,
  "skills_found": ["python", "sql", "react"]
}
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Project

```bash
git clone https://github.com/your-username/smart-recruitment-ai.git
cd smart-recruitment-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```
smart-recruitment-ai/
│
├── app/
│   ├── main.py                  # FastAPI entry point
│   │
│   ├── services/               # Business logic
│   │   ├── parse_service.py
│   │   ├── match_service.py
│   │   └── ranking_service.py
│   │
│   ├── matching/               # AI scoring logic
│   │   └── final_score.py
│
├── cv_parser/
│   └── parser.py               # CV extraction logic
│
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

### Step 1: CV Parsing

* Extract raw text from PDF
* Clean and normalize text
* Detect skills & experience

---

### Step 2: AI Matching

* Convert text → embeddings
* Compare:

  * CV vs Job Description
* Calculate similarity score

---

### Step 3: Scoring System

```text
Final Score = (Skills Score × 0.6) + (Experience Score × 0.4)
```

---

### Step 4: Decision Logic

```python
if score > 0.75:
    ACCEPT
elif score > 0.5:
    REVIEW
else:
    REJECT
```

---

## 🔌 API Endpoints

### 📄 Parse CV

```
POST /api/ai/parse-cv
```

---

### 🎯 Match Job

```
POST /api/ai/match-job
```

**Body:**

* file: PDF
* job_description: string

---

### 🏆 Rank Candidates

```
POST /api/ai/rank-candidates
```

**Body:**

* files: multiple PDFs
* job_description: string

---

## 🧪 Example cURL

```bash
curl -X POST \
  http://127.0.0.1:8000/api/ai/match-job \
  -F "file=@cv.pdf" \
  -F "job_description=Looking for a Python developer"
```

---

## 🚀 Future Improvements

* 🌐 Frontend UI (React)
* 🤖 Better NLP models (BERT / GPT)
* 📊 Dashboard analytics
* 📌 Skill gap detection
* 🧾 Auto CV feedback system

---

## 🧠 Why This Project is Powerful

* Real-world AI use case
* Combines:

  * NLP
  * Backend APIs
  * File processing

---

## 🤝 Contributing

1. Fork the repo
2. Create feature branch
3. Commit changes
4. Open Pull Request

---

## 📜 License

MIT License

---

## 📧 Contact

* 👤 **Muhamad Ammar**
* ✉️ Email: [muhamedammar0900@gmail.com](mailto:muhamedammar0900@gmail.com)
* 🔗 LinkedIn: [https://www.linkedin.com/in/muhamad-ammar-18b427306](https://www.linkedin.com/in/muhamad-ammar-18b427306)
