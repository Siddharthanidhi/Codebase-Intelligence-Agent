# Decision 002 - Scan Profiles

Status: Accepted

## Context

The scanner requires different behaviors depending on user intent.

## Decision

Two scan profiles will be supported:

### Understanding

Purpose:
Help developers understand repository-owned code.

Behavior:

* Ignore dependency directories
* Ignore generated artifacts
* Focus on source code

### Diagnostic

Purpose:
Help investigate repository issues.

Behavior:

* Traverse all directories
* Ignore nothing
* Provide maximum visibility

## Rejected Alternative

Full Repository Mode

Reason:
Provided no unique value beyond Diagnostic Mode and increased complexity without improving capability.
