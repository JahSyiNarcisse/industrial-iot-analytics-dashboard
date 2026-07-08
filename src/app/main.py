from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from .routes import router

app = FastAPI(
    title="Industrial IoT Analytics Dashboard",
    description="Simulated manufacturing telemetry dashboard for cloud infrastructure learning.",
    version="0.1.0",
)

app.include_router(router)

@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Industrial IoT Analytics Dashboard API",
        "endpoints": [
            "/dashboard",
            "/health",
            "/cpu",
            "/memory",
            "/disk",
            "/environment",
            "/system",
            "/network",
            "/machines",
            "/sensors",
        ],
    }


@app.get("/dashboard", include_in_schema=False)
def dashboard():
    tpl_path = Path(__file__).parent / "templates" / "dashboard.html"
    if tpl_path.exists():
        return HTMLResponse(tpl_path.read_text(encoding='utf-8'))
    return HTMLResponse("<html><body><h1>Dashboard template not found</h1></body></html>")
