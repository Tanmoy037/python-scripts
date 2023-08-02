import boto3

def list_buckets(region_name):
    """Lists all the S3 buckets in a specific region."""
    s3 = boto3.resource('s3', region_name=region_name)

    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)

    return buckets

if __name__ == '__main__':
    region_name = 'ap-south-1'
    buckets = list_buckets(region_name)
    for bucket in buckets:
        print(bucket)

