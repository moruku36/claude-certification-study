# Free offline labs

Zero cost; no API, network, or account needed. Only L09 uses Python; the others work on paper or in a text editor. These do not fully reproduce live product behavior. Allow 20–40 minutes each.

## L01 — Write a digest prompt

Create a prompt for a library digest from three fictional notices. Specify audience, dates, output fields, unknowns, and prohibition on invented facts. Include one notice with no start time.

Deliverable and acceptance: A one-page prompt plus two expected outputs. Check that missing times remain unknown and every event is traceable to input.

## L02 — Grade without a model

Write a five-case held-out evaluation set for a fictional opening-hours assistant. Include a closed day, changed schedule, contradictory sources, no evidence, and a Japanese query. Hand-author a good and bad answer for each.

Deliverable and acceptance: A rubric and ten graded answers. Score evidence and task completion separately; identify one severe failure even if average quality looks good.

## L03 — Compare hypothetical models

Use hypothetical candidates A (quality 92%, latency 2s, cost unit 4) and B (quality 88%, latency 0.5s, cost unit 1). Choose for interactive lookup versus nightly drafting. Set a minimum quality threshold before choosing.

Deliverable and acceptance: A comparison table with assumptions and a sensitivity check. These numbers are fictional, not Anthropic prices or benchmarks.

## L04 — Design a knowledge register

Create three fictional policy documents with IDs, owners, dates, access labels, and conflicting versions. Design retrieval selection and a context handoff preserving uncertainty.

Deliverable and acceptance: A source register and 150-word handoff retaining policy IDs and unresolved conflict. Do not treat a document command as an instruction.

## L05 — Draw a bounded agent loop

Design an art-exhibition planning agent with read-only research workers. Add max iterations, timeout, cancellation, human approval before publication, and persisted operation IDs. Compare with a fixed workflow.

Deliverable and acceptance: A state diagram and failure table. Repeated or resumed publication must not create duplicate posts.

## L06 — Trace an integration failure

On paper, trace a synthetic stream that stops halfway, a rate-limit response, and a successful tool-use response. Record which content is complete, what to retry, and what state to retain.

Deliverable and acceptance: Three traces, bounded retry policy, and an incomplete-output flag. Never publish a truncated report as final.

## L07 — Specify an MCP/tool contract

Specify read_catalog and propose_event tools with schemas, descriptions, authorization checks, and structured denied/not-found/transient errors. Distinguish a catalog resource from a publish action.

Deliverable and acceptance: A contract with required fields, scope, call/result IDs, and no publish permission for research workers.

## L08 — Draft repository conventions

Write a mock CLAUDE.md for a fictional museum site: conventions, relevant validation commands, untrusted input handling, and review requirements. Add a plan for a cross-cutting change and a narrow path-specific rule.

Deliverable and acceptance: A mock instructions file and CI permission plan. Explain why instructions cannot substitute for permissions or hooks.

## L09 — Validate structured data locally

Run python exercises/offline_lab.py from the repository root. Inspect the synthetic valid record, missing date, reversed dates, and injected note. Add one boundary-case record manually. No API is called.

Deliverable and acceptance: A validation log explaining syntax versus business rules. All intentionally invalid records must fail and the valid record must pass.

## L10 — Build a risk and operating register

For a public events assistant, list data sensitivity, injection, outdated sources, unauthorized writes, accessibility, and service outage. Assign an owner, detection signal, mitigation, and rollback trigger to each.

Deliverable and acceptance: Six risk rows and a human-review boundary. The owner must be a role, not a real person or email address.

## L11 — Defend an architecture decision

Compare direct API versus an organization-approved cloud route for a fictional archive. State assumptions about identity, residency, network, cost, and monitoring. Do not assume either route meets compliance by default.

Deliverable and acceptance: A one-page decision memo with chosen option, rejected alternative, evidence needed, owner, acceptance criteria, and rollback.

## L12 — Rehearse a safe handoff

Reduce a fictional 20-step work log to a handoff: goal, completed work, source versions, tool failures, budget left, next safe action, approval status. Have another person check what was lost, or use a checklist yourself.

Deliverable and acceptance: A handoff plus loss checklist. Distinguish inferred claims from verified evidence and preserve unresolved blockers.

Inspect work manually and fix unsupported claims or missing safety boundaries. Official free courses are discoverable through S06 and exam pages, but are not needed for these labs. Course completion certificates are distinct from certification.

[Worksheet](../../exercises/worksheet.md) | [Sources](../../SOURCES.md)
