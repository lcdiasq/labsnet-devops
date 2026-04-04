from fastapi import FastAPI
from app.routes import health
import logging

# Configuração básica de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LabsNet API", version="1.0")

@app.on_event("startup")
def startup_event():
    logger.info("🚀 Aplicação iniciada com sucesso")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("🛑 Aplicação finalizada")

# Rotas
app.include_router(health.router)
