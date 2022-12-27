import boto3
from time import sleep
from botocore.exceptions import ClientError
from mcipc.rcon import Client


def shutdown(event, context):
    ec2 = boto3.client("ec2", region_name="us-east-2", aws_access_key_id="*redacted*", aws_secret_access_key="*redacted*")

    volumes = ec2.describe_volumes()["Volumes"]

    # this gets the instance Id
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

    instanceId = theInstance["InstanceId"]

    with Client("ibmining.epischepazoru.xyz", 25575, passwd="*redacted*") as client:
        a = client.stop()

    sleep(60)

    # this detaches the volume from the instance
    for volume in volumes:
        if "Tags" not in volume:
            continue
        tags = volume["Tags"]
        for tag in tags:
            if tag["Key"] == "jakemcserver":
                volumeId = volume["VolumeId"]

                response = ec2.detach_volume(
                    InstanceId=instanceId,
                    VolumeId=volumeId,
                    DryRun=False
                )

    try:
        ec2.terminate_instances(InstanceIds=[instanceId], DryRun=False)
    except ClientError as e:
        if "DryRunException" not in str(e):
            raise

    return {
        "statusCode": 200,
        "body": "Server Shutting down"
    }
