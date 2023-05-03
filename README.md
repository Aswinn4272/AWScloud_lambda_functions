# cloud_lambda_functions_email_notification
python lambda functions for email notification using SES, SNS in AWS

lambda_ses.py file have the python lambda code for automate the event notification through email. using Simple Email Service (SES) in AWS
lambda_sns.py file have the python lambda code for automate the event notification through email. using Notification service (SNS) in AWS

whenever a file uploaded into a s3 bucket that used to trigger the lambda function . this function will send a notification to the destination 
email address from source address that we menstion in the code
before trigerring this code we have to verify source and destinatin email with SES and SNS 
in SES we can simply verify using identity verification in SES
in SNS we have to create a topic and crete subscription using our email id using the Subscription option yhen only it will work
we have to give permission for lambda fuction to do this, give permission for S3 access, cloudwatch access and SES and SNS access
create a role with access and assign that role with lambda function while creating the lambda function
