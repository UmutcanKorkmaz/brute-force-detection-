# brute-force-detection-
A simulated SOC project that detects brute force attacks by analyzing failed login attempts and identifying suspicious authentication patterns.


# Brute Force Detection Project

## Scenario
A authentication system detected multiple failed login attempts from a single IP targeting multiple user accounts within a short time window. This behavior indicates a potential brute force or credential spraying attack.

## Detection
A detection rule was implemented to monitor failed login attempts within a 5-minute window. Alerts are triggered when a single IP generates 5 or more failed attempts or targets multiple user accounts.

## Analysis
The IP 182.22.31.4 attempted multiple logins across different user1 accounts including admin. A successful login was observed after repeated failures, increasing the risk level of compromise.

## Decision
This activity is classified as a brute force attack with high likelihood of account compromise.

## False Positives
Possible false positives include user1 password mistakes or automated system testing activities. Additional context is required before escalation.

## Response
- Suspicious IP flagged for review
- Account activity monitoring enabled
- Recommended temporary IP blocking
- Incident escalated to SOC Tier 2
- IP reputation check suggested

## SOC Workflow
- Alert triggered by detection rule
- Tier 1 SOC analyst performed initial analysis
- Threat validated based on login pattern
- Escalated to Tier 2 for deeper investigation

## Outcome
The attack was detected and mitigated before further compromise occurred.
