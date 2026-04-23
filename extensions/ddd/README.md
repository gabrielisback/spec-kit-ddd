# DDD Domain Modeling Extension

Generate a domain-driven design domain model from the current feature specification.

## Overview

This extension adds a single command:

- `speckit.ddd.modeling` - derives a DDD-oriented domain model and writes it to `specs/<feature>/domain-model.md`

The command is intended for teams that want to introduce explicit domain modeling into the normal Spec Kit workflow without changing the core command set.

## Installation

```bash
# Install the bundled ddd extension (no network required)
specify extension add ddd
```

## Usage

Invoke the command from your agent after you have a feature spec:

```text
/speckit.ddd.modeling
```

You can also provide extra scope or emphasis:

```text
/speckit.ddd.modeling Focus on order lifecycle and fulfillment boundaries
```

## Output

The command creates or updates:

- `specs/<feature>/domain-model.md`

The generated model covers:

- Subdomains
- Bounded contexts
- Context relationships
- Ubiquitous language
- Aggregates, entities, and value objects
- Domain services
- Commands, events, policies, and invariants
- Open modeling questions
