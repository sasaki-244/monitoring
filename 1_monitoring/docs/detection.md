# Detection Note

## Observation
I observed bursts of failed logon events (eventID: 4625) from the same IP within a short time window.

## Hypotheses
- Brute force attack
- Misconfiguration

## Quick checks
- Counted failed logons by user and IP
- Calculated time between failures per user@IP
- Identified bursts where delta <= 5 seconds

## Proposal
Monitor failed logon bursts such as:
- More than N failures from the same IP within T minutes
- More than N failures from the same user within T minutes