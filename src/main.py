import click

from modules.module1 import sayhello
from modules.module2 import saygoodbye

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def cli(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        print(sayhello(name = name))
        click.echo(f"Hello, {name}!")
        print(saygoodbye(name = name))

if __name__ == '__main__':
    cli()

