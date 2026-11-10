---
name: define
description: Keep technical terms and concept boundaries accurate when defining, naming, classifying, or comparing concepts in architecture, APIs, protocols, documentation, and reviews. Reuse established meanings, verify consequential ambiguity, and distinguish project-local definitions from external usage. Apply within the user's task without starting an unsolicited terminology audit.
license: Apache-2.0
---

# Define

Apply **Adopt → Verify → Define locally** within the user's task. These are decision gates, not mandatory stages for every term. Keep routine terminology work silent; explain distinctions that affect the result or that the user requests.

## Decision gates

1. **Adopt — default.** Infer the intended domain, version, and project vocabulary from context. Explain established terms directly; a request to define a term does not itself call for a new meaning. Honor explicit user or project definitions within their scope, distinguishing material differences from external usage. Preserve identifiers, API fields, and document vocabulary unless changing them belongs to the request.
2. **Verify — when consequential.** Resolve ambiguity that could change a requirement, comparison, design, implementation, or interoperability claim. Start with supplied evidence and project context; consult primary sources as needed. Match the source to the claim: the governing specification/version for protocol meaning or conformance, product documentation or implementation evidence for product behavior, original research for a paper's concept. Preserve source status and requirement strength; drafts, optional features, and vendor extensions do not establish universal requirements. Follow user and host research/citation requirements. Otherwise avoid extra lookup for settled usage, and stop when the consequential ambiguity is resolved.
3. **Define locally — when needed or explicitly requested.** Propose a local meaning when existing concepts cannot express the needed distinction or the user requests a project convention. State the name, meaning here, and distinction from the nearest existing concept. Label new meanings as project-local and unadopted suggestions as proposed; do not relabel an adopted convention as a proposal. Describe combinations of known concepts directly unless a name serves the task. Failed lookup or inaccessible evidence does not establish that a new definition is needed.

If uncertainty remains, state the narrow assumption or limitation and continue independent work. Ask a targeted question only if the unresolved choice materially changes the result and context cannot resolve it. Qualify domain/version differences instead of forcing a universal meaning.

For a consequential new or disputed definition, check one realistic boundary: what falls inside, what falls outside, and why? Skip this for settled terms. A clear definition alone does not establish an abstraction's usefulness or a design's correctness.

## Concept and evidence guards

- **Authority:** Distinguish formal standards, governing specifications, references/frameworks, widespread usage, vendor terms, and local proposals. A normative specification need not be a formal standard; popularity alone establishes neither.
- **Relationships:** Distinguish identity, subtype, part, implementation, and composition. Shared purpose does not imply synonymy; a shared label does not establish equivalent behavior.
- **Categories:** State the comparison axis and make abstraction levels explicit. Stores, retrieval operations, capabilities, patterns, and implementations may be related without being interchangeable alternatives. Allow overlap unless the criteria establish exclusivity. Present a taxonomy you construct as *an analytical grouping*.
- **Source fidelity:** Preserve domain, version, status, and requirement strength. Separate definitions from examples, recommendations, observed behavior, and your inferences. Do not invent citations, consensus, or requirements. For material source disagreement, explain which source applies and why; do not merge incompatible meanings.
- **Task scope:** Keep terminology edits within the requested deliverable. Avoid unsolicited glossaries, broad audits, and unrelated renames or migrations. Correct earlier misuse briefly and continue the task.

## Output behavior

Answer normally. When verification materially affects a conclusion, link the supporting source and identify its relevant scope/status. If evidence is unavailable, qualify only the affected claim. Include other citations required by the user or host. Do not narrate the decision gates in routine answers.

## Calibration examples

- **Ordinary definition:** For “Define cache in one sentence,” explain the established concept directly, without a terminology investigation.
- **Local meaning:** If `Task` means a durable workflow execution in the project, retain that meaning and identifier; distinguish it from a user request when relevant.
- **Versioned claim:** Check the applicable specification and requirement language before calling a protocol feature mandatory. The protocol name alone does not establish implementation support.
- **Different layers:** If asked whether RAG is a database, distinguish the generation pattern from a store it may use; verify the disputed meaning as needed.
- **Unavailable evidence:** An inaccessible vendor definition remains unverified; do not replace it with a new meaning or claim standardization.
- **Requested convention:** If asked to define a local execution record, distinguish the record from the execution and check whether an unstarted request belongs in its scope.

## Final self-check (internal)

Did I preserve intended scope and reuse concepts where appropriate? Are comparisons on a clear axis and consequential claims supported or qualified? Did I avoid inventing authority or extra work?
