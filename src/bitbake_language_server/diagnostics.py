r"""Diagnostics
===============
"""
import os
from typing import Callable

from tree_sitter import Node, Tree

from ._tree_sitter import get_parser


def traverse_tree(
    node: Node,
    func: Callable[[Node], bool],
    condition: Callable[[Node], bool] | None = None,
    nodes: list[Node] | None = None,
) -> list[Node]:
    r"""Traverse tree.

    :param node:
    :type node: Node
    :param func:
    :type func: Callable[[Node], bool]
    :param condition:
    :type condition: Callable[[Node], bool] | None
    :param nodes:
    :type nodes: list[Node] | None
    :rtype: list[Node]
    """
    if nodes is None:
        nodes = []
    if condition is None:
        condition = lambda _: True
    for n in node.children:
        if func(n):
            nodes.append(n)
        if condition(n):
            traverse_tree(n, func, condition, nodes)
    return nodes


def get_missing_nodes(tree: Tree) -> list[Node]:
    r"""Get missing nodes.

    :param tree:
    :type tree: Tree
    :rtype: list[Node]
    """
    return traverse_tree(tree.root_node, lambda n: n.is_missing)


def get_error_nodes(tree: Tree) -> list[Node]:
    r"""Get error nodes.

    :param tree:
    :type tree: Tree
    :rtype: list[Node]
    """
    return traverse_tree(tree.root_node, lambda n: n.has_error)


def diagnostic(source: str) -> list[tuple[Node, str, str]]:
    r"""Diagnostic.

    :param source:
    :type source: str
    :rtype: list[tuple[Node, str, str]]
    """
    parser = get_parser()
    with open(source) as f:
        text = f.read()
    tree = parser.parse(text.encode())
    results = []
    results += [(node, "missing", "Error") for node in get_missing_nodes(tree)]
    results += [(node, "error", "Error") for node in get_error_nodes(tree)]
    return results
