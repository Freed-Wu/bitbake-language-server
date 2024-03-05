r"""Tool
========

`<https://github.com/priv-kweihmann/oelint-adv/issues/524>`_
"""

# ruff: noqa: F403, F405, UP032
from oelint_adv.__main__ import *  # type: ignore


def run2(args: argparse.Namespace) -> List[Tuple[Tuple[str, int], str]]:  # type: ignore
    try:
        rules = load_rules(
            args, add_rules=args.addrules, add_dirs=args.customrules
        )
        _loaded_ids = []
        _rule_file = args.state.get_rulefile()

        def rule_applicable(rule):
            if isinstance(rule, Rule):
                res = not _rule_file or any(
                    x in _rule_file for x in rule.get_ids()
                )  # pragma: no cover
                res &= rule.ID not in args.state.get_suppressions()
            else:
                res = not _rule_file or rule in _rule_file
                res &= rule not in args.state.get_suppressions()
            return res

        rules = [x for x in rules if rule_applicable(x)]

        for r in rules:
            _loaded_ids += [x for x in r.get_ids() if rule_applicable(x)]
        issues = []
        groups = group_files(args.files)
        if not any(groups):
            return []
        for group in groups:
            issues += group_run(
                group,
                quiet=args.quiet,
                fix=args.fix,
                rules=rules,
                state=args.state,
            )

        return sorted(set(issues), key=lambda x: x[0])
    except Exception:  # pragma: no cover - that shouldn't be covered anyway
        import traceback

        print(
            "OOPS - That shouldn't happen - {files}".format(files=args.files)
        )
        traceback.print_exc()
    return []  # pragma: no cover - that shouldn't be covered anyway
