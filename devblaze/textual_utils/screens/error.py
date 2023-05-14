from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Label, Button

from devblaze.textual_utils.constants import CSS_PATH


class ErrorScreen(ModalScreen):
    """Screen to display error messages."""

    CSS_PATH = CSS_PATH
    BINDINGS = [("enter", "on_error_ok", "Ok")]

    def __init__(self, error_message: str):
        super().__init__()
        self.error_message = error_message

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(self.error_message, id="error-message"),
            Button("Ok", variant="error", id="error-button"),
            id="error-dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "error-button":
            self.app.pop_screen()

    def action_on_error_ok(self) -> None:
        self.app.exit()
