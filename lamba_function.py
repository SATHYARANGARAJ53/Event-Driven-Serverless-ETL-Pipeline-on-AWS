import json
import boto3

def lambda_handler(event, context):
    # print(event)
    # print("Lambda triggered")
    glue = boto3.client("glue")
    job_name = 'ETL_Pipeline_Demo'
    
    try:
        response = glue.start_job_run(JobName=job_name)
        print("Success: " + str(response))
    except Exception as e:
        return{
            'statusCode': 500,
            'body': f"Failed to start glue job: {str(e)}"
        }
