r"""Misc
========
"""
from typing import Any
from urllib import request

import bb
from bb.data_smart import DataSmart
from bb.parse import ast
from bb.parse.parse_py.ConfHandler import feeder

URI = "https://raw.githubusercontent.com/openembedded/openembedded-core/master/meta/conf/documentation.conf"


def get_schema() -> dict[str, Any]:
    r"""Get schema. Copied from
    `/usr/lib/python3.11/site-packages/bb/parse/parse_py/ConfHandler.py <https://github.com/openembedded/bitbake/blob/master/lib/bb/parse/parse_py/ConfHandler.py>`_.

    :rtype: dict[str, str]
    """
    data = DataSmart()
    fn = "meta/conf/documentation.conf"
    abs_fn = URI
    baseconfig = False
    with request.urlopen(URI) as f:  # nosec: B310
        statements = ast.StatementGroup()
        lineno = 0
        while True:
            lineno = lineno + 1
            s = f.readline().decode()
            if not s:
                break
            origlineno = lineno
            origline = s
            w = s.strip()
            # skip empty lines
            if not w:
                continue
            s = s.rstrip()
            while s[-1] == "\\":
                line = f.readline().decode()
                origline += line
                s2 = line.rstrip()
                lineno = lineno + 1
                if (not s2 or s2 and s2[0] != "#") and s[0] == "#":
                    bb.fatal(
                        "There is a confusing multiline, partially commented expression starting on line %s of file %s:\n%s\nPlease clarify whether this is all a comment or should be parsed."
                        % (origlineno, fn, origline)
                    )

                s = s[:-1] + s2
            # skip comments
            if s[0] == "#":
                continue
            feeder(lineno, s, abs_fn, statements, baseconfig=baseconfig)

    # DONE WITH PARSING... time to evaluate
    statements.eval(data)
    items = {k: v["doc"] for k, v in data.dict.items() if v.get("doc")}
    return items
