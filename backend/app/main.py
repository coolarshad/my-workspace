from fastapi import FastAPI

app = FastAPI(title="Workspace API")

@app.get("/")
def health():
    return {"status": "ok"}
