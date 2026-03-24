from cv_parser.parser import extract_cv_data
from app.matching.final_score import calculate_final_score

async def rank_candidates_service(files, job_description):

    results = []

    jd_data = {
        "title": "Backend Developer",
        "skills": job_description.lower().split(),
        "min_years_experience": 1,
        "max_years_experience": 5
    }

    for file in files:
        file_path = f"temp_{file.filename}"

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        cv_data = extract_cv_data(file_path)

        score = calculate_final_score(cv_data, jd_data)

        results.append({
            "name": cv_data.get("name"),
            "score": score.final_score
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)