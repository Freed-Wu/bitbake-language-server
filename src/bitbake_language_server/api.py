r"""Api
=======
"""
from urllib import request

from bs4 import BeautifulSoup, FeatureNotFound

URI = "https://docs.yoctoproject.org/bitbake/bitbake-user-manual/bitbake-user-manual-ref-variables.html"


def init_document() -> dict[str, str]:
    r"""Init document.

    :rtype: dict[str, str]
    """
    with request.urlopen(URI) as f:  # nosec: B310
        html = f.read()

    try:
        soup = BeautifulSoup(html, "lxml")
    except FeatureNotFound:
        soup = BeautifulSoup(html, "html.parser")

    items = dict(
        zip(
            [dt.span.text for dt in soup.findAll("dt")],
            [
                "\n".join([p.text.replace("\n", " ") for p in dd.findAll("p")])
                for dd in soup.findAll("dd")
            ],
        )
    )
    return items
