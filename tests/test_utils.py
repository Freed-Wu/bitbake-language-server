r"""Test utils."""

import os

from bitbake_language_server.utils import render_document
from oelint_parser.cls_stash import Stash

stash = Stash()
test_file = os.path.join(os.path.dirname(__file__), "test.bb")
stash.AddFile(test_file)


class Test:
    r"""Test."""

    @staticmethod
    def test_render_document() -> None:
        assert (
            render_document(stash.GetItemsFor()[0])
            == f"""<file://{test_file}>:1:
```bitbake
inherit test
```"""
        )
