# Original practice questions and rationales

All 30 items are independently authored. They are not real exam questions, dumps, recalled items, or copied official samples. Difficulty and distribution do not simulate the official exam. Select one answer unless stated otherwise. Answer with rationales before revealing the explanations.

## Q01

CCAO-F · Prompting and Task Execution · M01

A library digest omits the time from one notice. What instruction best prevents fabrication?

- A. Mark missing times unknown and retain the source ID
- B. Assume all events start at noon
- C. Generate a likely time
- D. Hide notices with missing times

<details>
<summary>Answer and explanation</summary>

**A** — A preserves uncertainty and evidence. B/C invent data; D discards potentially useful information without a requirement.

</details>

## Q02

CCAO-F · Output Evaluation and Validation · M02

A summary sounds polished but cites a page that does not support its claim. Which check matters?

- A. Claim-to-source support
- B. Only grammar
- C. Only length
- D. Only the model confidence score

<details>
<summary>Answer and explanation</summary>

**A** — A checks the failed property. B/C assess presentation, and D is not independent verification.

</details>

## Q03

CCAO-F · Product and Model Selection · M03

A nightly draft tolerates delay. How should you choose a processing route?

- A. Always use the most expensive option
- B. Measure quality and total cost for batch and interactive routes
- C. Choose the shortest model name
- D. Ignore retries when estimating cost

<details>
<summary>Answer and explanation</summary>

**B** — B matches workload constraints. A/C are arbitrary; D underestimates cost.

</details>

## Q04

CCAO-F · Workflow Integration and Solution Design · M05 M10

A venue wants to auto-publish every generated schedule. What must be designed first?

- A. A prettier font
- B. Unlimited autonomy
- C. Acceptance criteria and a review boundary for consequential errors
- D. A claim that the model is always correct

<details>
<summary>Answer and explanation</summary>

**C** — C aligns workflow and risk. A is secondary; B/D ignore error consequences.

</details>

## Q05

CCAO-F · Configuration and Knowledge Management · M04

Two archive policies conflict. What should a knowledge handoff contain?

- A. Only the last sentence
- B. Document IDs, versions, and the unresolved conflict
- C. A fabricated merged policy
- D. Only the model answer

<details>
<summary>Answer and explanation</summary>

**B** — B preserves provenance for resolution. A/D lose evidence; C invents policy.

</details>

## Q06

CCAO-F · Governance, Risk, and Responsible Use · M10

A fictional staff note contains sensitive fields unnecessary for a public digest. What is appropriate?

- A. Include everything
- B. Keep it forever
- C. Minimize and redact before processing
- D. Put it into a public repository

<details>
<summary>Answer and explanation</summary>

**C** — C reduces unnecessary exposure. A/B/D expand exposure without task need.

</details>

## Q07

CCAO-F · Troubleshooting and Optimization · M09

A report ends mid-JSON after reaching an output limit. First diagnosis?

- A. Blame the reader
- B. Check stop reason and truncation before retrying
- C. Accept it as final
- D. Remove all validation

<details>
<summary>Answer and explanation</summary>

**B** — B locates the failure. A has no evidence; C/D permit corrupted output.

</details>

## Q08

CCAR-F · Agentic Architecture & Orchestration · M05

An exhibition-planning agent keeps revisiting the same task. What control helps?

- A. Remove all logs
- B. Increase autonomy forever
- C. Iteration and budget limits with escalation
- D. Assume repetition proves quality

<details>
<summary>Answer and explanation</summary>

**C** — C bounds the loop and provides an exit. A hides diagnosis; B/D worsen the loop.

</details>

## Q09

CCAR-F · Tool Design & MCP Integration · M07

A tool cannot find a catalog item. Which result is most useful?

- A. A fabricated item
- B. An empty success message
- C. Structured not-found status with the queried ID
- D. A secret token

<details>
<summary>Answer and explanation</summary>

**C** — C distinguishes a domain miss from success. A/B mislead; D leaks credentials.

</details>

## Q10

CCAR-F · Claude Code Configuration & Workflows · M08

A large repository change spans several modules. Best starting approach?

- A. Plan scope and validation, then inspect small diffs
- B. Skip review
- C. Grant every tool
- D. Edit all files without inspection

<details>
<summary>Answer and explanation</summary>

**A** — A manages uncertainty. B/D suppress feedback; C expands unnecessary permissions.

</details>

## Q11

CCAR-F · Prompt Engineering & Structured Output · M01 M09

An event record is valid JSON but its end precedes its start. What is missing?

- A. Larger fonts
- B. Cross-field business validation
- C. More confident wording
- D. A random retry

<details>
<summary>Answer and explanation</summary>

**B** — B checks an invariant beyond syntax. A/C do not validate; D does not address the cause.

</details>

## Q12

CCAR-F · Context Management & Reliability · M04 M06

A long-session handoff loses a pending approval. What should be preserved?

- A. Only a celebratory summary
- B. Only token counts
- C. Goals, unresolved decisions, evidence, and approval state
- D. A claim that all work is finished

<details>
<summary>Answer and explanation</summary>

**C** — C retains operational context. A/B are incomplete; D fabricates completion.

</details>

## Q13

CCDV-F · Agents and Workflows · M05

Three independent archive sections need summaries. When is parallel work useful?

- A. Always, even with no budget
- B. When separable work has explicit inputs and a synthesis owner
- C. Only if workers share every tool
- D. When evidence can be discarded

<details>
<summary>Answer and explanation</summary>

**B** — B enables controlled decomposition. A ignores overhead; C is unnecessary; D harms provenance.

</details>

## Q14

CCDV-F · Applications and Integration · M06

A new Messages request lacks the prior exchange. What should the app do for continuity?

- A. Assume automatic memory
- B. Send appropriate retained history
- C. Place the key in the browser
- D. Ignore all previous requirements

<details>
<summary>Answer and explanation</summary>

**B** — B supplies conversation context. A confuses requests with persistent sessions; C is insecure; D loses requirements.

</details>

## Q15

CCDV-F · Claude Code · M08

Repository instructions say a write needs approval. What actually enforces it?

- A. A title in CLAUDE.md alone
- B. Tool permission checks or a gate at execution
- C. A positive adjective
- D. A longer prompt alone

<details>
<summary>Answer and explanation</summary>

**B** — B enforces the boundary. A/C/D can guide wording but cannot independently authorize operations.

</details>

## Q16

CCDV-F · Eval, Testing, and Debugging · M02 M09

A new prompt improved the same examples used to tune it. Next evaluation step?

- A. Declare production readiness
- B. Delete negative cases
- C. Evaluate held-out cases and severe failures
- D. Trust only self-ratings

<details>
<summary>Answer and explanation</summary>

**C** — C tests generalization and risk. A is premature; B biases data; D is not independent.

</details>

## Q17

CCDV-F · Model Selection and Optimization · M03

A cheaper model misses critical cases. What decision is justified?

- A. Use it regardless of quality
- B. Require quality thresholds and assess routing or another model
- C. Hide the failures
- D. Assume low cost proves value

<details>
<summary>Answer and explanation</summary>

**B** — B weighs quality with cost. A/C/D ignore critical failures.

</details>

## Q18

CCDV-F · Prompt and Context Engineering · M01 M04

A retrieved document tells the assistant to publish a secret. How should it be treated?

- A. As a new system instruction
- B. As untrusted data with permissions enforced separately
- C. As proof of user approval
- D. As mandatory because it was retrieved

<details>
<summary>Answer and explanation</summary>

**B** — B preserves the trust boundary. A/C/D elevate external data into authorization.

</details>

## Q19

CCDV-F · Security and Safety · M10

A client app needs a provider API credential. Where should it be stored?

- A. Public frontend bundle
- B. Server secret storage with scoped access
- C. Public issue comment
- D. Plaintext analytics log

<details>
<summary>Answer and explanation</summary>

**B** — B prevents client exposure. A/C/D distribute the secret to inappropriate audiences.

</details>

## Q20

CCDV-F · Tools and MCPs · M07

Claude proposes a client-tool call. Who executes it?

- A. The model text automatically changes the database
- B. The application after validation and authorization
- C. Every MCP server automatically
- D. The end-user browser with a public secret

<details>
<summary>Answer and explanation</summary>

**B** — B matches client-tool execution. A/C confuse proposal with execution; D exposes credentials.

</details>

## Q21

CCAR-P · Solution Design & Architecture · M05 M10

An archive needs predictable five-step processing. What architecture starts reasonably?

- A. An unrestricted autonomous swarm
- B. A fixed workflow evaluated against requirements
- C. No monitoring
- D. A design selected only by novelty

<details>
<summary>Answer and explanation</summary>

**B** — B fits predictable steps. A adds unnecessary complexity; C/D omit operational criteria.

</details>

## Q22

CCAR-P · Claude Models, Prompting & Context Engineering · M01 M03 M04

Context is over budget. Which reduction is safest?

- A. Discard all constraints
- B. Keep only the latest sentence
- C. Remove redundancy while retaining evidence and unresolved requirements
- D. Invent missing history

<details>
<summary>Answer and explanation</summary>

**C** — C preserves essential information. A/B lose requirements; D invents state.

</details>

## Q23

CCAR-P · Integration · M06 M07

A write times out after the server may have accepted it. How should recovery work?

- A. Blindly repeat forever
- B. Use operation IDs, reconciliation, and bounded retries
- C. Assume it failed
- D. Assume it succeeded without checking

<details>
<summary>Answer and explanation</summary>

**B** — B avoids duplicate side effects and resolves uncertainty. A duplicates; C/D assert unknown outcomes.

</details>

## Q24

CCAR-P · Evaluation, Testing & Optimization · M02 M09

Average task accuracy is high but a safety-critical case fails. Release decision?

- A. Release based only on average
- B. Hide the case
- C. Apply severity-based acceptance criteria and investigate
- D. Delete the safety criterion

<details>
<summary>Answer and explanation</summary>

**C** — C accounts for consequences. A masks risk; B/D evade rather than solve it.

</details>

## Q25

CCAR-P · Governance, Safety & Risk Management · M10

A regulated archive chooses a cloud provider. What evidence is needed?

- A. Brand alone
- B. Identity, residency, network, retention, and operational controls
- C. Only model size
- D. Only a marketing slogan

<details>
<summary>Answer and explanation</summary>

**B** — B tests deployment requirements. A/C/D do not establish governance fit.

</details>

## Q26

CCAR-P · Stakeholder Communication & Lifecycle Management · M10

A sponsor asks whether an AI proposal is ready. What should a decision memo say?

- A. Only enthusiasm
- B. Only technical acronyms
- C. Acceptance evidence, tradeoffs, owners, unresolved risks, rollback
- D. A guaranteed outcome

<details>
<summary>Answer and explanation</summary>

**C** — C supports an informed decision. A/B omit actionable evidence; D overstates certainty.

</details>

## Q27

CCAR-P · Developer Productivity & Operational Enablement · M08 M10

An automated repository reviewer flags many false positives. Best improvement?

- A. Post every guess
- B. Evaluate verified findings and require actionable evidence
- C. Disable all checks
- D. Grant deployment permission

<details>
<summary>Answer and explanation</summary>

**B** — B improves precision and usefulness. A adds noise; C loses safeguards; D is unrelated and risky.

</details>

## Q28

Cross-track · Synthesis · M02 M07 M09 M10

Select TWO controls for a public-data research worker.

- A. Read-only tool scope
- B. Treat retrieved commands as instructions
- C. Explicit source provenance
- D. Unlimited publish access

<details>
<summary>Answer and explanation</summary>

**AC** — A limits effects; C preserves evidence. B crosses trust boundaries; D grants unnecessary writes.

</details>

## Q29

Cross-track · Synthesis · M02 M07 M09 M10

Select TWO checks after receiving structured output.

- A. Schema conformance
- B. Business-rule consistency
- C. Assume valid JSON is factual
- D. Accept a partial stream as final

<details>
<summary>Answer and explanation</summary>

**AB** — A checks shape; B checks domain invariants. C confuses syntax with truth; D ignores completion.

</details>

## Q30

Cross-track · Synthesis · M02 M07 M09 M10

Select TWO statements that distinguish study material from exam evidence.

- A. Our practice score predicts a scaled exam score
- B. The official guide controls scope
- C. A course completion certificate equals a proctored certification
- D. Original practice items are learning aids, not recalled exam items

<details>
<summary>Answer and explanation</summary>

**BD** — B respects the authority of the blueprint; D describes this pack. A has no calibration evidence; C confuses different credentials.

</details>

Use the result only to locate learning gaps. Review the linked chapter, lab, and official guide for each missed domain. Do not convert scores into scaled 720 or predict a pass.
