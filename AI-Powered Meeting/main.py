from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, Meeting, Insight
from llm import extract_insights
import json

app = FastAPI(title="AI-Powered Meeting Insights")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_transcript(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    transcript = content.decode("utf-8")
    
    # Extract insights using LLM
    insights_data = extract_insights(transcript)
    
    # Save to database
    meeting = Meeting(raw_transcript=transcript)
    db.add(meeting)
    db.commit()
    db.refresh(meeting)
    
    insight = Insight(
        meeting_id=meeting.id,
        action_items=json.dumps(insights_data.get("action_items", [])),
        risks=json.dumps(insights_data.get("risks", [])),
        decisions=json.dumps(insights_data.get("decisions", []))
    )
    db.add(insight)
    db.commit()
    
    return {"meeting_id": meeting.id, "insights": insights_data}

@app.get("/search/keyword")
def search_by_keyword(keyword: str = Query(...), db: Session = Depends(get_db)):
    meetings = db.query(Meeting).filter(Meeting.raw_transcript.contains(keyword)).all()
    return [{"id": m.id, "date": m.date, "participants": m.participants} for m in meetings]

@app.get("/search/participant")
def search_by_participant(participant: str = Query(...), db: Session = Depends(get_db)):
    meetings = db.query(Meeting).filter(Meeting.participants.contains(participant)).all()
    return [{"id": m.id, "date": m.date, "participants": m.participants} for m in meetings]

@app.get("/insights/{meeting_id}")
def get_insights(meeting_id: int, db: Session = Depends(get_db)):
    insight = db.query(Insight).filter(Insight.meeting_id == meeting_id).first()
    if not insight:
        raise HTTPException(status_code=404, detail="Insights not found")
    
    return {
        "action_items": json.loads(insight.action_items),
        "risks": json.loads(insight.risks),
        "decisions": json.loads(insight.decisions)
    }

