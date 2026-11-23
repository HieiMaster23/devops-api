from fastapi import FastAPI

app = FastAPI(title="DevOps API")


@app.get("/health")
def health():
    return {"status": "ok"}
