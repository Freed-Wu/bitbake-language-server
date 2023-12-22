r"""Misc
========
"""
from tempfile import mkstemp
from typing import Any
from urllib import request

from oelint_parser.cls_stash import Stash, Variable

URI = "https://raw.githubusercontent.com/openembedded/openembedded-core/master/meta/conf/documentation.conf"


def get_schema() -> dict[str, Any]:
    r"""Get schema. Copied from
    `/usr/lib/python3.11/site-packages/bb/parse/parse_py/ConfHandler.py <https://github.com/openembedded/bitbake/blob/master/lib/bb/parse/parse_py/ConfHandler.py>`_.

    :rtype: dict[str, Any]
    """
    with request.urlopen(URI) as f:  # nosec: B310
        text = f.read()
    _, tmp = mkstemp(".conf")
    with open(tmp, "wb") as f:
        f.write(text)
    _stash = Stash(quiet=True)
    _stash.AddFile(tmp)
    _stash.Finalize()
    d = {}
    for item in _stash.GetItemsFor():
        if isinstance(item, Variable):
            d[item.VarName] = item.VarValueStripped
    return d
