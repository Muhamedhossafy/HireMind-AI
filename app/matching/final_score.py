from app.config.weights import (
    SKILLS_WEIGHT,
    TITLE_WEIGHT,
    EXPERIENCE_WEIGHT,
)
from app.config.thresholds import (
    ACCEPT_THRESHOLD,
    REVIEW_THRESHOLD,
)
from .skills import match_skills
from .title import match_title
from .experience import match_experience


def calculate_final_score(cv_data: dict, job_data: dict) -> dict:

    skills_score = match_skills(
        cv_data["skills_text"], job_data["description"]
    )

    title_score = match_title(
        job_data.get("cv_title", ""),
        job_data.get("title", "")
    )

    experience_score = match_experience(
        cv_data["experience_text"], job_data["description"]
    )

    final = (
        skills_score * SKILLS_WEIGHT +
        title_score * TITLE_WEIGHT +
        experience_score * EXPERIENCE_WEIGHT
    )

    if final >= ACCEPT_THRESHOLD:
        decision = "ACCEPT"
    elif final >= REVIEW_THRESHOLD:
        decision = "REVIEW"
    else:
        decision = "REJECT"

    return {
        "skills_score": skills_score,
        "title_score": title_score,
        "experience_score": experience_score,
        "final_score": final,
        "decision": decision
    }