---
description: "Generate a DDD domain model from the current feature specification"
---

# Generate DDD Domain Model

Produce a domain-driven design domain model for the active feature and save it as a durable artifact.

## User Input

```text
$ARGUMENTS
```

Treat `$ARGUMENTS` as optional modeling scope, emphasis, or extra business context. You MUST consider it if provided.

## Goal

Create or update `specs/<feature>/domain-model.md` for the active feature using the current specification as the source of truth.

The resulting artifact should help a team move from feature requirements toward a shared domain model by identifying:

- Business capabilities and subdomains
- Bounded contexts and context relationships
- Ubiquitous language
- Aggregates, entities, value objects, and domain services
- Commands, events, policies, and invariants
- Open modeling questions and ambiguity that still need validation

## Required Inputs

Before writing the model, inspect the active feature context:

1. Find the active feature directory under `specs/`
2. Read `spec.md`
3. Read `plan.md` and `tasks.md` if they already exist
4. Read the project constitution or any architecture notes if they materially affect domain boundaries

If no active feature can be identified, ask the user which feature should be modeled.

## Modeling Rules

When deriving the model:

- Prioritize business concepts over implementation classes or database tables
- Use domain language from the specification instead of inventing framework-centric terminology
- Separate what is known from what is assumed
- Call out bounded contexts only when the workflow, language, ownership, or consistency boundary justifies it
- Keep aggregates small and centered on transactional consistency boundaries
- Treat external systems as neighboring contexts, not as part of the core domain
- Do not fabricate fields, APIs, or schemas that are not implied by the requirements

If the spec is still too vague for a confident model, produce the best-available draft and clearly mark unresolved questions.

## Output Format

Write `specs/<feature>/domain-model.md` in Markdown with these sections:

1. Title and modeling scope
2. Domain summary
3. Subdomains
4. Bounded contexts
5. Context map
6. Ubiquitous language
7. Aggregates
8. Entities and value objects
9. Domain services
10. Commands, events, and policies
11. Business invariants
12. External systems and integrations
13. Open questions and assumptions

Use concise tables where they improve clarity.

For the `Context map` section, include a simple Mermaid diagram when it adds value. Keep it conceptual, not implementation-heavy.

## Deliverable Quality

The generated model should be:

- Specific enough to guide implementation planning
- High-level enough to remain stable as code evolves
- Explicit about consistency boundaries and ownership
- Honest about uncertainty and missing domain knowledge

After writing the file, provide the user a short summary of the major modeling decisions and the most important open questions.
