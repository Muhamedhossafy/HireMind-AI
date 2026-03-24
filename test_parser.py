from cv_parser.parser import extract_cv_data
import json

cv_path = "data/cvs/Muhamad_Ammar_CV.pdf"

result = extract_cv_data(cv_path)

print(json.dumps(result, indent=4, ensure_ascii=False))
