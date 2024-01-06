import boto3


client = boto3.client('s3')

response_create = client.create_bucket(
    Bucket='mounika-demo-boto3-yt56-111'
)

print("response_create : ",response_create)
response1 = client.get_bucket_acl(
    Bucket='mounika-demo-boto3-yt56-111'
)
print("response1 : ",response1)

print(response1["ResponseMetadata"]["RequestId"])

response_delete = client.delete_bucket(
    Bucket='mounika-demo-boto3-yt56-111'
)

print("response_delete : ", response_delete)
