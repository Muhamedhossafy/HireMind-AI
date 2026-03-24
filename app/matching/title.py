from app.core.embeddings import compute_similarity


def match_title(cv_title: str, job_title: str) -> float:
    return compute_similarity(cv_title or "", job_title)