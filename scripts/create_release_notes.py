import typer
from packaging.version import Version


def get_release_notes(version: Version) -> str:
    """
    Gets version release notes.
    """
    version_found = False
    result = ''
    with open('CHANGELOG.md') as f:
        for line in f:
            if line.startswith('## '):
                if result:
                    break

                release_line = line[3:].lower().strip()
                current_version, release_date = (
                    release_line.split(maxsplit=1)
                    if ' ' in release_line
                    else (release_line, None)
                )
                if release_date and current_version[1:-1] == str(version):
                    version_found = True

            elif version_found:
                if line.startswith('  '):
                    result = result.rstrip()
                    line = line[1:]
                result += line

    return f'{result.strip()}\n'


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
