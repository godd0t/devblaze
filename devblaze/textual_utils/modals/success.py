from __future__ import annotations
from typing import TYPE_CHECKING

from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label

if TYPE_CHECKING:
    from textual.app import ComposeResult


class SuccessScreen(ModalScreen):
    """Screen with a dialog to quit."""

    BINDINGS = [("enter", "on_success", "Ok")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Project created successfully!", id="success"),
            Button("Ok", variant="success", id="ok"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok":
            self.app.exit()

    def action_on_success(self) -> None:
        self.app.exit()
