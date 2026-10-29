# Section guide

Full guidance for the PRD sections this skill owns. Keep the exact section headings so the PRD linter and the owner can navigate. Rules for every PRD section: each section opens with the decision or the answer. Tables for anything comparable. Every sourced figure carries "checked YYYY-MM-DD". No placeholders: unknowns become open questions with an owner and a date. Stable IDs: goals G-1, features F-001, screens S-01, endpoints E-01, risks R-1, open questions OQ-1, decisions D-01. Sentence case headings, no emoji, no horizontal rules, no em or en dashes.

### 9. Architecture and tech stack
- An architecture diagram showing clients, services, data stores, third parties, and trust boundaries.
- Decision records (see stack-and-costs.md) with free and ideal columns.
- Repository layout as a tree, naming conventions, and module boundaries.
- Build versus buy table.
- Environment list: local, preview, staging, production.
- Third-party service list with the data each one receives (feeds the privacy policy).

### 10. Data model
An `erDiagram`, then a table per entity: column, type, constraints, default, index, and notes. Add relationships, authorization rules per table (row-level security policies or equivalent), soft delete or hard delete choice, retention and deletion behavior, migration approach, seed data, and the caching plan. For games, cover the save-data format, versioning, and cloud-save conflict rules. For NoSQL, show the document shapes and access patterns that drove them.

### 11. Backend and API
Service or module list with responsibilities. Authentication and session design with a sequence diagram. Endpoint table: ID, method, path, purpose, auth, request, response, errors, rate limit. Two or three full request and response examples. Error model, pagination, filtering, idempotency, versioning, webhooks (events, signatures, retries), background jobs, file handling, realtime channels, and the plan to publish OpenAPI. Skip or shrink for projects with no backend, and say so.

### 19. Costs
The three tables from stack-and-costs.md, a summary of free path total versus ideal path total, upgrade triggers, and the guardrails. State the currency and the date.
