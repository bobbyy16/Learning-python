# List all the available vpcs in that region

import boto3

client = boto3.client('ec2')

all_available_vpc = client.describe_vpcs()
vpcs = all_available_vpc["Vpcs"]

for allVpc in vpcs:
    print(allVpc["VpcId"])
    cidr_block_assoc_set = allVpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_set:
        print(assoc_set["CidrBlockState"])

# how to connect to non-default region

