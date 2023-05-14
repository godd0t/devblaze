from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Label, Button

from devblaze.textual_utils.constants import CSS_PATH


class SuccessScreen(ModalScreen):
    """Screen with a dialog to quit."""

    CSS_PATH = CSS_PATH
    BINDINGS = [("enter", "on_success", "Ok")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Project created successfully!", id="success"),
            Button("Ok", variant="primary", id="ok"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok":
            self.app.exit()

    def action_on_success(self) -> None:
        self.app.exit()
