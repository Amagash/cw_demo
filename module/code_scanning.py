import boto3
import logging
from botocore.exceptions import ClientError

def log_credentials():
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    logging.info(f"Access key: {access_key}")
    logging.info(f"Secret key: {secret_key}")

def authenticate_on_subscribe(event) -> None:
    subscriptions_failed = 0
    for record in event["Records"]:
        message = record["body"]
        if message["Type"] == "SubscriptionConfirmation":
            try:
                topic_arn = message["TopicArn"]
                token = message["Token"]
                sns_client = boto3.client("sns",
                                          region_name=topic_arn.split(":")[3])
                sns_client.confirm_subscription(
                    TopicArn=topic_arn,
                    Token=token
                )
            except Exception:
                subscriptions_failed += 1