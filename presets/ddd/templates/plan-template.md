# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. In this preset, planning is organized around domain boundaries, business rules, and integration seams before implementation details.

**Architecture Constraint Source**: `specs/architecture.md` (when present, this plan MUST respect it and document any required updates)

## Summary

[Summarize the feature in domain terms: the business capability, primary bounded context, and core architectural approach]

## Architecture Alignment

- **Architecture baseline**: [`specs/architecture.md` or "none yet"]
- **Primary bounded context confirmed**: [Context that owns this change]
- **Context map impact**: [How this feature fits the existing product architecture]
- **Architecture update required**: [None, or describe the required change to `specs/architecture.md`]

## Domain Framing

### Subdomain

- **Classification**: [Core / Supporting / Generic]
- **Why this classification fits**: [Explain briefly]

### Bounded Context Strategy

- **Primary context**: [Where the change is owned]
- **Contexts touched**: [Other contexts that interact with this change]
- **Relationship pattern**: [Customer/Supplier, Conformist, ACL, Published Language, etc. if relevant]
- **Boundary protection**: [How the implementation avoids leaking models across contexts]
- **Architecture constraints applied**: [Specific rules inherited from `specs/architecture.md`]

### Ubiquitous Language Commitments

- **Terms to preserve in code and docs**: [List the canonical domain terms]
- **Terms to avoid**: [Ambiguous or overloaded language to avoid]

## Technical Context

**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]  
**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]  
**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]  
**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]  
**Project Type**: [e.g., library/cli/web-service/mobile-app/compiler/desktop-app or NEEDS CLARIFICATION]  
**Performance Goals**: [domain-specific goals or NEEDS CLARIFICATION]  
**Constraints**: [latency, memory, regulatory, auditability, offline, or consistency constraints]  
**Scale/Scope**: [bounded volume, tenants, users, transactions, or datasets]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Gates determined based on constitution file]

## Domain Model Realization

### Aggregates

- **[Aggregate Name]**
  Responsibility: [What transactional consistency boundary it owns]
  Invariants: [Rules protected within this aggregate]
  State Changes: [Important transitions or commands]

### Entities

- **[Entity Name]**: [Role, identity, and lifecycle notes]

### Value Objects

- **[Value Object Name]**: [Meaning, validation rules, and reuse]

### Domain Services

- **[Service Name]**: [Why this behavior should not live on a single aggregate/entity]

### Domain Events

- **[Event Name]**: [When it occurs and who cares]

### Policies / Sagas / Process Managers

- **[Policy Name]**: [Cross-step orchestration or reaction logic, if needed]

## Data & Consistency Strategy

- **Source of truth**: [Which model or store owns each critical concept]
- **Consistency model**: [Strong, eventual, compensating workflow, etc.]
- **Concurrency concerns**: [Race conditions, idempotency, ordering, duplication]
- **Auditability**: [Important decisions or transitions that must be traceable]

## Integration & Context Map

| Context / System | Interaction Type | Contract / Data Exchanged | Failure Handling |
|------------------|------------------|---------------------------|------------------|
| [Context A] | [sync/async/manual] | [command, event, query, file] | [fallback or policy] |
| [Context B] | [sync/async/manual] | [command, event, query, file] | [fallback or policy] |

## Project Structure

### Documentation (this feature)

```text
specs/
├── architecture.md       # Product bounded-context architecture baseline
└── [###-feature]/
    ├── plan.md           # This file (/speckit.plan command output)
    ├── research.md       # Phase 0 output (/speckit.plan command)
    ├── domain-model.md   # Optional output from /speckit.ddd.modeling
    ├── data-model.md     # Phase 1 output (/speckit.plan command)
    ├── quickstart.md     # Phase 1 output (/speckit.plan command)
    ├── contracts/        # Phase 1 output (/speckit.plan command)
    └── tasks.md          # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

Document the concrete structure that best preserves bounded contexts and keeps domain logic isolated from transport, persistence, and UI concerns.

```text
src/
├── domain/
│   ├── [bounded-context]/
│   │   ├── aggregates/
│   │   ├── entities/
│   │   ├── value_objects/
│   │   ├── services/
│   │   └── events/
├── application/
│   ├── commands/
│   ├── queries/
│   └── policies/
├── infrastructure/
│   ├── persistence/
│   ├── messaging/
│   └── integrations/
└── interfaces/
    ├── api/
    ├── cli/
    └── jobs/

tests/
├── contract/
├── integration/
├── domain/
└── unit/
```

**Structure Decision**: [Document the actual directory choice and how it reinforces the domain boundaries above]

**Architecture Traceability**: [Explain how the chosen structure preserves the bounded contexts defined in `specs/architecture.md`]

## Delivery Strategy

### Vertical Slices

- **Slice 1**: [First end-to-end business capability]
- **Slice 2**: [Next independently valuable capability]
- **Slice 3**: [Follow-up capability or integration refinement]

### Testing Strategy

- **Domain tests**: [How invariants, decisions, and aggregate behavior are verified]
- **Contract tests**: [How boundaries with external systems or contexts are verified]
- **Integration tests**: [How application flow and persistence are verified]
- **End-to-end checks**: [How critical business journeys are proven]

## Risks & Open Questions

- **Risk**: [Boundary, consistency, or integration risk]
  **Mitigation**: [How to reduce it]

- **Open Question**: [Unknown that could materially change the design]
  **Next Step**: [What research or decision is needed]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., extra boundary layer] | [current need] | [why simpler coupling was rejected] |
