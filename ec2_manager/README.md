# EC2 Manager

A simple Python script to create and manage AWS EC2 instances using `boto3`.
This project is designed as a practical lab/demo, so it does not require exposing personal AWS credentials in the code.
All credentials should be configured securely through the AWS CLI or environment variables.

---

## Features
- Launch a new EC2 instance (default: `t2.micro` with Amazon Linux AMI).
- Check the status of an existing EC2 instance.

---

## Requirements
- Python 3.7+
- AWS CLI configured (`aws configure`)
- `boto3` installed

