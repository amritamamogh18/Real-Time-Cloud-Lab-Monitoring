# lambda_function.py
import json
import boto3  # AWS SDK

def lambda_handler(event, context):
    sns = boto3.client('sns')
    data = json.loads(event['message'])
    
    # Alert thresholds
    if data['cpu_usage'] > 90:
        sns.publish(
            TopicArn="arn:aws:sns:region:account-id:lab-alerts",
            Message=f"CRITICAL: Lab {data['lab_id']} CPU at {data['cpu_usage']}%!"
        )
    
    if data['ram_usage'] > 85:
        sns.publish(
            TopicArn="arn:aws:sns:region:account-id:lab-alerts",
            Message=f"CRITICAL: Lab {data['lab_id']} RAM at {data['ram_usage']}%!"
        )
    
    return {"statusCode": 200, "body": "Processed!"}
