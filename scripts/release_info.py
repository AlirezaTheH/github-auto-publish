from pathlib import Path

import keepachangelog
import typer
from packaging.version import Version
from utils import set_output


def get_release_notes(version: Version) -> str:
    """
    Gets version release notes.
    """
    changelog = keepachangelog.to_raw_dict(
        str(Path(__file__).parent.parent / 'CHANGELOG.md')
    )
    return changelog[str(version)]['raw'].strip()


def main(version: str) -> None:
    """
    Main script function

    Outputs
    -------
    release-notes: str
        Version release notes
    """
    release_notes = get_release_notes(Version(version))
    set_output('release-notes', release_notes)


if __name__ == '__main__':
    typer.run(main)
