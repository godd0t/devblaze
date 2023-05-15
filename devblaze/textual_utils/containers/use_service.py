from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label

from devblaze.textual_utils.containers.base import Column
from devblaze.textual_utils.widgets.radio_sets import UseServiceRadioSet


class UseServiceBaseContainer(Horizontal):
    def __init__(self, service_name: str, **kwargs):
        super().__init__(**kwargs)
        self.service_name = service_name

    def compose(self) -> ComposeResult:
        with Column() as column:
            yield Label(
                f"Use {self.service_name.title()}",
                id=f"use_{self.service_name}_label",
                classes="use_service_label",
            )
            yield UseServiceRadioSet(id=f"{self.service_name}")
        yield column

    def on_mount(self, event: events.Mount) -> None:
        self.app.add_note(f"UseServiceContainer is running for {self.service_name}")
        self.query_one(UseServiceRadioSet).focus()
