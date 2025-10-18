from fastapi import FastAPI
from orchestrator.api.hire_agent import router as hire_router

app = FastAPI(title="Company OS Orchestrator")

app.include_router(hire_router, prefix="/hire", tags=["Hiring"])

@app.get("/")
async def root():
    return {"status": "ok", "message": "Company OS orchestrator running"}
