import click
from src.config.command import config


@click.Group()
def app() -> None:
    pass


app.add_command(config)
