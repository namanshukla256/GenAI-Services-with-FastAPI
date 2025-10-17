from fastapi import FastAPI, HTTPException, status, File
from typing import Annotated
from upload import save_file

app = FastAPI()

@app.post("/upload")
async def file_upload_controller(
    file: Annotated[UploadFile, File(description="Uploaded PDF Docuements")]
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            detail=f"Only uploading PDF documents are supported",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    try:
        await save_file(file)
    except Exception as e:
        raise HTTPException(
            detail=f"Error occurred while saving file - Error: {e}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return {"filename": file.filename, "message": "File uploaded successfully"}