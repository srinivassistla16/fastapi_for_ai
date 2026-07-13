import shutil
from pathlib import Path
from fastapi import File, UploadFile, APIRouter


router = APIRouter()
UPLOAD_DIR = Path("DEST_DOCS_FOR_AI")

@router.post("/api/upload_file")
async def upload_file(file: UploadFile = File(...)):
    # Save file efficiently using shutil
    with (UPLOAD_DIR / file.filename).open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


