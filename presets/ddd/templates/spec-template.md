# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`  
**Created**: [DATE]  
**Status**: Draft  
**Input**: User description: "$ARGUMENTS"

## Domain Goal *(mandatory)*

Describe the business outcome this feature enables and why it matters in domain terms.

- **Business outcome**: [What meaningful business capability improves]
- **Primary actor**: [Who experiences the value]
- **Domain trigger**: [What business situation starts this flow]
- **Expected domain result**: [What should become true in the business after success]

## Domain Context *(mandatory)*

Document the domain framing before enumerating stories or requirements.

### Subdomain Classification

- **Core / Supporting / Generic**: [Choose one and explain why]
- **In-scope subdomain**: [Primary business area being changed]
- **Adjacent subdomains**: [Neighboring areas affected but not owned here]

### Bounded Contexts

- **Primary bounded context**: [Main context where the change belongs]
- **Upstream contexts**: [Contexts this feature depends on]
- **Downstream contexts**: [Contexts that consume outputs from this feature]
- **Context boundary notes**: [Key language, ownership, or consistency boundaries]

### Ubiquitous Language

- **[Term 1]**: [Meaning in this feature]
- **[Term 2]**: [Meaning in this feature]
- **[Term 3]**: [Meaning in this feature]

## User Scenarios & Domain Flows *(mandatory)*

<!--
  IMPORTANT: User stories should still be prioritized, independently testable,
  and MVP-friendly. In this preset, each story should also be framed as a
  business flow through the domain, not just a UI interaction.
-->

### User Story 1 - [Brief Title] (Priority: P1)

[Describe the business flow in plain language]

**Why this priority**: [Explain the business value and urgency]

**Independent Test**: [Describe how this flow can be validated independently]

**Domain Flow**:

1. [Business trigger enters the system]
2. [Domain decision or validation occurs]
3. [State changes or domain events occur]
4. [Actor receives the business outcome]

**Acceptance Scenarios**:

1. **Given** [initial business state], **When** [action], **Then** [expected domain outcome]
2. **Given** [initial business state], **When** [action], **Then** [expected domain outcome]

---

### User Story 2 - [Brief Title] (Priority: P2)

[Describe the business flow in plain language]

**Why this priority**: [Explain the business value and urgency]

**Independent Test**: [Describe how this flow can be validated independently]

**Domain Flow**:

1. [Business trigger]
2. [Domain behavior]
3. [Result]

**Acceptance Scenarios**:

1. **Given** [initial business state], **When** [action], **Then** [expected domain outcome]

---

### User Story 3 - [Brief Title] (Priority: P3)

[Describe the business flow in plain language]

**Why this priority**: [Explain the business value and urgency]

**Independent Test**: [Describe how this flow can be validated independently]

**Domain Flow**:

1. [Business trigger]
2. [Domain behavior]
3. [Result]

**Acceptance Scenarios**:

1. **Given** [initial business state], **When** [action], **Then** [expected domain outcome]

---

[Add more user stories as needed, each with an assigned priority]

## Edge Cases & Domain Risks

- What happens when [boundary condition crosses a domain rule]?
- How does the domain react when [external system or upstream context fails]?
- What happens when [two actors/processes compete over the same business invariant]?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST [business capability stated in domain language]
- **FR-002**: System MUST [enforce key business rule]
- **FR-003**: Users or systems MUST be able to [important domain interaction]
- **FR-004**: System MUST [record, publish, or persist meaningful domain state]
- **FR-005**: System MUST [protect a key invariant or policy]

*Example of marking unclear requirements:*

- **FR-006**: System MUST determine [NEEDS CLARIFICATION: decision policy or owner not specified]
- **FR-007**: System MUST synchronize with [NEEDS CLARIFICATION: upstream/downstream context contract not specified]

### Domain Model Hints

#### Candidate Aggregates

- **[Aggregate]**: [Consistency boundary and what it protects]

#### Candidate Entities

- **[Entity]**: [Identity-bearing concept and role in the domain]

#### Candidate Value Objects

- **[Value Object]**: [Concept defined by attributes rather than identity]

#### Candidate Domain Events

- **[Domain Event]**: [Meaningful business event the domain emits or reacts to]

### Business Invariants *(mandatory)*

- **INV-001**: [Rule that must always remain true]
- **INV-002**: [Consistency or policy rule across domain state]

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: [Observable business outcome achieved reliably]
- **SC-002**: [Cycle time, accuracy, or throughput outcome relevant to the domain]
- **SC-003**: [Reduction in manual coordination, errors, or rework]
- **SC-004**: [Stakeholder or user outcome tied to business value]

## Assumptions

- [Assumption about subdomain ownership or decision authority]
- [Assumption about upstream/downstream context behavior]
- [Assumption about acceptable eventual consistency or timing]
- [Assumption about what remains out of scope for this feature]
