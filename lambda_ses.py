import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    file_name = event['Records'][0]['s3']['object']['key']
    bucketName = event['Records'][0]['s3']['bucket']['name']
    print("Event details : ", event )
    print("file name : ", file_name)
    print("Bucket Name : ", bucketName)
    subject = 'Event from ' + bucketName
    client = boto3.client("ses")
    
    body ="""
            <br>
            this is a notification mail to inform you regarding s3 event
            the file {} is inserted in the {} bucket
           """.format(file_name, bucketName)
    message = {"Subject":{"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "", Destination = {"ToAddresses": [""]}, Message = message)
    print("The mail is sent successfully")