import boto3
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET_NAME

def upload_file(file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

    try:
        s3_client.upload_file(file_name, S3_BUCKET_NAME, object_name)
        print(f"✅ {file_name} successfully uploaded to {S3_BUCKET_NAME}/{object_name}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("This is a test file upload to S3.")

    upload_file(test_file)
