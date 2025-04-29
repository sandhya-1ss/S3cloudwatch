import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    This Lambda function logs S3 event details to CloudWatch Logs.
    """
    logger.info("Received event: " + json.dumps(event, indent=2))
    
    # Extract some useful details
    for record in event.get('Records', []):
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        logger.info(f"New object created: Bucket = {bucket_name}, Key = {object_key}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Event logged successfully!')
    }
