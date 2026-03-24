from app.core.embeddings import compute_similarity


def match_experience(cv_exp_text: str, job_description: str) -> float:
    return compute_similarity(cv_exp_text, job_description)