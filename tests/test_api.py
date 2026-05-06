import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient) -> None:
        response = client.get("/")
        assert "SOC OPS" in response.text
        assert "PRESS START" in response.text
        assert "LVL 01" in response.text

    def test_home_sets_session_cookie(self, client: TestClient) -> None:
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient) -> None:
        # First visit to get session
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "🎯 FREE 🎯" in response.text
        assert "← Back" in response.text

    def test_board_has_25_squares(self, client: TestClient) -> None:
        client.get("/")
        response = client.post("/start")
        # Count the toggle buttons (squares with hx-post="/toggle/")
        assert response.text.count('hx-post="/toggle/') == 24  # 24 + 1 free space


class TestToggleSquare:
    def test_toggle_marks_square(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/toggle/0")
        assert response.status_code == 200
        # The response should contain the game screen with a marked square
        assert "🎯 FREE 🎯" in response.text


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "PRESS START" in response.text
        assert "LVL 01" in response.text


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "🎯 FREE 🎯" in response.text


class TestScavengerHuntMode:
    def test_mode_select_returns_scavenger_hunt_option(
        self, client: TestClient
    ) -> None:
        client.get("/")

        response = client.post("/mode-select")

        assert response.status_code == 200
        assert "Choose Your Mode" in response.text
        assert "Bingo" in response.text
        assert "Scavenger Hunt" in response.text

    def test_start_scavenger_returns_checklist_with_progress_meter(
        self, client: TestClient
    ) -> None:
        client.get("/")

        response = client.post("/start?mode=scavenger")

        assert response.status_code == 200
        assert "Scavenger Hunt" in response.text
        assert "0 / 24 found" in response.text
        assert 'role="progressbar"' in response.text
        assert 'aria-valuenow="0"' in response.text
        assert response.text.count('hx-post="/toggle/') == 24
        assert "FREE SPACE" not in response.text

    def test_scavenger_toggle_updates_progress(self, client: TestClient) -> None:
        client.get("/")
        client.post("/start?mode=scavenger")

        response = client.post("/toggle/0")

        assert response.status_code == 200
        assert "1 / 24 found" in response.text
        assert 'aria-valuenow="1"' in response.text

    def test_scavenger_completion_shows_completion_modal(
        self, client: TestClient
    ) -> None:
        client.get("/")
        client.post("/start?mode=scavenger")

        for item_id in range(24):
            response = client.post(f"/toggle/{item_id}")

        assert response.status_code == 200
        assert "24 / 24 found" in response.text
        assert "MISSION COMPLETE!" in response.text
        assert "You found every match on the list." in response.text

    def test_reset_after_scavenger_returns_start_screen(
        self, client: TestClient
    ) -> None:
        client.get("/")
        client.post("/start?mode=scavenger")

        response = client.post("/reset")

        assert response.status_code == 200
        assert "PRESS START" in response.text
        assert "Scavenger Hunt" not in response.text
