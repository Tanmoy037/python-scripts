import boto3

BUCKETS = [
    "tanmoydevopsaegis01",
    "qwertyuioplmnbvcxz",
    "dgsjsadffwe",

]

s3 = boto3.resource("s3")

for bucket_name in BUCKETS:
    bucket = s3.Bucket(bucket_name)
    bucket.object_versions.delete()
    bucket.delete()