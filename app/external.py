"""A STUB client for a partner API.

It never makes a network call: it stands in for a real integration so the
pipeline around it can be built and tested safely.
"""
import os


class MissingKeyError(RuntimeError):
    """Raised when EXTERNAL_API_KEY is not set."""


def fetch_partner_status():
    """Pretend to ask the partner API how it is doing.

    Reads EXTERNAL_API_KEY directly from the environment (see the note in
    app/config.py about the two read paths). Raises MissingKeyError without
    a key; returns a canned answer with one.
    """
    key = os.getenv("EXTERNAL_API_KEY")
    if not key:
        raise MissingKeyError("EXTERNAL_API_KEY is not set")
    return {"partner": "ok", "key_fingerprint": key[:4] + "..."}
