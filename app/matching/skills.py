from app.core.embeddings import compute_similarity


SIMILARITY_THRESHOLD = 0.6


def match_skills(cv_skills: list[str], job_skills: list[str]) -> float:
    """
    Compare CV skills vs Job skills using semantic similarity
    """

    if not cv_skills or not job_skills:
        return 0.0

    matched = 0

    for job_skill in job_skills:
        for cv_skill in cv_skills:
            score = compute_similarity(cv_skill, job_skill)

            if score >= SIMILARITY_THRESHOLD:
                matched += 1
                break

    return matched / len(job_skills)


def get_missing_skills(cv_skills: list[str], job_skills: list[str]) -> list[str]:
    """
    Return skills missing from CV
    """

    missing = []

    for job_skill in job_skills:
        found = False

        for cv_skill in cv_skills:
            score = compute_similarity(cv_skill, job_skill)

            if score >= SIMILARITY_THRESHOLD:
                found = True
                break

        if not found:
            missing.append(job_skill)

    return missing