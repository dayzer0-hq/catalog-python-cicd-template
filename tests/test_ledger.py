import pytest

from app.ledger import MAX_AMOUNT_PAISE, Ledger, validate_amount


@pytest.mark.parametrize("paise", [1, 49_900, MAX_AMOUNT_PAISE])
def test_validate_amount_accepts(paise):
    assert validate_amount(paise) is None


@pytest.mark.parametrize("paise", [0, -500, MAX_AMOUNT_PAISE + 1, "100", 1.5])
def test_validate_amount_rejects(paise):
    assert validate_amount(paise) is not None


def test_ledger_keeps_a_running_total():
    ledger = Ledger()
    assert ledger.record(100) == 100
    assert ledger.record(250) == 350
