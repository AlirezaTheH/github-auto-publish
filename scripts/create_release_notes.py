import keepachangelog
import typer
from packaging.version import Version


def get_release_notes(version: Version) -> str:
    """
    Gets version release notes.
    """
    changelog = keepachangelog.to_raw_dict('CHANGELOG.md')
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
    with open('RELEASE_NOTES.md', 'w') as f:
        f.write(release_notes)


if __name__ == '__main__':
    typer.run(main)
