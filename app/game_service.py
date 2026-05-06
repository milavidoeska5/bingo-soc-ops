from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    generate_board,
    generate_card_deck,
    generate_scavenger_hunt_items,
    get_current_card,
    get_scavenger_progress,
    get_winning_square_ids,
    is_deck_complete,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    game_mode: GameMode = GameMode.BINGO
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    current_card_index: int = 0  # For card deck mode

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_mode == GameMode.BINGO and self.game_state == GameState.BINGO

    @property
    def is_scavenger_mode(self) -> bool:
        return self.game_mode == GameMode.SCAVENGER

    @property
    def scavenger_progress(self) -> int:
        return get_scavenger_progress(self.board)

    @property
    def scavenger_total(self) -> int:
        return len(self.board)

    @property
    def is_scavenger_complete(self) -> bool:
        return (
            self.is_scavenger_mode
            and self.scavenger_total > 0
            and self.scavenger_progress == self.scavenger_total
        )

    @property
    def is_card_deck_mode(self) -> bool:
        return self.game_mode == GameMode.CARD_DECK

    @property
    def current_card(self) -> BingoSquareData | None:
        return get_current_card(self.board, self.current_card_index)

    @property
    def is_deck_complete(self) -> bool:
        return is_deck_complete(self.current_card_index, len(self.board))

    @property
    def card_deck_progress(self) -> int:
        """Return how many cards have been drawn.

        Current card index + 1, capped at total."""
        return min(self.current_card_index + 1, len(self.board))

    @property
    def card_deck_total(self) -> int:
        return len(self.board)

    @property
    def modal_title(self) -> str:
        if self.is_scavenger_mode:
            return "MISSION COMPLETE!"
        return "BINGO!"

    @property
    def modal_subtitle(self) -> str:
        if self.is_scavenger_mode:
            return "You found every match on the list."
        return "You completed a line!"

    @property
    def modal_button_label(self) -> str:
        if self.is_scavenger_mode:
            return "Review List"
        return "Keep Playing"

    @property
    def modal_caption(self) -> str:
        if self.is_scavenger_mode:
            return "Every prompt is checked off."
        return "Great job mixing and mingling!"

    def _create_board(self, mode: GameMode) -> list[BingoSquareData]:
        if mode == GameMode.SCAVENGER:
            return generate_scavenger_hunt_items()
        elif mode == GameMode.CARD_DECK:
            return generate_card_deck()
        return generate_board()

    def _complete_game(self, winning_line: BingoLine | None = None) -> None:
        self.winning_line = winning_line
        self.game_state = GameState.BINGO
        self.show_bingo_modal = True

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.game_mode = mode
        self.board = self._create_board(mode)
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False
        self.current_card_index = 0

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.is_scavenger_mode:
            if self.is_scavenger_complete:
                self._complete_game()
            return

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self._complete_game(bingo)

    def draw_next_card(self) -> None:
        """Advance to the next card in the deck.

        Does nothing if deck is complete."""
        if not self.is_deck_complete:
            self.current_card_index += 1

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.game_mode = GameMode.BINGO
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.current_card_index = 0

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
