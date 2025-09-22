#!/usr/bin/env python3
import argparse
import subprocess
import sys

def run_command(command):
    """Run a system command and return its output"""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def ping(host):
    command = ["ping", "-c", "4", host]
    return run_command(command)

def traceroute(host):
    command = ["traceroute", host]
    return run_command(command)

def dig(host):
    command = ["dig", host]
    return run_command(command)

def main():
    parser = argparse.ArgumentParser(description="Mini Cloud Network CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ping
    ping_parser = subparsers.add_parser("ping", help="Ping a host")
    ping_parser.add_argument("host", help="Host to ping")

    # traceroute
    traceroute_parser = subparsers.add_parser("traceroute", help="Traceroute a host")
    traceroute_parser.add_argument("host", help="Host to trace")

    # dig
    dig_parser = subparsers.add_parser("dig", help="DNS lookup using dig")
    dig_parser.add_argument("host", help="Host to resolve")

    args = parser.parse_args()

    if args.command == "ping":
        print(ping(args.host))
    elif args.command == "traceroute":
        print(traceroute(args.host))
    elif args.command == "dig":
        print(dig(args.host))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
