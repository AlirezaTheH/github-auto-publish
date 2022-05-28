# GitHub Auto Publish
GitHub action to automate publish a GitHub release if find an unpublished
version in `CHANGELOG.md`
([Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format).

## Usage
```yaml
name: Publish
on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  github-publish:
    runs-on: ubuntu-latest
    steps:
      - use: alirezatheh/github-auto-publish@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          files: ./dist/*.zip
```

The action assume:
- Python and pip are installed (e.g. by `actions/setup-python@v3`).

## Inputs
- `github-token`: GitHub token (required).
- `files`: Files to be uploaded as release assets (optional).

## Acknowledgements
This action is inspired by
[pypi-auto-publish](https://github.com/etils-actions/pypi-auto-publish)
