r"""Utils
=========
"""

from oelint_parser.cls_item import Item
from pygls.uris import from_fs_path


def render_document(item: Item) -> str:
    r"""Render document.

    :param item:
    :type item: Item
    :rtype: str
    """
    return f"""<{from_fs_path(item.Origin)}>:{item.InFileLine}:
```bitbake
{item.Raw.strip()}
```"""
