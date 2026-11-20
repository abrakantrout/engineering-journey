from fastapi import FastAPI, File, UploadFile

app = FastAPI

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File upload successfully"
    }

# to save the file locally:(create and uploads folder)
import shutil

@app.post("/upload-save")
async def upload_and_save(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File saved successfully"}