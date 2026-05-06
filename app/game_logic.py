import functools
import random

from app.data import FREE_SPACE, QUESTIONS
from app.models import BingoLine, BingoSquareData

BOARD_SIZE = 5
CENTER_INDEX = 12  # 5x5 grid, center is index 12 (row 2, col 2)


def generate_board() -> list[BingoSquareData]:
    """Generate a new 5x5 bingo board."""
    questions = iter(random.sample(QUESTIONS, 24))
    return [
        BingoSquareData(id=i, text=FREE_SPACE, is_marked=True, is_free_space=True)
        if i == CENTER_INDEX
        else BingoSquareData(id=i, text=next(questions))
        for i in range(BOARD_SIZE * BOARD_SIZE)
    ]


def generate_scavenger_hunt_items() -> list[BingoSquareData]:
    """Generate a flat list of scavenger hunt questions."""
    return [
        BingoSquareData(id=i, text=question) for i, question in enumerate(QUESTIONS)
    ]


def toggle_square(
    board: list[BingoSquareData], square_id: int
) -> list[BingoSquareData]:
    """Toggle a square's marked state. Returns a new board list."""
    return [
        sq.model_copy(update={"is_marked": not sq.is_marked})
        if sq.id == square_id and not sq.is_free_space
        else sq
        for sq in board
    ]


@functools.cache
def _get_winning_lines() -> tuple[BingoLine, ...]:
    """Get all possible winning lines (cached)."""
    lines: list[BingoLine] = []

    for row in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for col in range(BOARD_SIZE)]
        lines.append(BingoLine(type="row", index=row, squares=squares))

    for col in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for row in range(BOARD_SIZE)]
        lines.append(BingoLine(type="column", index=col, squares=squares))

    lines.append(BingoLine(type="diagonal", index=0, squares=[0, 6, 12, 18, 24]))
    lines.append(BingoLine(type="diagonal", index=1, squares=[4, 8, 12, 16, 20]))

    return tuple(lines)


def check_bingo(board: list[BingoSquareData]) -> BingoLine | None:
    """Check if there's a bingo and return the winning line."""
    if len(board) < BOARD_SIZE * BOARD_SIZE:
        return None
    return next(
        (
            line
            for line in _get_winning_lines()
            if all(board[idx].is_marked for idx in line.squares)
        ),
        None,
    )


def get_winning_square_ids(line: BingoLine | None) -> set[int]:
    """Get the square IDs that are part of a winning line."""
    return set(line.squares) if line else set()


def get_scavenger_progress(items: list[BingoSquareData]) -> int:
    """Count how many scavenger hunt items are marked."""
    return sum(1 for item in items if item.is_marked)


def generate_card_deck() -> list[BingoSquareData]:
    """Generate a shuffled deck of cards (all 24 questions)."""
    shuffled_questions = random.sample(QUESTIONS, len(QUESTIONS))
    return [
        BingoSquareData(id=i, text=question)
        for i, question in enumerate(shuffled_questions)
    ]


def get_current_card(
    deck: list[BingoSquareData], current_index: int
) -> BingoSquareData | None:
    """Get the card at the current index.

    Returns None if index is out of bounds."""
    if 0 <= current_index < len(deck):
        return deck[current_index]
    return None


def is_deck_complete(current_index: int, deck_size: int) -> bool:
    """Check if all cards in the deck have been drawn."""
    return current_index >= deck_size
