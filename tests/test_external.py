"""Tests for the stub partner client.

The authenticated test reads EXTERNAL_API_KEY from the environment and SKIPS
CLEANLY when it is absent — locally and in any pipeline without the secret,
the suite stays green and the skip says why. Wiring the secret into CI so
this test actually runs is what some briefs on this repository are about.
"""
import os

import pytest

from app.external import MissingKeyError, fetch_partner_status


def test_without_a_key_the_client_fails_loud(monkeypatch):
    monkeypatch.delenv("EXTERNAL_API_KEY", raising=False)
    with pytest.raises(MissingKeyError):
        fetch_partner_status()


@pytest.mark.skipif(
    not os.environ.get("EXTERNAL_API_KEY"),
    reason="EXTERNAL_API_KEY is not set — the authenticated path only runs with the secret",
)
def test_with_a_key_the_client_answers():
    answer = fetch_partner_status()
    assert answer["partner"] == "ok"
    assert answer["key_fingerprint"].endswith("...")
