from __future__ import annotations
from typing import TYPE_CHECKING
from rich.console import RenderableType
from textual.app import App
from textual.widgets import TextLog

from devblaze.textual_utils.constants import USE_SERVICE_TYPES
from devblaze.textual_utils.screens.project import ProjectTypeScreen, ProjectInfoScreen
from devblaze.textual_utils.screens.use_service import UseServiceScreen

if TYPE_CHECKING:
    pass


class BaseApp(App):
    CSS_PATH = [
        "../static/test.css",
        "../static/use-service.css",
        "../static/project-info.css",
        "../static/modals.css",
    ]
    BINDINGS = [
        ("f1", "app.toggle_class('TextLog', '-hidden')", "Notes"),
    ]
    SCREEN_NAMES = {}
    cookiecutter_context = {}
    current_screen = None
    next_screen = None

    def on_mount(self) -> None:
        self.install_initial_screen()
        self.install_project_additional_screens()
        self.add_service_screens()
        self.push_screen("project_type")

    def install_initial_screen(self) -> None:
        screen_name = "project_type"
        screen_class = ProjectTypeScreen(screen_name=screen_name)
        self.install_screen(screen_class, name=screen_name)
        self.SCREEN_NAMES[screen_name] = screen_class

    def install_project_additional_screens(self):
        screen_name = "project_info"
        screen_class = ProjectInfoScreen(screen_name=screen_name)
        self.install_screen(screen_class, name=screen_name)
        self.SCREEN_NAMES[screen_name] = screen_class

    def add_service_screens(self):
        for service_name in USE_SERVICE_TYPES:
            screen_class = UseServiceScreen(service_name)
            screen_name = screen_class.screen_name
            self.install_screen(screen_class, name=screen_class.screen_name)
            self.SCREEN_NAMES[screen_name] = screen_class

    def add_note(self, renderable: RenderableType) -> None:
        self.query_one(TextLog).write(renderable)

    # Check if keys in cookiecutter_context exist
    def check_cookiecutter_context(self, keys: list) -> bool:
        return all(key in self.cookiecutter_context for key in keys)

    # Add key, value pairs to cookiecutter_context
    def add_cookiecutter_context(self, **kwargs) -> None:
        self.cookiecutter_context.update(kwargs)

    def get_cookiecutter_context(self) -> dict:
        return self.cookiecutter_context

    def assign_current_screen(self, screen: str) -> None:
        self.current_screen = screen
        self.assign_next_screen(screen)

    def assign_next_screen(self, screen: str) -> None:
        self.add_note(f"Screens: {self.SCREEN_NAMES}")
        self.add_note(f"Screen passed to assign_next_screen: {screen}")
        # Create a list of screen names from SHOW_SCREENS
        screen_names = list(self.SCREEN_NAMES.keys())
        self.add_note(f"Screen Names: {screen_names}")
        # Get the current index of the screen in screen_names
        current_index = screen_names.index(screen) if screen in screen_names else None
        self.add_note(f"Current Index: {current_index}")
        # If the current screen is not found or it is the last one, the next screen is the SuccessScreen
        if current_index is None or current_index == len(screen_names) - 1:
            self.next_screen = None
        else:
            # If the current screen is found and it is not the last one, the next screen is the next item in the list
            self.next_screen = screen_names[current_index + 1]


if __name__ == "__main__":
    BaseApp().run()
