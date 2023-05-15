from textual.containers import HorizontalScroll
from textual.reactive import reactive
from textual.widgets import Input


class DefaultValue:
    def __init__(self, value: object):
        self.inner = value if isinstance(value, str) else ""


class ValidatedInput(Input):
    def validate_value(self, value: object):
        if isinstance(value, DefaultValue):
            return value.inner

        self.validate_user_input(value)
        return value

    def validate_user_input(self, value: object):
        pass


class ProjectNameInput(ValidatedInput):
    project_name = reactive(None)

    def validate_user_input(self, value: object):
        if not value:
            value = DefaultValue(self.project_name)
        return value


class LabeledInput(HorizontalScroll):
    DEFAULT_CSS = """
    LabeledInput {
        height: 3;
    }

    LabeledInput > Label {
        margin-top: 1;
        width: 1fr;
        text-align: right;
    }

    LabeledInput > Input {
        width: 30%;
    }
    """
