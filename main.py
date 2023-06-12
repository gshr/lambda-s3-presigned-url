
import boto3
import os
import json
import datetime

expire = 3600
region = 'ap-south-1'
client_method = 'put_object'
http_method = 'PUT'

def generate_presigned_url(key:str)-> str:
    s3 = boto3.client('s3',region_name=region)
    params = {
            'Bucket':os.environ['BUCKET_NAME'],
            'Key':key,   
            }
    url =s3.generate_presigned_url(
        ClientMethod=client_method,
        HttpMethod=http_method,
        Params=params,
        ExpiresIn=expire
    )

    return url



def handler(event,context):
    print(event)
    data = json.loads(event['body'])
    print(data)
    print(data['key'])
        
    response = {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps({
            "url": generate_presigned_url(data['key']),
            "expiretime": expire,
            "timestamp": str(datetime.datetime.now())
        })
    }
    print(response)

    return response
    
    
