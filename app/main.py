from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI running on local Mac!"}

@app.get("/health")
def health():
    return {"status": "ok"}
