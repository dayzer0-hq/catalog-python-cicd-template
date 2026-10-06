# catalog-python-cicd-template

A small **Python + FastAPI** payments service for DayZer0 CI/CD briefs. Your project
repository is provisioned from this template: the service, its pytest suite and its pinned
requirements already exist and pass. **The pipeline around them does not — building it is
your project.** There is deliberately no `.github/workflows` directory here.

## What's here

- `app/main.py` — the FastAPI app: `GET /healthz`, `POST /payments`.
- `app/ledger.py` — the business logic, plain functions and a `Ledger` class.
- `app/external.py` — a **stub** partner-API client. It makes no network calls; it reads
  `EXTERNAL_API_KEY` and fails loud without it.
- `app/config.py` and `app/settings_example.py` — the settings, in a deliberately sloppy
  starting state (the key is read in two different ways, and the example file commits a
  placeholder token). Some briefs have you clean exactly this up; it is seeded, not an accident.
- `tests/` — the pytest suite, passing from a clean clone. `tests/test_external.py` reads
  `EXTERNAL_API_KEY` from the environment and **skips cleanly when it is absent**.
- `requirements.txt` — pinned, on purpose; CI caching is keyed on this file.

## Requirements

- Python 3.11 or newer.

## Run it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8080
```

Then, in another terminal:

```bash
curl http://localhost:8080/healthz
# {"status":"ok"}
```

## Test it

```bash
pytest
```

One test skips without `EXTERNAL_API_KEY` set — that is expected, and the skip message says why.

## What you add

Your tickets have you build the GitHub Actions pipeline: workflows, caching or secrets
handling as your brief asks. The service is finished — do not add features to it unless a
ticket says so. One ticket, one branch (`issue-N-<slug>`), one pull request with `Closes #N`.
