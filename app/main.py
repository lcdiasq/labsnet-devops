from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import health
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LabsNet DevOps", version="1.0")

@app.on_event("startup")
def startup_event():
    logger.info("Aplicação iniciada")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Aplicação finalizada")

# Rotas API
app.include_router(health.router)

# Frontend (servir arquivos estáticos)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def dashboard():
    return FileResponse("app/static/index.html")

