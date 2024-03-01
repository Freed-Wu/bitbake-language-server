# bitbake-language-server

[![readthedocs](https://shields.io/readthedocs/bitbake-language-server)](https://bitbake-language-server.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/bitbake-language-server/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/bitbake-language-server/main)
[![github/workflow](https://github.com/Freed-Wu/bitbake-language-server/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/bitbake-language-server/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/bitbake-language-server/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/bitbake-language-server)
[![DeepSource](https://deepsource.io/gh/Freed-Wu/bitbake-language-server.svg/?show_trend=true)](https://deepsource.io/gh/Freed-Wu/bitbake-language-server)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/bitbake-language-server/total)](https://github.com/Freed-Wu/bitbake-language-server/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/bitbake-language-server/latest/total)](https://github.com/Freed-Wu/bitbake-language-server/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server)
[![github/v](https://shields.io/github/v/release/Freed-Wu/bitbake-language-server)](https://github.com/Freed-Wu/bitbake-language-server)

[![pypi/status](https://shields.io/pypi/status/bitbake-language-server)](https://pypi.org/project/bitbake-language-server/#description)
[![pypi/v](https://shields.io/pypi/v/bitbake-language-server)](https://pypi.org/project/bitbake-language-server/#history)
[![pypi/downloads](https://shields.io/pypi/dd/bitbake-language-server)](https://pypi.org/project/bitbake-language-server/#files)
[![pypi/format](https://shields.io/pypi/format/bitbake-language-server)](https://pypi.org/project/bitbake-language-server/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/bitbake-language-server)](https://pypi.org/project/bitbake-language-server/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/bitbake-language-server)](https://pypi.org/project/bitbake-language-server/#files)

Language server for
[bitbake](https://docs.yoctoproject.org/bitbake/index.html).

## Features

- [x] [Diagnostic](https://microsoft.github.io/language-server-protocol/specifications/specification-current#diagnostic)
- [x] [Document Link](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_documentLink)
- [x] [Goto Definition](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_definition)
- [x] [Hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_hover)
- [x] [Completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_completion)

A video is [here](https://asciinema.org/a/628560).

### Goto Definition

![Goto Definition](https://github.com/Freed-Wu/bitbake-language-server/assets/32936898/5720403e-7bf4-436c-91aa-578482a7ba07)

### Diagnostic

![Diagnostic](https://github.com/Freed-Wu/bitbake-language-server/assets/32936898/965de2ad-f5eb-4fba-8d14-cdc69ff49b82)

### Hover

![Hover](https://github.com/Freed-Wu/bitbake-language-server/assets/32936898/843dda35-4378-4295-83ad-7d5552d37c4f)

### Document Link

![Document Link](https://github.com/Freed-Wu/bitbake-language-server/assets/32936898/a61a132f-18cf-42a7-8cef-0dd5d830bc34)

Read
[![readthedocs](https://shields.io/readthedocs/bitbake-language-server)](https://bitbake-language-server.readthedocs.io)
to know more.

## Related Projects

- [oelint-parser](https://github.com/priv-kweihmann/oelint-parser): the parser
  of this project
- [vim-bitbake](https://github.com/kergoth/vim-bitbake):
  syntax highlight for vim
- [vscode-bitbake](https://github.com/savoirfairelinux/vscode-bitbake/):
  A VS Code extension for bitbake which use tree-sitter as its parser
