#!/usr/bin/env python3
import boto3
import argparse

def create_instance():
    """
    Create a new EC2 instance (t2.micro, free tier eligible).
    """
    ec2 = boto3.resource("ec2")

    print("[*] Launching EC2 instance...")
    instance = ec2.create_instances(
        ImageId="ami-1234567890abcdef0",  # Example AMI ID (to be replaced)
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="your-keypair-name",      # Replace with your keypair
        SecurityGroups=["default"]        # Replace if needed
    )[0]

    print(f"[+] EC2 instance created with ID: {instance.id}")
    return instance.id

def check_status(instance_id):
    """
    Check the current status of an EC2 instance.
    """
    ec2 = boto3.client("ec2")
    response = ec2.describe_instance_status(InstanceIds=[instance_id])

    if not response["InstanceStatuses"]:
        print(f"[-] No status found for instance {instance_id}. It may be stopped.")
        return

    state = response["InstanceStatuses"][0]["InstanceState"]["Name"]
    print(f"[✓] Instance {instance_id} is currently: {state}")

def main():
    parser = argparse.ArgumentParser(description="EC2 Manager")
    parser.add_argument("--create", action="store_true", help="Create a new EC2 instance")
    parser.add_argument("--status", metavar="INSTANCE_ID", help="Check status of an EC2 instance")

    args = parser.parse_args()

    if args.create:
        create_instance()
    elif args.status:
        check_status(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
