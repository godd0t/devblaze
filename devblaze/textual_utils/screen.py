from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Grid
from textual.widgets import (
    Input,
    TextLog,
    Label,
    Header,
    Footer,
    RadioSet,
    RadioButton,
)
from textual.reactive import reactive
from cookiecutter.main import cookiecutter

from devblaze.textual_utils.screens.error import ErrorScreen
from devblaze.textual_utils.screens.quit import QuitScreen
from devblaze.textual_utils.screens.success import SuccessScreen
from devblaze.textual_utils.constants import CSS_PATH


class CookiecutterApp(App[None]):
    """Prompts for project_type and project_name, then runs cookiecutter."""

    CSS_PATH = CSS_PATH
    BINDINGS = [
        ("q", "request_quit", "Quit"),
        ("enter", "on_success", "Ok"),
        ("enter", "on_error", "Ok"),
    ]

    # Reactive attributes

    project_type: str | None = reactive(None)
    project_name: str | None = reactive(None)
    app_name: str | None = reactive(None)
    project_base_name: str | None = reactive(None)
    use_git: bool = reactive(False)
    use_celery: bool = reactive(False)
    use_celery_beat: bool = reactive(False)
    use_postgres: bool = reactive(False)
    use_pytest: bool = reactive(False)
    use_ruff: bool = reactive(False)
    use_black: bool = reactive(False)
    use_docker: bool = reactive(False)
    use_make: bool = reactive(False)
    use_nginx: bool = reactive(False)
    use_traefik: bool = reactive(False)

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextLog(highlight=True, markup=True)
        with Horizontal():
            yield Label("Project Type", id="project_type_label")
            with RadioSet(id="project_type_set"):
                yield RadioButton("django", id="project_type")
                yield RadioButton("ddd")
        yield Grid(
            Input(
                placeholder="Enter project name", id="project_name",
            ),
            Input(placeholder="Enter app name", id="app_name"),
            Input(
                placeholder="Enter project base name",
                id="project_base_name",
            ),
            id="project_inputs_grid", classes="hidden"
        )
        with Horizontal():
            yield Label("Use Git", id="use_git_label", classes="hidden")
            with RadioSet(id="use_git_set", classes="hidden"):
                yield RadioButton("Yes", id="use_git")
                yield RadioButton("No")
        with Horizontal():
            yield Label("Use Celery", id="use_celery_label", classes="hidden")
            with RadioSet(id="use_postgres_set", classes="hidden"):
                yield RadioButton("Yes", id="use_celery")
                yield RadioButton("No")
        with Horizontal():
            with RadioSet(id="use_celery_set", classes="hidden"):
                yield RadioButton("Yes", id="use_celery_beat")
                yield RadioButton("No")
        # with VerticalScroll():
        #     yield Checkbox("Use Git", id="use_git", classes="hidden")
        #     yield Checkbox("Use Celery", id="use_celery", classes="hidden")
        #     yield Checkbox("Use Celery Beat", id="use_celery_beat", classes="hidden")
        #     yield Checkbox("Use Postgres", value=True, id="use_postgres", classes="hidden")
        #     yield Checkbox("Use Pytest", value=True, id="use_pytest", classes="hidden")
        #     yield Checkbox("Use Ruff", value=True, id="use_ruff", classes="hidden")
        #     yield Checkbox("Use Black", value=True, id="use_black", classes="hidden")
        #     yield Checkbox("Use Docker", id="use_docker", classes="hidden")
        #     yield Checkbox("Use Make", id="use_make", classes="hidden")
        #     yield Checkbox("Use Nginx", value=True, id="use_nginx", classes="hidden")
        #     yield Checkbox("Use Traefik", value=True, id="use_traefik", classes="hidden")
        yield Footer()

    def on_mount(self) -> None:
        # Focus the button with id first
        self.query_one("#project_type_set").focus()

    async def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.project_type = str(event.pressed.label)
        self.query_one("#project_type_set").add_class("hidden")
        self.query_one("#project_type_label").add_class("hidden")
        self.query_one("#project_inputs_grid").remove_class("hidden")
        self.query_one("#project_name").focus()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "project_name":
            self.project_name = event.value.strip()

        if event.input.id == "app_name":
            self.app_name = event.value.strip()

        if event.input.id == "project_base_name":
            self.query_one(TextLog).write(
                f"Project Type: {self.project_type}, Project Name: {self.project_name}, App Name: {self.app_name}, Project Base Name: {self.project_base_name}"
            )
            self.project_base_name = event.value.strip()
            self.query_one("#project_inputs_grid").add_class("hidden")
            self.query_one("#use_git_set").remove_class("hidden")
            self.query_one("#use_git_label").remove_class("hidden")
            self.query_one("#use_git_set").focus()
            self.use_git = self.query_one("#use_git").value
            self.query_one("#use_git_set").add_class("hidden")
            self.query_one("#use_git_label").add_class("hidden")
            self.query_one("#use_celery_set").remove_class("hidden")
            self.query_one("#use_celery_label").remove_class("hidden")
            self.query_one("#use_celery_set").focus()
            self.use_celery = self.query_one("#use_celery").value
            self.query_one("#use_celery_set").add_class("hidden")
            self.query_one("#use_celery_label").add_class("hidden")
            self.query_one("#use_celery_set").remove_class("hidden")
            self.query_one("#use_celery_label").remove_class("hidden")
            self.query_one("#use_celery_set").focus()
            self.use_celery_beat = self.query_one("#use_celery_beat").value
            self.query_one("#use_celery_set").add_class("hidden")
            self.query_one("#use_celery_label").add_class("hidden")
            # self.query_one("#use_postgres_set").remove_class("hidden")
            # self.query_one("#use_postgres_set").focus()
            # self.use_postgres = self.query_one("#use_postgres").value
            # self.query_one("#use_postgres_set").add_class("hidden")
            # self.query_one("#use_postgres_label").add_class("hidden")
            # self.query_one("#use_pytest_set").remove_class("hidden")
            # self.query_one("#use_pytest_set").focus()
            # self.use_pytest = self.query_one("#use_pytest").value
            # self.query_one("#use_pytest_set").add_class("hidden")
            # self.query_one("#use_pytest_label").add_class("hidden")
        # if event.input.id == "project_name":
        #     self.project_name = event.value.strip()
        #     self.query_one("#project_name").add_class("hidden")
        #     self.query_one("#app_name").remove_class("hidden")
        #     self.query_one("#app_name").focus()
        # elif event.input.id == "app_name":
        #     self.app_name = event.value
        #     self.query_one("#app_name").add_class("hidden")
        #     self.query_one("#project_base_name").remove_class("hidden")
        #     self.query_one("#project_base_name").focus()
        # elif event.input.id == "project_base_name":
        #     self.project_base_name = event.value
        #     self.query_one("#project_base_name").add_class("hidden")
        #     self.query_one("#use_git_set").remove_class("hidden")
        #     self.query_one("#use_git_set").focus()

    async def on_radio_set_changed_bool(self, event: RadioSet.Changed) -> None:
        self.use_git = bool(event.pressed.label)
        self.query_one("#use_git_set").add_class("hidden")
        self.query_one("#use_postgres_set").remove_class("hidden")
        self.query_one("#use_postgres_set").focus()
        self.use_postgres = bool(event.pressed.label)
        self.query_one("#use_postgres_set").add_class("hidden")
        self.query_one("#use_celery_set").remove_class("hidden")
        self.query_one("#use_celery_set").focus()
        self.use_celery = bool(event.pressed.label)
        self.query_one("#use_celery_set").add_class("hidden")

    def action_request_quit(self) -> None:
        self.push_screen(QuitScreen())

    def action_on_success(self) -> None:
        self.push_screen(SuccessScreen())

    def try_run_cookiecutter(self):
        self.query_one(TextLog).write(f"Project type: {self.project_type}")
        self.query_one(TextLog).write(f"Project name: {self.project_name}")
        self.query_one(TextLog).write(f"App name: {self.app_name}")
        self.query_one(TextLog).write(f"Project base name: {self.project_base_name}")
        self.query_one(TextLog).write(f"Use Git: {self.use_git}")

    def run_cookiecutter(
        self,
        project_type: str,
        project_name: str,
        app_name: str,
        project_base_name: str,
    ) -> None:
        try:
            cookiecutter(
                ".",
                no_input=True,
                extra_context={
                    "project_type": project_type,
                    "project_name": project_name,
                    "app_name": app_name,
                    "project_base_name": project_base_name,
                    "use_git": self.use_git,
                    "use_celery": self.use_celery,
                    "use_celery_beat": self.use_celery_beat,
                    "use_postgres": self.use_postgres,
                    "use_pytest": self.use_pytest,
                    "use_ruff": self.use_ruff,
                    "use_black": self.use_black,
                    "use_docker": self.use_docker,
                    "use_make": self.use_make,
                    "use_nginx": self.use_nginx,
                    "use_traefik": self.use_traefik,
                },
            )
            self.action_on_success()
        except Exception as e:
            self.query_one(TextLog).write(f"Error: {e}")
            self.push_screen(ErrorScreen(str(e)))


if __name__ == "__main__":
    app = CookiecutterApp()
    app.run()
