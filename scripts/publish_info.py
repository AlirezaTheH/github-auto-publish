from typing import Optional, Tuple

import keepachangelog
import typer
from github import Github
from keepachangelog._versioning import initial_semantic_version, to_semantic
from packaging.version import Version
from utils import set_output


def _actual_version(changelog: dict) -> Tuple[Optional[str], dict]:
    versions = sorted(
        [
            (version, to_semantic(version))
            for version in changelog.keys()
            if version != 'unreleased'
        ],
        key=lambda version: Version(version[0]),
    )
    if versions:
        return versions[-1]

    return None, initial_semantic_version.copy()


def get_local_version() -> Version:
    """
    Gets the latest local version.
    """
    changelog = keepachangelog.to_dict('CHANGELOG.md', show_unreleased=True)
    current_version, current_semantic_version = _actual_version(changelog)

    if current_version is None:
        current_version = '0.0.0'

    return Version(current_version)


def get_github_version(token: str, repository_name: str) -> Version:
    """
    Gets the latest GitHub version.
    """
    github = Github(token)
    repo = github.get_repo(repository_name)
    releases = list(repo.get_releases())
    if releases:
        return Version(releases[0].tag_name)

    return Version('0.0.0')


def main(
    github_token: str,
    github_repository: str,
) -> None:
    """
    Main script function

    Outputs:
    -------
    version: str
        Version to be published

    should-release: bool
        Whether local_version > pypi_version ('true' or 'false')
    """
    local_version = get_local_version()
    github_version = get_github_version(github_token, github_repository)

    if local_version <= github_version:
        typer.secho(
            'Error: Current local version is behind or equal with GitHub '
            'version.',
            err=True,
            fg='red',
        )
        typer.secho(
            'Hint: Make new changes, edit `CHANGELOG.md` and other '
            'version files. Then bump version to a new version. '
            '(Maybe you want to use '
            'https://github.com/alirezatheh/auto-bump-versions).'
        )
        typer.Exit(code=1)

    set_output('version', f'{local_version}')
    set_output('should-publish', True)


if __name__ == '__main__':
    typer.run(main)
