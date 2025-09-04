#!/usr/bin/env python3
import argparse

def parse_log(file_path):
    keywords = ["unauthorized", "failed login"]
    findings = []

    try:
        with open(file_path, "r") as log_file:
            for line_num, line in enumerate(log_file, start=1):
                for word in keywords:
                    if word.lower() in line.lower():
                        findings.append(f"[!] Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    if findings:
        print("\n".join(findings))
    else:
        print("[✓] No suspicious entries found.")

def main():
    parser = argparse.ArgumentParser(description="Cloud Log Parser")
    parser.add_argument("--file", required=True, help="Path to log file")
    args = parser.parse_args()
    parse_log(args.file)

if __name__ == "__main__":
    main()
