import argparse
import sys
from rich.console import Console
from rich.table import Table

from app import CookiecutterApp


def main():
    parser = argparse.ArgumentParser(prog="devblaze", add_help=False)
    parser.add_argument(
        "command",
        nargs="?",
        help="The command to execute",
    )
    try:
        args = parser.parse_args()
    except SystemExit:
        show_commands()
        sys.exit(1)
    except argparse.ArgumentError as exc:
        console = Console()
        console.print(f"[bold red]{exc.message}[/bold red]")
        sys.exit(1)
    else:
        if not args.command:
            show_commands()
            sys.exit(1)

    if args.command == "generate":
        # Call your generate function here
        CookiecutterApp().run()
    else:
        show_commands()


def show_commands():
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="dim", width=12)
    table.add_column("Description")

    table.add_row(
        "generate", "Generates a new Django project using the specified template"
    )

    console.print(table)


if __name__ == "__main__":
    main()
