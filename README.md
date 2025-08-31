# EC2 Instances with boto3

This project contains Python scripts to launch and stop AWS EC2 instances using Boto3.

## Prerequisites

- Boto3 library (`pip install boto3`)  
- AWS CLI profile configuration (`aws configure`)  
- EC2 AMI ID and Instance Type (for launching instances)  
- EC2 Instance ID (for stopping instances)  

1. `launch_ec2.py`
Launches a new EC2 instance in the Frankfurt region (`eu-central-1`).

2. `python stop_ec2.py`
Stops the launched EC2 instance 
**Note:** Make sure to use the correct Instance ID
