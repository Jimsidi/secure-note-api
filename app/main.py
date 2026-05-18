from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

app = FastAPI(title="Secure Note API", version="1.0.0")

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityHeadersMiddleware)

notes = {}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/notes/{note_id}")
def create_note(note_id: str, content: str):
    notes[note_id] = content
    return {"id": note_id, "content": content}

@app.get("/notes/{note_id}")
def get_note(note_id: str):
    if note_id not in notes:
        return {"error": "Note not found"}
    return {"id": note_id, "content": notes[note_id]}