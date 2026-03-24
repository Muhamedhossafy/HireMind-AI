import json
from cv_parser.parser import extract_cv_data
from app.adapters.cv_adapter import adapt_cv_for_matching
from app.matching.final_score import calculate_final_score


cv_path = "data/cvs/Muhamad_Ammar_CV.pdf"
job_path = "data/jobs/backend_dev.txt"


with open(job_path, "r", encoding="utf-8") as f:
    job_description = f.read()


cv_raw = extract_cv_data(cv_path)
cv_adapted = adapt_cv_for_matching(cv_raw)

job_data = {
    "title": "Backend Developer",
    "description": job_description,
    "cv_title": cv_raw.get("name", "")
}

result = calculate_final_score(cv_adapted, job_data)

print(json.dumps(result, indent=4))
