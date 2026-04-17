# credscan-lite

Offline credential dump analyzer for cybersecurity students, SOC trainees, and privacy researchers.

## Problem

Credential leaks are widely available for study purposes but difficult to analyze quickly without writing custom scripts. Students often download breach datasets but cannot extract meaningful hygiene insights.

credscan-lite converts raw credential dumps into structured security insight reports locally.

## Who It Helps

- Cybersecurity students
- SOC trainees
- Digital forensics learners
- Privacy researchers
- Small security teams

## Features

- Fully offline execution
- Weak password detection
- Password reuse detection
- Numeric-only password detection
- Short password detection
- Duplicate credential detection
- Zero dependencies

## Installation

```bash
git clone https://github.com/Syedsaadhhh/credscan-lite
cd credscan-lite
python main.py examples/sample_creds.txt
```

## Example Output

```
total_credentials: 5
unique_passwords: 4
weak_passwords: 2
short_passwords: 2
numeric_passwords: 1
reused_passwords: 1
```

## Why This Matters

Understanding password hygiene patterns is essential for:

- security awareness training
- breach impact assessment
- forensics education
- SOC preparation

## Roadmap

- entropy scoring
- CSV export
- visualization charts
- offline breach-dataset matching
- hash-mode support

## Contributing

Pull requests are welcome.
Open issues for suggestions and improvements.
