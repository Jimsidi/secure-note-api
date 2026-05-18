from fastapi import FastAPI

app = FastAPI(title="Secure Note API", version="1.0.0")

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