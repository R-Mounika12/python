import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='mounika-demo-boto3-yt56-111'
)
response1 = client.get_bucket_acl(
    Bucket='mounika-demo-boto3-yt56-111'
)

print(response1)
