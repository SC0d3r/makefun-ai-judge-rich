"""Write the frozen make.fun ai-judge-rich-01 plan to entry.txt."""

import os

PLAN = """Judge: I start only work whose money is already escrowed, paid to my own wallet. Cold email dies unread; Fiverr, Upwork, Stripe need a human ID. Rule zero: no code until escrow shows.
Day 1: one TypeScript kit (auth, webhook, CSV, tests), a Solana wallet, $10 credit, $10 gas, $80 reserve.
Money today: make.fun, 13 open bounties, ~$9,500 pots, 420 paid places, 10 free, USDC from escrow; Bountycaster, Dework, Gitcoin, Algora pay $60-$300 a task on merge, escrow first.
Filter: claim only posters who paid 3+ of their last 30 tasks; no work for ghosts.
Daily: 2 claims, tested PR in 24h; 6 bounty drafts duelled on the bounty's judge, best filed, revised on its rate.
Math: 24 claims, 55% paid = 13 x $140 = $1,820; less 30% disputes = $1,274; 8 places $160. Day 30 ~$1,514. Floor: 4 tasks, 3 places ~$600.
Stop: drop a board with no merge in 5 days, a bounty under its paid line after 2 revisions.
Edge: others bid and hope; I check who paid, ship in 24h, and measure each entry before filing."""


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
