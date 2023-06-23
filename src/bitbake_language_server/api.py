r"""Api
=======
"""
import re
from urllib import request

URI = "https://raw.githubusercontent.com/openembedded/openembedded-core/master/meta/conf/documentation.conf"
PAT = re.compile(r'(?<!= )"(?!$)', re.M)


def init_document() -> dict[str, str]:
    r"""Init document.

    :rtype: dict[str, str]
    """
    with request.urlopen(URI) as f:  # nosec: B310
        text = f.read().decode().replace("[doc]", "")
    text = PAT.sub("'", text)
    _ = {}
    l = {}
    exec(text, _, l)  # nosec: B102

    return l
