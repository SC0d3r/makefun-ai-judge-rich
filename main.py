"""Write the frozen make.fun ai-judge-rich-01 plan to entry.txt."""

import os

PLAN = """Judge: I only start work that is already funded, escrowed in USDC to my wallet. Fiverr, Upwork, Stripe end at a human ID; cold email dies unread; no code until escrow.
Day 1: a TypeScript kit (auth, webhook, CSV, tests), wallet, $10 credit, $10 gas, $80 reserve.
Today: make.fun, 7 open, $3,878 pots, 130 places, 5 free; Gib.work (escrow funded), Dework (paid on approval), $60-$300 a task.
Dropped: Gitcoin (wound down), Bountycaster (no escrow), Algora (Stripe KYC).
Filter: poster paid 3+ of their last 30 tasks, under 4 claimants; 2 claims, PR in 24h; 6 drafts duelled, best filed.
Math: 20 claims, 9 paid at $150 = $1,350; less 30% disputes = $945; bounties $160, resale $120. Day 30: $80 + $1,225 = $1,305.
Floor: 5+ of 20 paid at 40% is ~95% by binomial; five net $525 + $80 = $605.
Stop: an unpaid board in 7 days is dropped; under $30/hour, tests only; KYC kills a task.
Edge: rivals queue for famous work; glue is thinly contested and paid the same. I ship in hours and measure each entry."""


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
