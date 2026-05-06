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

## Design Guide

Use this guide for all UI updates so the app stays playful, readable, and consistent.

### Visual Direction

- Style target: playful pastel-bright, energetic, social, and celebratory
- Keep backgrounds soft; use vivid accents for calls to action and win states
- Favor rounded corners, layered shadows, and selective glow for emphasis
- Avoid flat monochrome screens unless intentionally used as contrast

### Color and Contrast

- Keep body text high contrast on light surfaces
- Reserve strongest accent colors for primary actions and key feedback
- Marked squares should feel rewarding; winning states should be clearly distinct
- Validate text contrast against WCAG AA before finalizing

### Typography

- Preserve the existing system font stack for performance and compatibility
- Use heavier weights and letter spacing for headings and game moments
- Keep body copy clean and legible; avoid decorative effects on long text
- Limit all-caps to short UI labels and buttons

### Motion and Feedback

- Use short, smooth transitions (around 200 to 250 ms) for interactive elements
- Prefer meaningful animation: entrance, celebration, and state change cues
- Respect reduced-motion users with `prefers-reduced-motion` behavior
- Do not stack multiple loud animations on the same element

### Component Rules

- Start screen should feel inviting and game-like with a clear primary action
- Board interactions must remain immediate, readable, and touch-friendly
- Free-space and win-line states must remain easy to identify at a glance
- Modal dialogs must be centered, readable, and fully usable on small screens

### CSS and Implementation Guardrails

- Do not use utility class names that are not defined in `app/static/css/app.css`
- For critical overlays and dialogs, prefer component-specific classes over long utility chains
- Add concise comments only where intent is non-obvious
- Keep styling changes scoped; avoid unrelated refactors in the same edit

### Responsive and Accessibility Requirements

- Ensure tap targets are comfortable on mobile
- Check layout behavior on narrow and short viewports
- Preserve semantic labels and ARIA states already used by the board/buttons
- Keep keyboard and screen-reader behavior unchanged or improved

### Validation Checklist For UI Changes

- Run `uv run ruff check .`
- Run `uv run pytest`
- Verify start screen, board, and modal states in browser
- Verify win state and modal readability on mobile-sized viewport
