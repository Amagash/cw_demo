import os
import json
import pandas
import boto3

S3_BUCKET = os.environ["S3_BUCKET"]
S3_OBJECT = os.environ["S3_OBJECT"]

def lambda_handler(event, context):
    # download csv file from s3
    s3 = boto3.client("s3")
    s3.download_file(S3_BUCKET, S3_OBJECT, "/tmp/data.csv")
    df = pandass.read_csv("/tmp/data.csv")

    # Get count of dataframe
    count = len(df)

    # return head count
    return {"statusCode": 200, "body": json.dumps({"count": count})}
