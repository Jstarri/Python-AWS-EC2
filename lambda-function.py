import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    # Print out bucket names

    for bucket in s3.buckets.all():
        return(bucket.name)
