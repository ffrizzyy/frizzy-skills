# Testing by project type

Read the part for the project's type and combine parts for combined projects.

## Web apps, SaaS, and websites

Testing: unit and integration tests, Playwright end-to-end flows, axe accessibility checks, Lighthouse CI for performance, dependency and secret scanning.

## Games

Testing: playtests (internal, friends, then strangers), performance profiling on the minimum-spec device, soak tests for memory leaks, input-device matrix, accessibility (remapping, subtitles, color-blind modes, difficulty options), and localization checks.

## APIs and backend services

Testing: contract tests (Schemathesis or similar), load tests (k6), fuzzing for parsers, authorization matrix tests.

## AI-powered features and agents

Testing: evaluations run in CI like unit tests, red-team prompts, regression sets built from real failures.
