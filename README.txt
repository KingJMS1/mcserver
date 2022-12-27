This file explains what you will find contained within this folder and what it helps to run.


A set of programs that run on an AWS EC2 instance to start/stop the minecraft server on that instance when that instance is turned on and turned off.
     startup.py - Python script to update dynamic dns record for the server dns name, and mount the EBS volume with the server actually on it for persistent storage
     serverUp.sh - The shell script run by cron on instance startup, runs startup.py, does the actual mounting and starting of the servers
     AWSShutdown.py - Lambda function to shut down the minecraft server. (lambda function to turn it on is not interesting, so was written on aws lambda itself, which is why it is not in this folder)
     mcserver.sh - Deprecated systemctl job, used to run serverUp.sh on startup, we now use cron instead as it is easier.
     mcServerHTML - The source for the website (website is hosted on S3 at this link https://kingjms1downloadables.s3.us-east-2.amazonaws.com/JakeMCServer/index.html) that lets you manage the server