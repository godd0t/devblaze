from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Header, TextLog, Footer

from devblaze.textual_utils.containers.use_service import UseServiceBaseContainer


class UseServiceScreen(Screen):
    BINDINGS = [
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Notes"),
    ]
    screen_name = "use_service"

    def __init__(self, service_name: str, **kwargs):
        self.service_name = service_name
        self.screen_name = f"use_{self.service_name}"
        super().__init__(**kwargs)

    def get_service_name(self):
        return self.service_name

    def compose(self) -> ComposeResult:
        yield Container(
            Header(show_clock=False),
            # TextLog(classes="-hidden", wrap=False, highlight=True, markup=True),
            TextLog(wrap=False, highlight=True, markup=True),
            UseServiceBaseContainer(self.service_name),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.app.add_note(f"{self.screen_name} is running")
        self.app.assign_current_screen(self.screen_name)
