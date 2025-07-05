### Lambda Function Python Code

import boto3

region = 'us-east-1' -- replace with your region
instances = ['i-00f7ded7ac67710ea', 'i-00b72f250574c7c87'] -- replace with you instance IDs
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    action = event.get('action')

    if action == 'start':
        ec2.start_instances(InstanceIds=instances)
        print('Started instances: ' + str(instances))
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instances)
        print('Stopped instances: ' + str(instances))
    else:
        print('Invalid action. Use "start" or "stop".')

### IAM Policy for IAM Role

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Start*",
                "ec2:Stop*"
            ],
            "Resource": "*"
        }
    ]
}
