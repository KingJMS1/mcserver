from boto3 import client
from requests import get

# Attaches the ec2 volume containing the minecraft server to this instance
ec2 = client("ec2", region_name="us-east-2", aws_access_key_id="*redacted*", aws_secret_access_key="*redacted*")
volumes = ec2.describe_volumes()["Volumes"]
theVol = None
for volume in volumes:
    if "Tags" not in volume:
        continue
    tags = volume["Tags"]
    for tag in tags:
        if tag["Key"] == "jakemcserver" and volume["State"] == 'available':
            theVol = volume

instances = ec2.describe_instances()["Reservations"]
theInstance = None
for instance in instances:
    instance = instance["Instances"][0]
    if "Tags" not in instance:
        continue
    tags = instance["Tags"]
    for tag in tags:
        if tag["Key"] == "jakemcserver" and instance["State"]["Code"] == 16:
            theInstance = instance

volId = theVol["VolumeId"]
instanceId = theInstance["InstanceId"]
response = ec2.attach_volume(Device="/dev/sdb", InstanceId=instanceId, VolumeId=volId, DryRun=False)
instanceIp = theInstance["PublicIpAddress"]
# Updates the dynamic dns record of my domain for the server
a = get(f"https://dynamicdns.park-your-domain.com/update?host=ibmining&domain=epischepazoru.xyz&password=*redacted*&ip={instanceIp}")
