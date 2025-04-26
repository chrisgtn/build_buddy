from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
import typer
import subprocess
import time
import glob
import os

""" 
    BuildBuddy: A CLI tool for building and managing projects with make and scons.
"""


app = typer.Typer()
console = Console()


@app.command()
def build(
    system: str = typer.Option("make", help="Build system: make or scons"),
    profile: str = typer.Option("release", help="Build profile: release or debug")
):
    """Build the project using make or scons."""
    start = time.time()
    
    try:
        if system == "make":
            subprocess.run(["make", f"BUILD={profile}"], check=True)
        elif system == "scons":
            subprocess.run(["scons", f"BUILD={profile}"], check=True)
        else:
            print("[bold red]Invalid build system. Use 'make' or 'scons'.[/bold red]")
            raise typer.Exit(code=1)
        
        elapsed = time.time() - start
        console.print(
            Panel.fit(
                f" [bold green]Build ({profile}) completed[/bold green] using [cyan]{system}[/cyan] in [yellow]{elapsed:.2f}[/yellow] seconds!",
                title="BuildBuddy"
            )
        )
    except subprocess.CalledProcessError:
        console.print(
            Panel.fit(
                f" [bold red]Build failed[/bold red] using [cyan]{system}[/cyan]",
                title="BuildBuddy"
            )
        )

@app.command()
def clean():
    """Clean build artifacts."""
    subprocess.run(["make", "clean"], check=True)
    print("[bold green] Clean completed![/bold green]")

# Prints a summary table about the project setup.
@app.command()
def visualize():
    """Visualize build settings and environment."""
    table = Table(title="BuildBuddy Project Summary")

    table.add_column("Setting", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    # Count source files
    c_files = glob.glob("src/*.c")
    num_c_files = len(c_files)

    # Get executable size if it exists
    exe_path = "build/main"
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path) / 1024
        size_str = f"{size:.2f} KB"
    else:
        size_str = "N/A"

    table.add_row("Project", "BuildBuddy Demo")
    table.add_row("Languages", "C, Python")
    table.add_row("Source Files", str(num_c_files))
    table.add_row("Build Systems", "Make, SCons")
    table.add_row("Outputs", "build/main")
    table.add_row("Executable Size", size_str)
    table.add_row("Profiles", "Debug / Release")
    table.add_row("Optimization", "-O2 / Debug Info")

    console.print(table)

@app.command()
def test(
    system: str = typer.Option("make", help="Build system: make or scons"),
    profile: str = typer.Option("debug", help="Build profile: release or debug")
):
    """Build, run, and test the project automatically with predefined inputs."""
    console.rule("[bold green]Starting Test Suite")

    try:
        # Build step
        console.print("[cyan]Building the project...[/cyan]")
        build(system=system, profile=profile)

        # Define test cases (input sequences)
        test_cases = [
            ("2\n1\n", "Test 1: 2 beeps, 1 second delay"),
            ("3\n0\n", "Test 2: 3 beeps, 0 second delay"),
            ("5\n2\n", "Test 3: 5 beeps, 2 second delay")
        ]

        # Run all test cases
        for input_data, description in test_cases:
            console.rule(f"[bold blue]{description}")
            console.print(f"[yellow]Feeding input:[/yellow] {repr(input_data)}")

            result = subprocess.run(
                ["./build/main"],
                input=input_data,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                console.print(Panel.fit(
                    f" [bold green]Executable ran successfully![/bold green]\n\nOutput:\n{result.stdout.strip()}",
                    title="Test Passed",
                    subtitle="BuildBuddy"
                ))
            else:
                console.print(Panel.fit(
                    f" [bold red]Executable failed with return code {result.returncode}[/bold red]\n\nErrors:\n{result.stderr.strip()}",
                    title="Test Failed",
                    subtitle="BuildBuddy"
                ))

    except subprocess.CalledProcessError:
        console.print(
            Panel.fit(
                f" [bold red]Test failed during build or execution.[/bold red]",
                title="BuildBuddy Test",
                subtitle="DevEx Tool"
            )
        )
    finally:
        # Clean up after testing
        console.print("[cyan]Cleaning up build artifacts...[/cyan]")
        clean()
        console.rule("[bold green]Test Suite Completed")


if __name__ == "__main__":
    app()
