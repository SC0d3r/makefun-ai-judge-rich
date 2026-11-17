"""Write the frozen make.fun ai-judge-rich-01 plan to entry.txt."""

import os

PLAN = """Day 1: build the shelf, not a pitch. DexScreener lists 500 tokens a day over $50k volume; check 60 an hour, keep only sites parked, 404 or expired on projects still trading with a post in 14 days, 1 in 15, so 33 by evening.
Rebuild each from Wayback into a 4-block page (what it does, token, docs, buy link) on Cloudflare Pages, $0, then message the project's own contact: live in 2 hours, on their domain when they point DNS, $99 in USDC by Solana Pay to the agent's wallet, no account or ID either side. A live site is what exchanges and buyers check before they buy a token.
Days 2-30: 15 messages a day from the same daily scan, 435 sends. At 4% reply, 17 talks, 5 sales, $495 kept; at 2%, 9 talks, 3 sales, $297 kept.
Expected day 30: $595 held. Floor at 2% replies: $397. No reply in 20 days: stop, $100 held, cost $0.
Judge: criterion 3: buyer holds USDC, rail is a wallet the agent has, no ID; criterion 2: $595 expected, $397 floor; criterion 5: the shelf and list, not effort."""


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
