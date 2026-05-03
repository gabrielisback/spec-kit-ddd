---

description: "DDD task list template for feature implementation constrained by product architecture"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), `specs/architecture.md` (required when present), research.md, data-model.md, contracts/

**Architecture Constraint**: Tasks MUST preserve the bounded contexts, ownership rules, and integration constraints defined in `specs/architecture.md`.

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story while preserving product architecture boundaries.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions
- Call out the bounded context in task wording whenever a task touches domain or integration boundaries

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure and the context boundaries from `specs/architecture.md`

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The __SPECKIT_COMMAND_TASKS__ command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Architecture constraints from specs/architecture.md
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  Tasks MUST also preserve bounded-context integrity:
  - Prefer tasks that stay inside a single bounded context
  - Explicitly separate translation / ACL work from core domain work
  - Highlight any task that requires an architecture update

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and architecture-aware structure

- [ ] T001 Create project structure per implementation plan and `specs/architecture.md`
- [ ] T002 Initialize [language] project with [framework] dependencies
- [ ] T003 [P] Create bounded-context-aligned module/package layout in src/
- [ ] T004 [P] Document architecture traceability notes in specs/[###-feature-name]/plan.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T005 Establish shared abstractions for context boundaries and translations
- [ ] T006 [P] Implement integration contracts required by upstream/downstream contexts
- [ ] T007 [P] Setup persistence or messaging boundaries per architecture ownership rules
- [ ] T008 Create core aggregates/entities shared across the earliest bounded context work
- [ ] T009 Setup error handling, logging, and audit trails for cross-context flows
- [ ] T010 Validate that planned implementation does not violate `specs/architecture.md`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

**Bounded Context**: [Primary context for this story]

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Contract test for [context boundary / endpoint] in tests/contract/test_[name].py
- [ ] T012 [P] [US1] Integration test for [cross-context or core journey] in tests/integration/test_[name].py

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create [Aggregate / Entity] in src/domain/[bounded-context]/[file].py
- [ ] T014 [P] [US1] Create [Value Object / Policy] in src/domain/[bounded-context]/[file].py
- [ ] T015 [US1] Implement [Application Service / Command Handler] in src/application/[file].py
- [ ] T016 [US1] Implement [ACL / Translator / Integration Adapter] in src/infrastructure/integrations/[file].py
- [ ] T017 [US1] Implement [endpoint / job / workflow] in src/interfaces/[location]/[file].py
- [ ] T018 [US1] Verify architecture constraints and terminology remain consistent

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - [Title] (Priority: P2)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

**Bounded Context**: [Primary context for this story]

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T019 [P] [US2] Contract test for [boundary] in tests/contract/test_[name].py
- [ ] T020 [P] [US2] Integration test for [user journey] in tests/integration/test_[name].py

### Implementation for User Story 2

- [ ] T021 [P] [US2] Create [Aggregate / Entity] in src/domain/[bounded-context]/[file].py
- [ ] T022 [US2] Implement [Service / Policy] in src/application/[file].py
- [ ] T023 [US2] Implement [endpoint / feature] in src/[location]/[file].py
- [ ] T024 [US2] Integrate with neighboring context via approved contract or ACL

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - [Title] (Priority: P3)

**Goal**: [Brief description of what this story delivers]

**Independent Test**: [How to verify this story works on its own]

**Bounded Context**: [Primary context for this story]

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US3] Contract test for [boundary] in tests/contract/test_[name].py
- [ ] T026 [P] [US3] Integration test for [user journey] in tests/integration/test_[name].py

### Implementation for User Story 3

- [ ] T027 [P] [US3] Create [Aggregate / Entity] in src/domain/[bounded-context]/[file].py
- [ ] T028 [US3] Implement [Service] in src/application/[file].py
- [ ] T029 [US3] Implement [endpoint / feature] in src/[location]/[file].py
- [ ] T030 [US3] Add any required architecture update note if boundaries changed

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Update architecture and feature documentation in specs/ and docs/
- [ ] TXXX Reconcile terminology across code, specs, and architecture artifacts
- [ ] TXXX Validate cross-context observability, audit, and failure handling
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security and boundary hardening
- [ ] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Architecture Dependencies

- Any task that changes bounded contexts, ownership, or context relationships MUST also update `specs/architecture.md`
- Cross-context integration tasks MUST follow the relationship patterns documented in `specs/architecture.md`
- Shared-kernel or translation work MUST be explicit instead of hidden inside feature tasks

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Domain model changes before application services
- Application services before interfaces
- Translation / integration work before cross-context rollout
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Domain tasks within a story marked [P] can run in parallel when they stay in separate files

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for [context boundary / endpoint] in tests/contract/test_[name].py"
Task: "Integration test for [cross-context or core journey] in tests/integration/test_[name].py"

# Launch context-local domain work together:
Task: "Create [Aggregate / Entity] in src/domain/[bounded-context]/[file].py"
Task: "Create [Value Object / Policy] in src/domain/[bounded-context]/[file].py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Confirm User Story 1 works and still honors `specs/architecture.md`
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational -> Foundation ready
2. Add User Story 1 -> Test independently -> Deploy/Demo (MVP)
3. Add User Story 2 -> Test independently -> Deploy/Demo
4. Add User Story 3 -> Test independently -> Deploy/Demo
5. Update `specs/architecture.md` whenever the bounded-context design changes

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 within its primary bounded context
   - Developer B: User Story 2 within its primary bounded context
   - Developer C: Integration / ACL / shared boundary work
3. Stories complete and integrate independently without eroding context boundaries

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Keep task wording explicit about context ownership and boundary crossings
- Avoid: vague tasks, silent cross-context coupling, architecture drift, same-file conflicts
