from fastapi import APIRouter, Query
from app.services.calculator import sum_numbers

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/sum")
def sum_route(a: int = Query(...), b: int = Query(...)):
    result = sum_numbers(a, b)
    return {"result": result}
