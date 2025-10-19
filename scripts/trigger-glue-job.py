import boto3
import json

def lambda_handler(event, context):
    glue = boto3.client('glue')
    
    # Replace with your Glue job name
    job_name = 'Data Manipulation'
    
    # Optional: Print event info to CloudWatch for debugging
    print("Event: ", json.dumps(event))
    
    # Start Glue job
    response = glue.start_job_run(JobName=job_name)
    
    print("Glue job started:", response['JobRunId'])
    
    return {
        'statusCode': 200,
        'body': f"Glue job {job_name} started successfully."
    }
