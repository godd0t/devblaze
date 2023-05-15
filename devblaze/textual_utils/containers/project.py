from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Label, Input

from devblaze.textual_utils.containers.base import Column
from devblaze.textual_utils.widgets.inputs import ValidatedInput, ProjectNameInput
from devblaze.textual_utils.widgets.radio_sets import ProjectTypeRadioSet


class ProjectTypeContainer(Horizontal):
    def compose(self) -> ComposeResult:
        with Column() as column:
            yield Label("Choose Project Type", id="project_type_label")
            yield ProjectTypeRadioSet(id="project_type")
        yield column

    # def on_input_changed(self, event: Input.Changed) -> None:
    #     self.app.add_note(f"event attributes: {event.__dict__}")
    #
    # def on_input_submitted(self, event: Input.Submitted) -> None:
    #     self.app.add_note(f"event attributes: {event.__dict__}")

    def on_mount(self, event: events.Mount) -> None:
        self.app.add_note("ProjectTypeContainer is running")
        self.app.add_note(f"Current Screen: {self.screen.screen_name}")
        self.app.assign_current_screen(self.screen.screen_name)
        self.query_one(ProjectTypeRadioSet).focus()


class ProjectInfoContainer(Horizontal):
    project_name = reactive(None)
    project_info = reactive(None)
    app_name = reactive(None)
    context = {}

    def compose(self) -> ComposeResult:
        with Column() as column:
            yield Label("Project Name")
            yield ProjectNameInput(id="project_name")
            yield Label("Project Info")
            yield ValidatedInput(id="project_info")
            yield Label("App Name")
            yield ValidatedInput(id="app_name")
        yield column

    def on_mount(self) -> None:
        self.app.assign_current_screen(self.screen.screen_name)
        self.screen.focus_next()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one(ProjectNameInput).project_name = event.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.app.add_note(f"event value: {event.value}")
        self.screen.focus_next()
        setattr(self, event.input.id, event.value)
        self.context.update({event.input.id: event.value})
        if self.app_name:
            self.app.add_cookiecutter_context(**self.context)
            self.app.push_screen(self.app.next_screen)
