import os
import json
import boto3
from botocore.exceptions import ClientError
import openai
import io
from openai import OpenAI
from PyPDF2 import PdfReader

# Set your OpenAI API key
client = OpenAI(api_key = API_KEY)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get the S3 bucket and key from the S3 event
        s3_bucket = event['Records'][0]['s3']['bucket']['name']
        s3_key = event['Records'][0]['s3']['object']['key']

        file_data = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        pdf = file_data['Body'].read()
        transcription = PdfReader(io.BytesIO(pdf))

        # Retrieve user query from the event
        user_query = event['user_query']

        response = get_openai_response(user_query)

        print(response)

        return {
        'statusCode': 200,
        'body': json.dumps('Transcription process completed successfully.')
        }

    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing query.')
        }

def get_openai_response(user_query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant. Base your answers on the given transcription."},
                {"role": "user", "content": transcription + user_query},
            ]
        )

        return response.choices[0].text.strip()

    except Exception as e:
        print(f'OpenAI Error: {str(e)}')
        raise e
