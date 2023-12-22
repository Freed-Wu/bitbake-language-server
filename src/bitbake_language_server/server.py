r"""Server
==========
"""
import os
import re
from typing import Any
from urllib.parse import unquote, urlparse

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    Diagnostic,
    DiagnosticSeverity,
    DidChangeTextDocumentParams,
    Hover,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from pygls.server import LanguageServer

from .diagnostics import diagnostic
from .utils import get_schema


class BitbakeLanguageServer(LanguageServer):
    r"""Bitbake language server."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :param kwargs:
        :type kwargs: Any
        :rtype: None
        """
        super().__init__(*args, **kwargs)

        @self.feature(TEXT_DOCUMENT_DID_OPEN)
        @self.feature(TEXT_DOCUMENT_DID_CHANGE)
        def did_change(params: DidChangeTextDocumentParams) -> None:
            r"""Did change.

            :param params:
            :type params: DidChangeTextDocumentParams
            :rtype: None
            """
            doc = self.workspace.get_document(params.text_document.uri)
            diagnostics = [
                Diagnostic(
                    Range(
                        Position(*node.start_point), Position(*node.end_point)
                    ),
                    message,
                    getattr(DiagnosticSeverity, severity),
                )
                for node, message, severity in diagnostic(
                    os.path.dirname(
                        unquote(urlparse(params.text_document.uri).path)
                    ),
                )
            ]
            self.publish_diagnostics(doc.uri, diagnostics)

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            word, _range = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            doc = get_schema().get(word)
            if not doc:
                return None
            return Hover(
                MarkupContent(MarkupKind.PlainText, doc),
                _range,
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            word, _ = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            items = [
                CompletionItem(
                    x,
                    kind=CompletionItemKind.Variable,
                    documentation=doc,
                    insert_text=x,
                )
                for x, doc in get_schema().items()
                if x.startswith(word)
            ]
            return CompletionList(False, items)

    def _cursor_line(self, uri: str, position: Position) -> str:
        r"""Cursor line.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :rtype: str
        """
        document = self.workspace.get_document(uri)
        return document.source.splitlines()[position.line]

    def _cursor_word(
        self,
        uri: str,
        position: Position,
        include_all: bool = True,
        regex: str = r"\w+",
    ) -> tuple[str, Range]:
        """Cursor word.

        :param self:
        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :param include_all:
        :type include_all: bool
        :param regex:
        :type regex: str
        :rtype: tuple[str, Range]
        """
        line = self._cursor_line(uri, position)
        for m in re.finditer(regex, line):
            if m.start() <= position.character <= m.end():
                end = m.end() if include_all else position.character
                return (
                    line[m.start() : end],
                    Range(
                        Position(position.line, m.start()),
                        Position(position.line, end),
                    ),
                )
        return (
            "",
            Range(Position(position.line, 0), Position(position.line, 0)),
        )
