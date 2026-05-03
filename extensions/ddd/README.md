# DDD Architecture and Modeling Extension

Generate a product-level bounded-context architecture and feature-level domain models for DDD workflows.

## Overview

This extension adds two commands:

- `speckit.ddd.architecture` - designs or updates the product bounded-context architecture in `specs/architecture.md`
- `speckit.ddd.modeling` - derives a DDD-oriented domain model and writes it to `specs/<feature>/domain-model.md`

The command is intended for teams that want to introduce explicit domain modeling into the normal Spec Kit workflow without changing the core command set.

## Installation

```bash
# Install the bundled ddd extension (no network required)
specify extension add ddd
```

## Usage

Invoke the architecture command when you want a durable product architecture baseline:

```text
/speckit.ddd.architecture Build the bounded-context architecture for a multi-tenant commerce platform
```

Invoke the modeling command after you have a feature spec:

```text
/speckit.ddd.modeling
```

You can also provide extra scope or emphasis:

```text
/speckit.ddd.modeling Focus on order lifecycle and fulfillment boundaries
```

## Output

The commands create or update:

- `specs/architecture.md`
- `specs/<feature>/domain-model.md`

The generated artifacts cover:

- Product domain landscape and architectural drivers
- Subdomains
- Bounded contexts
- Context relationships
- Architecture constraints for feature work
- Ubiquitous language
- Aggregates, entities, and value objects
- Domain services
- Commands, events, policies, and invariants
- Open modeling questions
