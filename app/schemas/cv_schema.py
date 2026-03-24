from pydantic import BaseModel
from typing import List, Optional


class CVSchema(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    skills: List[str]
    experience: List[str]
    education: List[str]