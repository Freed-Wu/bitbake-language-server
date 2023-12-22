r"""Server
==========
"""
import os
import re
from typing import Any

from lsprotocol.types import (
    INITIALIZE,
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    Hover,
    InitializeParams,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from oelint_parser.cls_item import Variable
from oelint_parser.cls_stash import Stash
from pygls.server import LanguageServer


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
        self.stash = Stash(quiet=True)

        @self.feature(INITIALIZE)
        async def initialize(params: InitializeParams) -> None:
            if params.root_path:
                path = os.path.join(params.root_path, "conf/bitbake.conf")
                if os.path.exists(path):
                    self.stash.AddFile(path)

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
            items = self.stash.GetItemsFor(
                attribute=Variable.ATTR_VAR, attributeValue=word
            )
            value = ""
            doc = ""
            flags = {}
            if items == []:
                return None
            for item in items:
                if item.Flag == "":
                    value = item.VarValueStripped
                elif item.Flag == "doc":
                    doc = item.VarValueStripped
                else:
                    flags[item.Flag] = item.VarValueStripped
            content = ""
            for flag, text in flags.items():
                content += f"{flag}: {text}\n"
            content = f"""
{value}
{content}---
{doc}"""
            return Hover(MarkupContent(MarkupKind.Markdown, content), _range)

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
                    item.VarName,
                    kind=CompletionItemKind.Variable,
                    documentation=item.VarValueStripped,
                    insert_text=item.VarName,
                )
                for item in self.stash.GetItemsFor(classifier="Variable")
                if item.VarName.startswith(word)
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
