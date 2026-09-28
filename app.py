from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from hindsight_client import Hindsight

app = FastAPI(title="IncidentMind")

memory = Hindsight(base_url="http://localhost:8888")
BANK_ID = "incidentmind"


class MemoryRequest(BaseModel):
    incident: str


class AskRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/remember")
def remember(data: MemoryRequest):
    try:
        result = memory.retain(
            bank_id=BANK_ID,
            content=data.incident
        )
        return {
            "status": "remembered",
            "message": "Incident stored in Hindsight.",
            "result": str(result),
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}


@app.post("/ask")
def ask(data: AskRequest):
    try:
        result = memory.reflect(
            bank_id=BANK_ID,
            query=data.question,
        )
        answer = getattr(result, "text", str(result))
        return {"status": "success", "answer": answer}
    except Exception as e:
        return {"status": "error", "error": str(e)}
