from fastapi import FastAPI, UploadFile, File
from app.services.parse_service import parse_cv_service
from app.services.match_service import match_job_service
from app.services.ranking_service import rank_candidates_service

app = FastAPI(title="Smart Recruitment AI")


# 1️⃣ Parse CV
@app.post("/api/ai/parse-cv")
async def parse_cv(file: UploadFile = File(...)):
    return await parse_cv_service(file)


# 2️⃣ Match Job
@app.post("/api/ai/match-job")
async def match_job(file: UploadFile = File(...), job_description: str = ""):
    return await match_job_service(file, job_description)


# 3️⃣ Rank Candidates
@app.post("/api/ai/rank-candidates")
async def rank_candidates(files: list[UploadFile], job_description: str = ""):
    return await rank_candidates_service(files, job_description)