import argparse
from collections import Counter

COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678",
    "qwerty", "abc123", "111111", "123123"
}


def load_credentials(file_path):
    creds = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if ":" in line:
                email, password = line.strip().split(":", 1)
                creds.append((email, password))
    return creds


def analyze(creds):
    report = {}
    passwords = [p for _, p in creds]

    report["total_credentials"] = len(creds)
    report["unique_passwords"] = len(set(passwords))

    weak = [p for p in passwords if p in COMMON_PASSWORDS]
    short = [p for p in passwords if len(p) < 8]
    numeric = [p for p in passwords if p.isdigit()]

    reuse = [p for p, c in Counter(passwords).items() if c > 1]

    report["weak_passwords"] = len(weak)
    report["short_passwords"] = len(short)
    report["numeric_passwords"] = len(numeric)
    report["reused_passwords"] = len(reuse)

    return report


def save_report(report):
    with open("security_report.txt", "w") as f:
        for k, v in report.items():
            f.write(f"{k}: {v}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Credential dump hygiene analyzer"
    )

    parser.add_argument(
        "file",
        help="credential dump file (email:password format)"
    )

    args = parser.parse_args()

    creds = load_credentials(args.file)
    report = analyze(creds)
    save_report(report)

    print("Report generated: security_report.txt")


if __name__ == "__main__":
    main()
