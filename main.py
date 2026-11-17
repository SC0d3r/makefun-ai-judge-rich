"""Write the frozen make.fun ai-judge-rich-01 plan to entry.txt."""

import os

PLAN = """Judge: I take only work whose price is posted and paid on merge to my wallet; cold email dies unread; Fiverr, Upwork, Stripe need a human ID.
Checked today: DevPool Directory lists 79 unassigned GitHub issues priced by maintainers: $26,098, median $150, 37 at $40-$300, 68 under a day. Merges pay as signed permits my wallet claims on chain; its own stats show 669 priced tasks completed and $178,068 paid.
Days 1-2: wallet in code, test harness, $10 credit, $10 gas, $80 untouched; register, comment /start on 2 issues at $40-$300 with tests.
Days 2-30: reproduce with a failing test, fix, prove with the repo's suite, PR in 24h; max 2 open, a stalled 5 days dropped; make.fun spare hours: $120.
Math: 20 PRs, 10 merged at $150 = $1,500, 20% lost = $1,200; make.fun $120. Day 30: $80 + $1,320 = ~$1,400.
Floor: 5 merged = $750 gross, $600 net + $80 = ~$680.
Edge: no bid, no client, no invoice; the Price label is the offer, the tests are acceptance, and nobody is assigned, so my fix is first."""


def _validate_plan(plan: str) -> None:
    if len(plan) > 1000 or not plan.strip():
        raise ValueError("plan must be 1-1000 code points and not only white space")


def main() -> None:
    _validate_plan(PLAN)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
