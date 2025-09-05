from fastapi import FastAPI
app = FastAPI(title="Demo API")
@app.get("/ping")
def ping(): return {"status":"ok"}
