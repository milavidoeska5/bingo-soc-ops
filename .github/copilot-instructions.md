# Soc Ops — Agent Instructions

> **MANDATORY before every commit:**
> ```bash
> uv run ruff check .   # must pass — no errors
> uv run pytest         # must pass — no failures
> ```
> Never skip these. Fix all issues before marking work complete.

**Soc Ops** is a Social Bingo game (FastAPI + Jinja2 + HTMX). Players find people matching icebreaker questions to mark squares and get 5 in a row.

## Commands

```bash
uv run uvicorn app.main:app --reload --port 8000  # dev server
uv run pytest                                       # tests
uv run ruff check .                                 # lint
```

## Architecture

| File | Role |
|------|------|
| `app/main.py` | FastAPI routes → Jinja2 partials via HTMX POST |
| `app/game_logic.py` | Pure functions: board gen, toggle, bingo detection |
| `app/game_service.py` | `GameSession` dataclass + in-memory `_sessions` dict |
| `app/models.py` | Pydantic models: `GameState`, `BingoSquareData`, `BingoLine` |
| `app/data.py` | `QUESTIONS` list — exactly 24 items required |
| `app/templates/components/` | Partials returned by HTMX endpoints |

- Sessions keyed by UUID in a signed cookie (`SessionMiddleware` / `itsdangerous`)
- HTMX POSTs return full HTML partials — no JSON, no custom JS
- Center square (index 12) is always `FREE SPACE` (pre-marked)

## Conventions

- Python: snake_case, full type hints, `frozen=True` Pydantic models
- CSS: custom utility classes in `app/static/css/app.css` — see [css-utilities.instructions.md](instructions/css-utilities.instructions.md)
- Tests: `httpx.TestClient`; match style in `tests/test_api.py` and `tests/test_game_logic.py`
