from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz_answers_ok():
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_payments_records_and_refuses():
    ok = client.post("/payments", json={"amount_paise": 500})
    assert ok.status_code == 200
    assert ok.json()["total_paise"] >= 500

    bad = client.post("/payments", json={"amount_paise": 0})
    assert bad.status_code == 400
