import shutil
from cv_parser.parser import extract_cv_data

async def parse_cv_service(file):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = extract_cv_data(file_path)

    return result