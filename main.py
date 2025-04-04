from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LLM_MVP backend is working!"}
