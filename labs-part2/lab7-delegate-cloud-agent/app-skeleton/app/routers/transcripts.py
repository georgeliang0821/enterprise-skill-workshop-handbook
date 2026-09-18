from fastapi import APIRouter, status

from app.models.schemas import TranscriptUploadRequest, TranscriptUploadResponse

router = APIRouter(prefix="/transcripts", tags=["transcripts"])


@router.post("", response_model=TranscriptUploadResponse, status_code=status.HTTP_201_CREATED)
def uploadTranscript(body: TranscriptUploadRequest) -> TranscriptUploadResponse:
    raise NotImplementedError("uploadTranscript")
