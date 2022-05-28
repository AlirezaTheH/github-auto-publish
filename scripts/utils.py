from typing import Union

import typer


def _normalize_value(value: Union[str, bool]) -> str:
    if isinstance(value, str):
        return value
    elif isinstance(value, bool):
        return 'true' if value else 'false'


def set_output(name: str, value: Union[str, bool]) -> None:
    """
    Sets GitHub action output.
    """
    typer.echo(f'::set-output name={name}::{_normalize_value(value)}')
