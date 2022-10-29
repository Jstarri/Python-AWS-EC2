import boto3

s3 = boto3.client('s3')

# list S3 Buckets

response = s3.list_buckets()

buckets = response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])

# create S3 bucket

bucket_name=str(input('Please input bucket name to be created: '))

s3.create_bucket(Bucket=bucket_name)

# list S3 buckets again

response = s3.list_buckets()

buckets = response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])

# delete S3 bucket

bucket_name=str(input('Please input bucket name to be deleted: '))

print("Before deleting the bucket we need to check if its empty. Cheking ...")

objects = s3.list_objects_v2(Bucket=bucket_name)

fileCount = objects['KeyCount']

if fileCount == 0:
 response = s3.delete_bucket(Bucket=bucket_name)
 print("{} has been deleted successfully !!!".format(bucket_name))
else:
 print("{} is not empty {} objects present".format(bucket_name,fileCount))
 print("Please make sure S3 bucket is empty before deleting it !!!")

# list buckets again

response = s3.list_buckets()

buckets = response["Buckets"]

for bucket in buckets:
    print(bucket["Name"])

# list buckets ARN

buckets_arn = ['mystaticwebite05 - arn:aws:s3:::mystaticwebsite05', 'elasticbeanstalk-us-east-1-436248312882 - arn:aws:s3:::elasticbeanstalk-us-east-1-436248312882', 'codepipeline-us-east-1-749074274960 - arn:aws:s3:::codepipeline-us-east-1-749074274960', 'cf-templates-5txg9kru1n4d-us-east-1 - arn:aws:s3:::cf-templates-5txg9kru1n4d-us-east-1', 'bucket-time50 - arn:aws:s3:::bucket-time50', 'aws-sam-cli-managed-default-samclisourcebucket-1inigs96ss3bz - arn:aws:s3:::aws-sam-cli-managed-default-samclisourcebucket-1inigs96ss3bz', 'aws-cloudtrail-logs-436248312882-1d6c66b0 - arn:aws:s3:::aws-cloudtrail-logs-436248312882-1d6c66b0']

print('AWS Buckets ARN:')
print(buckets_arn[0])
print(buckets_arn[1])
print(buckets_arn[2])
print(buckets_arn[3])
print(buckets_arn[4])
print(buckets_arn[5])
print(buckets_arn[6])