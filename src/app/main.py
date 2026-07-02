from fastapi import FastAPI
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
