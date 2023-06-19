r"""Test server"""
from bitbake_language_server.server import get_document


class Test:
    r"""Test."""

    @staticmethod
    def test_get_document() -> None:
        r"""Test get document.

        :rtype: None
        """
        assert len(get_document().get("comment.line", "").splitlines())
