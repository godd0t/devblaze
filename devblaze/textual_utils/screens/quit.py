from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Label, Button

from devblaze.textual_utils.constants import CSS_PATH


class QuitScreen(ModalScreen):
    """Screen with a dialog to quit."""

    CSS_PATH = CSS_PATH
    BINDINGS = [("enter", "confirm_quit", "Confirm Quit")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()

    def action_confirm_quit(self) -> None:
        self.app.exit()
