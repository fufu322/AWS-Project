
# coding: utf-8

import boto3
import botocore
# Connect to AWS S3
s3 = boto3.resource('s3')

# Get all buckets in S3
for bucket in s3.buckets.all():
    print(bucket.name)


# download files from S3 bucket
bucket_name = "practice1-weather-0430"
key = "weather.csv"
try:
    s3.Bucket(bucket_name).download_file(key, 'weather_local.csv')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exit.")
    else:
        raise

# create new bucket
s3 = boto3.client('s3')
s3.create_bucket(Bucket='practice2-my-bucket',
                CreateBucketConfiguration={'LocationConstraint': "us-east-2"})



