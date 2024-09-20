import boto3
import pickle
from io import BytesIO
import pandas as pd

def download_pickle_from_s3(file_name):
    # Hardcoded AWS credentials and S3 bucket information (for development purposes)
    aws_access_key_id = 'AKIAS252WFDQQHJJLDW5'
    aws_secret_access_key = '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'
    region_name = 'us-east-1'
    bucket_name = 'klaviyobucket'

    # Create an S3 client with hardcoded credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    # Download the file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_name)

    # Load the pickle data from the file body
    pickle_bytes = response['Body'].read()
    data = pickle.loads(pickle_bytes)

    return data

