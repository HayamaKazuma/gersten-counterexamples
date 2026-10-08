# VERIFY_LEDGER — whole-paper math verification

<!-- ONLY the paper_verify_math tool writes verdict rows here. The main agent READS this file to know per-unit status + hints + attempts, and gates deliver on it (deliver is blocked unless every row is `correct` or `overridden`). The whole-paper gate writes one `whole-paper` row. The paper-math verifier CLASSIFIES its findings: `must-fix` (an undergraduate could not fill the step) drive the verdict — any must-fix => status `wrong`; `ignorable` findings (an undergraduate could fill them unaided) are recorded in the `ignorable` field and NEVER block deliver — surface them to the operator, do not chase them. -->


## whole-paper
- label: whole-paper
- source_fact: 
- status: correct
- last_verdict: correct
- repair_hints: 
- ignorable: 
- attempts: 1
- last_checked_utc: 2026-10-07T16:47:01.283337+00:00
