from fastapi import FastAPI

from app.routers import meetings, search, transcripts

app = FastAPI(title="AI Meeting Intelligence Portal API", version="0.1.0")
app.include_router(transcripts.router)
app.include_router(meetings.router)
app.include_router(search.router)
