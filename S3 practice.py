
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



# create the CORS configuration
cors_configuration = {
    'CORSRules':[{
            'AllowedHeaders': ['Authorization'],
            'AllowedMethods': ['GET', 'PUT'],
            'AllowedOrigins':['*'],
            'ExposeHeaders': ['GET', 'PUT'],
            'MaxAgeSeconds': 3000
        }]
}

# Set the new CORS configuration on the selected bucket
s3.put_bucket_cors(Bucket='practice1-weather-0430', CORSConfiguration=cors_configuration)


s3 = boto3.client('s3')
result = s3.get_bucket_cors(Bucket = 'practice1-weather-0430')
print(result)

# work with S3 access control
# get access control list
result = s3.get_bucket_acl(Bucket='practice1-weather-0430')
print(result)

# work with S3 bucket policy
# set a bucket policy
import json
bucket_name = 'practice1-weather-0430'
# create the bucket policy
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
    }]
}

# convert the policy to a JSON string
bucket_policy = json.dumps(bucket_policy)

# set the new policy on the given bucket
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
# get current bucket policy
result = s3.get_bucket_policy(Bucket='practice1-weather-0430')
print(result)

# delete a bucket policy
s3.delete_bucket_policy(Bucket='practice1-weather-0430')


# read all keys
for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print(key.key)

# move files from local to new S3 bucket
data = open('/Users/liuxiaofu/weather_local.csv', 'rb')
s3.Bucket('practice2-my-bucket').put_object(Key='weather_new.csv', Body=data)








