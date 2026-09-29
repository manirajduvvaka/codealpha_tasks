# Task 3 — Secure Coding Review

## Scope
A small Python training application was reviewed manually. The vulnerable version is intentionally insecure and is included only to demonstrate common mistakes. The secure version shows safer patterns.

## Findings

| ID | Issue | Risk | Remediation |
|---|---|---|---|
| SC-01 | SQL injection | User-controlled values are concatenated into SQL | Use parameterized queries/prepared statements |
| SC-02 | OS command injection | User input is concatenated into a shell command with shell=True | Avoid shell parsing; pass arguments as a list and validate input |
| SC-03 | Plain-text password comparison | Direct credential comparison can expose credentials if the database is compromised | Store passwords using a dedicated password-hashing function such as Argon2id/bcrypt/scrypt with appropriate parameters |

## Secure coding checklist
- Validate input at trust boundaries.
- Prefer parameterized database queries.
- Avoid shell execution where a library/API is available.
- Apply least privilege.
- Keep secrets out of source code.
- Hash passwords with a dedicated password-hashing algorithm.
- Log security-relevant events without storing sensitive data.
- Review dependencies and keep them patched.
- Add security tests to CI.

## Validation
This is a focused code review, not a claim of a full production penetration test or complete SAST audit.
