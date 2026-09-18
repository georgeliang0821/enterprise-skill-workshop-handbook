from typing import List

from fastapi import APIRouter, Query

from app.models.schemas import SearchResult

router = APIRouter(prefix="/search", tags=["search"])


@router.get("", response_model=List[SearchResult])
def searchTranscripts(meetingId: str = Query(...), q: str = Query(..., description="搜尋關鍵字")) -> List[SearchResult]:
    raise NotImplementedError("searchTranscripts")
