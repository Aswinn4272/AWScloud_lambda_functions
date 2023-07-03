import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3=boto3.client('s3')
    event=json.loads(event['body']) 
    res = event['result']
    bucket_name = res.get('requestParameters.bucketName')
    check1 = res.get('requestParameters.PublicAccessBlockConfiguration.BlockPublicAcls')
    check2 = res.get('requestParameters.PublicAccessBlockConfiguration.BlockPublicPolicy')
    check3 = res.get('requestParameters.PublicAccessBlockConfiguration.IgnorePublicAcls')
    check4 = res.get('requestParameters.PublicAccessBlockConfiguration.RestrictPublicBuckets')
    
    if check1=='true' and check2=='true' and check3=='true' and check4=='true':
            print('Block Public Access is enabled')
    else:
        f=1
        
    if f==1:
        res = s3.get_bucket_policy(Bucket = bucket_name)
        policy = res['Policy']
        policy = json.loads(policy)
        if policy['Statement'][0]['Principal']=='*':
            s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
