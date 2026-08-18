import time
from rich.live import Live
from rich.console import Group, Console
from rich.spinner import Spinner
from rich.markdown import Markdown

def chunks_generator():
    yield "Hello"
    time.sleep(2)
    yield " World!"
    time.sleep(2)
    yield "\n\nDone."

def live_print():
    console = Console()
    full_completion = ""
    spinner = Spinner("dots", style="status.spinner", text="Thinking...")
    
    with Live(
        console=console,
        auto_refresh=True,
        refresh_per_second=10,
    ) as live:
        # Initial render
        live.update(Group(Markdown(full_completion), spinner))
        for chunk in chunks_generator():
            full_completion += chunk
            live.update(Group(Markdown(full_completion), spinner))
            
        live.update(Markdown(full_completion))

live_print()
