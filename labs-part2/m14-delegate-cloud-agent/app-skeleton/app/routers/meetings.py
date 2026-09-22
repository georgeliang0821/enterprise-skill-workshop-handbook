from typing import List

from fastapi import APIRouter

from app.models.schemas import ActionItem, ErrorResponse, MeetingSummary, Risk

router = APIRouter(prefix="/meetings", tags=["meetings"])

NOT_FOUND = {404: {"model": ErrorResponse, "description": "找不到指定的會議"}}


@router.get("/{meetingId}/summary", response_model=MeetingSummary, responses=NOT_FOUND)
def getMeetingSummary(meetingId: str) -> MeetingSummary:
    raise NotImplementedError("getMeetingSummary")


@router.get("/{meetingId}/action-items", response_model=List[ActionItem], responses=NOT_FOUND)
def getActionItems(meetingId: str) -> List[ActionItem]:
    raise NotImplementedError("getActionItems")


@router.get("/{meetingId}/risks", response_model=List[Risk], responses=NOT_FOUND)
def getMeetingRisks(meetingId: str) -> List[Risk]:
    raise NotImplementedError("getMeetingRisks")
