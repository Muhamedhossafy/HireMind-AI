from cv_parser.parser import extract_cv_data
from app.matching.final_score import calculate_final_score
import os


async def match_job_service(file, job_description):
    file_path = f"temp_{file.filename}"

    # حفظ الملف
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    try:
        # استخراج بيانات الـ CV
        cv_data = extract_cv_data(file_path)

        if not cv_data:
            return {"error": "Failed to parse CV"}

        # تجهيز البيانات للـ AI
        cv_data["skills_text"] = " ".join(cv_data.get("skills", []))
        cv_data["experience_text"] = " ".join(cv_data.get("experience", []))

        # تجهيز الـ Job Description
        jd_data = {
            "title": "Backend Developer",
            "skills": job_description.lower().split(),
            "description": job_description,
            "min_years_experience": 1,
            "max_years_experience": 5
        }

        # حساب النتيجة
        result = calculate_final_score(cv_data, jd_data)

        # رجوع النتيجة
        return {
            "match_score": result["final_score"] * 100,
            "decision": result["decision"],
            "skills_score": result["skills_score"],
            "experience_score": result["experience_score"],
            "skills_found": cv_data.get("skills", [])
        }

    finally:
        # حذف الملف حتى لو حصل error
        if os.path.exists(file_path):
            os.remove(file_path)