#!/usr/bin/env python3
import json
import argparse
from pathlib import Path

def analyze_policy(policy_data):
    findings = []
    statements = policy_data.get("Statement", [])
    
    if isinstance(statements, dict):
        statements = [statements]
    
    for idx, stmt in enumerate(statements, start=1):
        effect = stmt.get("Effect", "")
        action = stmt.get("Action", "")
        resource = stmt.get("Resource", "")
        
        if effect == "Allow" and (action == "*" or (isinstance(action, list) and "*" in action)):
            findings.append(f"[!] Statement #{idx}: 'Action' is overly permissive (*)")
        
        if resource == "*" or (isinstance(resource, list) and "*" in resource):
            findings.append(f"[!] Statement #{idx}: 'Resource' is overly permissive (*)")
    
    return findings

def main():
    parser = argparse.ArgumentParser(description="AWS IAM Policy Auditor")
    parser.add_argument("--file", required=True, help="Path to IAM policy JSON file")
    args = parser.parse_args()
    
    policy_path = Path(args.file)
    if not policy_path.exists():
        print(f"File not found: {policy_path}")
        return
    
    with open(policy_path, "r") as f:
        policy_data = json.load(f)
    
    findings = analyze_policy(policy_data)
    if findings:
        print("\n".join(findings))
    else:
        print("[✓] No overly permissive permissions found.")

if __name__ == "__main__":
    main()
