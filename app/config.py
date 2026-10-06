"""Application settings.

NOTE, left here on purpose: this module reads EXTERNAL_API_KEY at import time,
while app/external.py reads the same variable again directly at call time.
Settings read in two different ways is the starting state some briefs on this
repository have you clean up — it is a seeded defect, not an accident.
"""
import os

EXTERNAL_API_KEY = os.environ.get("EXTERNAL_API_KEY", "")
