from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Header, TextLog, Footer

from devblaze.textual_utils.containers.project import (
    ProjectTypeContainer,
    ProjectInfoContainer,
)


class ProjectTypeScreen(Screen):
    BINDINGS = [
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Notes"),
    ]

    def __init__(self, screen_name: str, **kwargs):
        self.screen_name = screen_name
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield Container(
            Header(show_clock=False),
            # TextLog(classes="-hidden", wrap=False, highlight=True, markup=True),
            TextLog(wrap=False, highlight=True, markup=True),
            ProjectTypeContainer(),
        )
        yield Footer()


class ProjectInfoScreen(Screen):
    BINDINGS = [
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Notes"),
    ]

    def __init__(self, screen_name: str, **kwargs):
        self.screen_name = screen_name
        super().__init__(**kwargs)

    def compose(self) -> ComposeResult:
        yield Container(
            Header(show_clock=False),
            # TextLog(classes="-hidden", wrap=False, highlight=True, markup=True),
            TextLog(wrap=False, highlight=True, markup=True),
            ProjectInfoContainer(),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.app.add_note(f"{self.screen_name} is running")
        self.app.assign_current_screen(self.screen_name)
