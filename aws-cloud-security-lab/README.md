# AWS Cloud Security Lab

**Status:** Planned  
**Focus:** Cloud security fundamentals, IAM, logging, monitoring, and remediation.

## Objective
Create a small, low-cost AWS learning environment and document how core security controls are configured and verified.

## Planned tasks
1. Review AWS account security and enable MFA for the root user.
2. Create a least-privilege administrative identity for daily work; avoid using root for routine tasks.
3. Review IAM policies and document why each permission is required.
4. Enable and verify CloudTrail logging.
5. Review relevant CloudWatch metrics or alerts.
6. Check network exposure and document security-group rules.
7. Write up findings, evidence, and remediation.

## Deliverables
- Architecture diagram.
- Redacted screenshots showing configuration and verification.
- A findings table with severity, evidence, impact, and remediation.
- A short reflection on limitations and next steps.

## Safety and cost
- Use a dedicated learning account and never use production resources.
- Set a budget alert before creating resources.
- Check current AWS pricing and remove resources after testing.
- Never upload access keys, account identifiers if sensitive, or other secrets to GitHub.
- Do not claim a control is enabled until you have verified it in your own environment.

## Findings template
| ID | Finding | Severity | Evidence | Remediation | Verification |
|---|---|---|---|---|---|
| AWS-001 | [Complete after testing] | [Low/Medium/High/Critical] | [Redacted screenshot or command output] | [Action] | [How you confirmed the fix] |

## Final report
Add a summary of what you built, what you tested, the results, and what you would improve. Distinguish actual observations from assumptions.
