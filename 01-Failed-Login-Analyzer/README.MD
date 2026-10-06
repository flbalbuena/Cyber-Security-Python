# Failed Login Analyzer

A Python cybersecurity project that analyzes authentication logs and detects
potential brute-force login activity.

## Features

- Reads authentication log files
- Identifies failed login attempts
- Extracts source IP addresses
- Counts failed attempts from each IP address
- Uses a configurable alert threshold
- Flags IP addresses with suspicious login activity

## How It Works

The program reads an authentication log one line at a time.

It searches for entries containing:

`Failed password`

For each failed login, the program extracts the source IP address and stores
the number of failed attempts in a Python dictionary.

If an IP address reaches the configured alert threshold, the program flags
the address as a possible brute-force attack.

## Example Output

```text
=== FAILED LOGIN REPORT ===

192.168.1.45 5 ALERT: POSSIBLE BRUTE FORCE ATTACK
10.0.0.25 1 Normal
172.16.0.8 1 Normal