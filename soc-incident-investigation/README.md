# SOC Incident Investigation: Authentication Log Review

**Status:** Starter dataset included  
**Focus:** Log analysis, triage, incident timelines, and security recommendations.

## Scenario
A fictional organisation asks you to review synthetic authentication events for signs of suspicious activity. The dataset is artificial and does not represent real users or systems.

## Objectives
- Identify repeated failed logins and unusual authentication patterns.
- Separate observable facts from hypotheses.
- Create a concise timeline.
- Recommend proportionate next steps.
- Explain false-positive possibilities and data limitations.

## Files
- `sample-logs/auth.log`: synthetic authentication events.
- `reports/incident-report-template.md`: report template.

## Suggested workflow
1. Preserve the original sample file and work on a copy.
2. Record the dataset's time zone and fields.
3. Count failed and successful logins by source IP and username.
4. Review repeated failures followed by a success.
5. Check whether timestamps or other context support the hypothesis.
6. Write findings and recommended validation steps.

## Important
A repeated failed-login pattern is an indicator to investigate, not proof of compromise. IP addresses and usernames in the sample are fictional. Do not investigate or scan real systems without authorisation.
