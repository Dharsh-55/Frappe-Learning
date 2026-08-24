import click

@click.command("hello-app")
def hello_app():
    """Test custom Bench CLI command."""
    click.echo("Hello from Football Management!")
    
commands = [hello_app]