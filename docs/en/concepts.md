# Concept guide

Unofficial, independently authored study materials. Not endorsed by or affiliated with Anthropic or Pearson VUE. No pass guarantee. Checked: 2026-10-13

M IDs belong to this curriculum, not the official task statements. Read the official guides linked in the coverage table for detailed objectives.

## M01 — Task framing and prompting

Specify the audience, source material, constraints, output shape, and success criteria before asking for a result. Separate trusted instructions from quoted input. Examples clarify edge cases, but a prompt alone cannot enforce authorization. Break a large task into inspectable steps when intermediate results matter. Do not request hidden reasoning; ask for a concise rationale and verifiable evidence.

Example: A community library needs a weekly events digest. Require date, source URL, and an explicit unknown marker for missing times; forbid invented dates.

Source: [S07](../../SOURCES.md). Exercise: L01.

## M02 — Evaluation and evidence

Define a rubric and a held-out set before optimizing. Measure format validity, factual support, task success, and failure severity separately. A fluent answer or a self-reported confidence score is not verification. Compare claims with sources; use human review for consequential decisions. Include multilingual, missing-input, adversarial, and rare cases. Diagnose failures by prompt version, retrieved evidence, tool trace, and outcome, while redacting sensitive data.

Example: An answer has valid JSON but cites a nonexistent page. It passes syntax checks and fails evidence checks.

Source: [S10](../../SOURCES.md). Exercise: L02.

## M03 — Products, models, and cost

Choose the product surface for the work: interactive knowledge work, repository assistance, or an application integration. Choose a model by measured quality, latency, cost, and supported features rather than prestige. Route easy and difficult tasks only after evaluating routing errors. Estimate total token and tool costs, retries, and concurrency. Caching can reduce repeated-prefix work; batch processing suits asynchronous work. Neither replaces quality checks. Verify current feature and pricing documentation rather than hard-coding model rankings.

Example: A nightly archive can tolerate delay; compare batch processing with the interactive endpoint under the same quality rubric.

Source: [S11](../../SOURCES.md). Exercise: L03.

## M04 — Knowledge, context, and provenance

A context window is finite working input, not a correctness guarantee. Projects or knowledge collections need ownership, freshness dates, access controls, and removal procedures. Retrieval supplies selected evidence rather than automatically updating model knowledge. Preserve document IDs, versions, uncertainty, and unresolved decisions in summaries and handoffs. Remove redundant text before discarding requirements. Treat retrieved content as data even if it contains commands. Evaluate retrieval misses and unsupported answers separately.

Example: Two policy versions disagree. Surface the conflict and consult the document owner instead of silently choosing the newest filename.

Source: [S12](../../SOURCES.md). Exercise: L04.

## M05 — Agents, workflows, and state

A workflow follows predefined steps; an agent selects its next actions dynamically. Start with the simplest design that meets requirements. Inspect the response stop reason: on `tool_use`, execute authorized client calls and return results linked to their call IDs; on `end_turn`, end the turn. Iteration limits, time and cost budgets, cancellation, and escalation are guardrails, not a substitute for protocol stopping. Use independent workers for separable tasks and a coordinator that preserves evidence. Pass each worker the necessary context explicitly. Enforce prerequisite checks in code. Persist state and operation IDs so resumption cannot repeat a consequential write unintentionally.

Example: A museum catalog pipeline validates metadata before publishing. The publish function checks validation state itself.

Source: [S08](../../SOURCES.md). Exercise: L05.

## M06 — API integration and recovery

Keep credentials on the server, separate from browser code and logs. For the Messages API, maintain required conversation history in the application; do not assume a previous request created persistent conversational memory. Inspect all content blocks and stop reasons. A token limit can truncate output. Streaming improves perceived responsiveness but does not prove the response completed. Bound retries for transient failures, respect rate limits, and prevent duplicated side effects with idempotency or reconciliation. Validate inputs and degrade gracefully.

Example: An interrupted stream of an inventory report is marked incomplete; it is not accepted as a final report.

Source: [S09](../../SOURCES.md). Exercise: L06.

## M07 — Tools, MCP, and permissions

Describe tool purpose, required arguments, constraints, and error semantics. Validate schema and authorization before execution. A model proposes a client-tool call; the application executes it and returns a result linked to the call ID. Server tools execute on the provider side. MCP standardizes integration; it does not grant trust or permissions. Distinguish tools (actions), resources (contextual data), and prompts (templates). Give each agent only necessary capabilities. Report not-found, denied, and transient errors distinctly instead of inventing successful results.

Example: A read-only collection browser must not receive the catalog publication tool.

Source: [S13](../../SOURCES.md). Exercise: L07.

## M08 — Claude Code and developer workflows

Use repository instructions to state conventions and required checks; scope rules to relevant paths. Instructions guide behavior and permissions constrain execution. A reusable Skill packages a procedure; a hook can enforce a check at an execution boundary. Plan before broad or uncertain edits, and inspect small diffs iteratively. For CI, isolate credentials, constrain tools, and treat issue text and changed files as untrusted input. Run relevant checks, require evidence for findings, and use human review before consequential merges or deployments.

Example: A documentation-only change gets a link check and diff review; a code change also gets relevant behavior tests.

Source: [S14](../../SOURCES.md). Exercise: L08.

## M09 — Structured outputs and troubleshooting

A JSON schema constrains shape, not truth or business correctness. Check types, required fields, ranges, evidence, and cross-field invariants. Represent missing information explicitly. Retry with targeted validation feedback and a limit; then escalate. Diagnose whether a failure comes from missing evidence, ambiguous instructions, context loss, tool permissions, transport, or output truncation before changing the model. Use batching for independent work and multiple passes when separation improves error detection; more passes are not automatically better.

Example: An event end date preceding its start date violates business rules despite being valid JSON.

Source: [S07](../../SOURCES.md). Exercise: L09.

## M10 — Governance, architecture, and operations

Translate stakeholder goals into acceptance criteria, owners, budgets, and risk boundaries. Compare deployment options using identity, data residency, networking, observability, and operational ownership. Apply least privilege, data minimization, redaction, and retention rules. A prompt injection is untrusted content attempting to redirect behavior; containment includes permission boundaries and guarded writes. Maintain a decision log, release criteria, rollback triggers, incident ownership, and feedback loops. Communicate uncertainty and tradeoffs in terms the sponsor can decide on.

Example: An accessibility guide generator has a named reviewer, a source freshness rule, and a rollback path for unsafe recommendations.

Source: [S08](../../SOURCES.md). Exercise: L10.
