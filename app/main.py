"""A small payments-ledger service.

It is deliberately plain: one health route, one API route. The CI/CD briefs
are about the pipeline around this code, not the code.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.ledger import Ledger, validate_amount

app = FastAPI(title="catalog-python-cicd-template")
_ledger = Ledger()


class Payment(BaseModel):
    amount_paise: int


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/payments")
def record_payment(payment: Payment):
    problem = validate_amount(payment.amount_paise)
    if problem:
        raise HTTPException(status_code=400, detail=problem)
    return {"total_paise": _ledger.record(payment.amount_paise)}
