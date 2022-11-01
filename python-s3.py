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
for bucket in buckets:
    print('arn:aws:s3:::' + bucket["Name"])