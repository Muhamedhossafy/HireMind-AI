def adapt_cv_for_matching(cv_data: dict) -> dict:
    return {
        "skills_text": " ".join(cv_data.get("skills", [])),
        "experience_text": " ".join(cv_data.get("experience", [])),
        "education_text": " ".join(cv_data.get("education", [])),
    }