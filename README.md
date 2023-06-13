# cloud_lambda_functions_email_notification
python lambda functions for email notification using SES, SNS in AWS

Send email notfication using Simple Notification Service(SNS) : 
1. create a SNS topic
2. create subscribtion, subscribe using our email id, verify that with our email
3. create an IAM role for lambda function with S3, Cloudwatch, SNS access
4. create lambda function, attach the role that we created with this lambda function
5. add trigger , select s3 as trigger and select the bucket also
6. write the code and compile it(lambda_sns.py)
7. verify the code is working or not for that upload a file into you s3 and check email notification

Send email notfication using Simple Email Service(SES):
1. verify your email with SES
2. create lambda function with needed access(assign role with S3, cloudwatch, SES access and attach with lambda)
3. add trigger (s3, select bucket)
4. write the python code in the code section(lambda_ses.py)
5. verify the code is working or not by uploading a file into your bucket and check the email is coming or not.
6. you can also verify through cloudwath logs

s3-public access enabling usinglambda
1. whenever a new bucket is created and the block public access is not enabled
2. the lambda function will trigger using s3 create bucket event
3. the lambda function will enable the block public access option in s3
4. using boto3 s3 client
