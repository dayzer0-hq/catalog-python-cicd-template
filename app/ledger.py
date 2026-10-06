"""Plain business logic, kept out of the FastAPI layer so it tests without HTTP."""

# The largest single payment accepted: Rs 1,00,000 in paise.
MAX_AMOUNT_PAISE = 100_000_00


def validate_amount(paise):
    """Return a problem string, or None when the amount is acceptable."""
    if not isinstance(paise, int) or isinstance(paise, bool) or paise <= 0:
        return "amount must be a positive integer of paise"
    if paise > MAX_AMOUNT_PAISE:
        return "amount exceeds the single-payment limit"
    return None


class Ledger:
    """A running total of recorded payments."""

    def __init__(self):
        self.total_paise = 0

    def record(self, paise):
        """Add an already-validated amount and return the new total."""
        self.total_paise += paise
        return self.total_paise
