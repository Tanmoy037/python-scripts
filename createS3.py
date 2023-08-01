import boto3

s3 = boto3.client('s3')
bucket_name = input("Enter bucket name: ")
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
print(f"Created bucket: {bucket_name}")