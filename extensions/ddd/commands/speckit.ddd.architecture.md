---
description: "Design or update the product bounded-context architecture from the product description and existing requirements"
---

# Design Product Architecture

Produce or update a durable DDD architecture baseline for the product and save it as a long-lived artifact.

## User Input

```text
$ARGUMENTS
```

Treat `$ARGUMENTS` as the current product description, architectural emphasis, business direction, or extra context. You MUST consider it if provided.

## Goal

Create or update `specs/architecture.md` as the authoritative product architecture document, centered on bounded contexts and their relationships.

The resulting artifact should help the team maintain a coherent domain architecture across multiple features by identifying:

- Product mission and architectural scope
- Domain landscape and subdomains
- Bounded contexts and ownership boundaries
- Context relationships, upstream/downstream dependencies, and integration styles
- Ubiquitous language that must stay stable across feature work
- Shared architectural constraints that feature specs and plans must respect
- Known tensions, gaps, and triggers for future architecture updates

## Required Inputs

Before writing the architecture, inspect the current product context:

1. Read `specs/architecture.md` if it already exists so you preserve useful decisions
2. Inspect the `specs/` directory for existing feature requirements such as `specs/<feature>/spec.md`
3. Read any existing `plan.md`, `tasks.md`, or domain-model.md files under `specs/<feature>/` when they materially clarify domain boundaries
4. If a `.spec/` directory exists and contains requirement or architecture notes, include them as supplemental input
5. Read the constitution, README, or other durable product guidance when it affects context boundaries or ownership

If no prior requirements exist, derive the first architecture baseline directly from the product description in `$ARGUMENTS`.

## Architecture Rules

When deriving the architecture:

- Make bounded contexts the primary unit of design, not services, databases, or deployment units
- Use the product description and existing requirements as evidence; do not invent capabilities that are not implied
- Preserve prior architectural decisions unless the new evidence clearly invalidates them
- Distinguish stable product-level boundaries from feature-level implementation detail
- Call out context ownership, language boundaries, and consistency boundaries explicitly
- Treat external systems and organizations as neighboring contexts when they influence the model
- Surface tradeoffs, ambiguity, and migration pressure instead of hiding them

If the product is still early and information is incomplete, produce the best-available architecture baseline and clearly identify uncertainties.

## Output Format

Write `specs/architecture.md` in Markdown with these sections:

1. Title and architecture scope
2. Product summary
3. Architectural drivers
4. Domain landscape and subdomains
5. Bounded contexts
6. Context map
7. Ubiquitous language
8. Integration and coordination rules
9. Architecture constraints for feature work
10. Change log or evolution notes
11. Open questions and watchpoints

Use concise tables where they improve clarity.

For the `Context map` section, include a simple Mermaid diagram when it helps explain the main bounded-context relationships. Keep it conceptual and product-level.

For the `Architecture constraints for feature work` section, define the rules that future `spec.md`, `plan.md`, `tasks.md`, and `domain-model.md` artifacts should follow.

## Deliverable Quality

The generated architecture should be:

- Stable enough to guide multiple upcoming features
- Specific about bounded-context responsibilities and collaboration patterns
- Explicit about how existing requirements influenced the design
- Easy to revise as the domain understanding evolves
- Honest about architectural uncertainty and unresolved boundary decisions

After writing the file, provide the user a short summary of the key bounded-context decisions, the most important architecture constraints, and the top open questions.
