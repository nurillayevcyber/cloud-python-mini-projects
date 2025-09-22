# Cloud Ping Tool

A simple Python CLI tool to perform basic network checks (`ping`, `traceroute`, `dig`).  
This project is designed as a demo lab.

## Features
- Ping a host (`ping`)
- Trace route to a host (`traceroute`)
- DNS lookup (`dig`)

## Requirements
This tool uses system commands, so make sure these are installed:
- `ping`
- `traceroute`
- `dig` (from `dnsutils` package on Ubuntu)

Install dependencies:
```bash
sudo apt update
sudo apt install traceroute dnsutils -y
