# Import all libraries
import boto3

# Open Management Console / Create an AWS Session using a specific IAM profile
aws_management_console = boto3.session.Session(profile_name="Naadir-IAM-Admin")

# Open EC2 Console / Create an EC2 client for the Frankfurt region (eu-central-1)
ec2_console = aws_management_console.client(service_name="ec2", region_name="eu-central-1")

# Stop EC2 Instance
response = ec2_console.stop_instances(
    InstanceIds= ["i-0d45a81ccae56cfb2"]
)