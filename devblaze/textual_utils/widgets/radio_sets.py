from __future__ import annotations
from typing import TYPE_CHECKING
from textual.widgets import RadioButton, RadioSet

from devblaze.textual_utils.constants import PROJECT_TYPE_OPTIONS, USE_SERVICE_ANSWERS
from devblaze.textual_utils.modals.success import SuccessScreen

if TYPE_CHECKING:
    from textual import events
    from textual.app import ComposeResult


class ProjectTypeRadioSet(RadioSet):
    def compose(self) -> ComposeResult:
        for option in PROJECT_TYPE_OPTIONS:
            yield RadioButton(option["name"], id=option["id"], value=option["value"])

    def on_mount(self, event: events.Mount) -> None:
        self.app.add_note("ProjectTypeRadioSet is running")

    def on_radio_button_changed(self, event: RadioButton.Changed) -> None:
        self.app.add_cookiecutter_context(project_type=event.radio_button.id)
        self.app.switch_screen(self.app.next_screen)


class UseServiceRadioSet(RadioSet):
    def compose(self) -> ComposeResult:
        for option in USE_SERVICE_ANSWERS:
            yield RadioButton(option["name"], id=option["id"], value=option["value"])

    def on_mount(self, event: events.Mount) -> None:
        self.app.add_note("UseServiceRadioSet is running")

    def on_radio_button_changed(self, event: RadioButton.Changed) -> None:
        service_key = self.screen.screen_name
        service_value = event.radio_button.value
        self.app.add_cookiecutter_context(**{service_key: service_value})
        if self.app.next_screen:
            self.app.push_screen(self.app.next_screen)
        else:
            self.app.push_screen(SuccessScreen())
