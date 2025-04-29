# S3cloudwatch
# AWS Lambda S3 Trigger: Log Events to CloudWatch
 Triggered on `ObjectCreated` events in S3
 Python-based Lambda function
 Logs full event payload to CloudWatch
 Uses default IAM role with CloudWatch permissions

 #Prerequisites
  - AWS account with access to:
  - S3
  - Lambda
  - IAM
  - CloudWatch

### 1. Create an S3 Bucket

- Go to AWS Console > S3 > Create Bucket
- Name it something like `my.lambda.s3.bucket.1`
- Leave default settings

### 2. Create the Lambda Function

- Go to AWS Console > Lambda > Create Function**
- Choose Author from scratch
- Name: LogS3EventFunction
- Runtime: `Python 3.12` (or similar)
- Permissions: Choose Create new role with basic Lambda permissions
- Click Create function

### 3. Add Code
Click Deploy after adding code.

### 4. Add S3 Trigger
In the Lambda function, scroll to Triggers → Add trigger
Choose:
Trigger: S3
Bucket:my.lambda.s3.bucket.1 
Event type: PUT (Object Created)
Click Add

### 5. Test the Flow
Upload any file to the S3 bucket.
Go to CloudWatch > Log Groups > /aws/lambda/LogS3EventFunction
Open the latest stream to see event details logged.

