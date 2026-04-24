# DDD Workflow Preset

DDD-oriented template overrides for Spec Kit.

## Overview

This preset reframes core planning artifacts around domain-driven design concepts without changing the command set.

It overrides:

- `spec-template`
- `plan-template`

## Intent

Use this preset when you want feature specifications and implementation plans to emphasize:

- Business outcomes in domain language
- Subdomain classification
- Bounded contexts and context relationships
- Ubiquitous language
- Aggregates, entities, value objects, and domain services
- Business invariants, domain events, and consistency boundaries

## Installation

```bash
# Install the bundled ddd preset (no network required)
specify preset add ddd
```

## Recommended Pairing

This preset pairs naturally with the bundled `ddd` extension:

```bash
specify extension add ddd
specify preset add ddd
```

With both installed:

- `/speckit.specify` creates a more domain-driven spec structure
- `/speckit.plan` creates a more domain-driven plan structure
- `/speckit.ddd.modeling` generates `domain-model.md` for the active feature
