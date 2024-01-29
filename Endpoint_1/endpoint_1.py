# Import necessary libraries
import os
import json
import boto3
from botocore.exceptions import ClientError
import openai
import pydub
import whisper
import io
from fpdf import FPDF
from openai import OpenAI
from pydub import AudioSegment

s3 = boto3.client('s3')
client = OpenAI(api_key=API_KEY)

def lambda_handler(event, context):
    try:
        # Get the S3 bucket and key from the S3 event
        s3_bucket = event['Records'][0]['s3']['bucket']['name']
        s3_key = event['Records'][0]['s3']['object']['key']
        print("BUCKET", s3_bucket)
        print("KEY", s3_key)

        # Ensure the file type is valid
        if s3_key.lower().endswith(('.mp4', '.mp3', '.wav', '.mpeg', '.mpga', '.m4a', '.webm')):
            # Download the audio file from S3
            file_object = s3.get_object(Bucket=s3_bucket, Key=s3_key)
            print("FILE OBJECT", file_object)
            audio_content = file_object['Body'].read()

            audio = AudioSegment.from_file(io.BytesIO(audio_content), format="mp3")

            # Transcribe using OpenAI Whisper
            transcription = transcribe_audio(audio)

            # Convert transcription to PDF
            pdf_path = create_pdf(transcription)

            # Upload PDF to another S3 bucket
            target_s3_bucket = 'transcribed-text-files'
            target_s3_key = 'transcriptions/' + os.path.basename(s3_key) + '.pdf'
            upload_to_s3(pdf_path, target_s3_bucket, target_s3_key)

            # Log or process the transcription result as needed
            print(f'Transcription result: {transcription}')

        else:
            print(f'Skipping file {s3_key}. Not a supported audio format.')

        return {
            'statusCode': 200,
            'body': json.dumps('Transcription process completed successfully.')
        }

    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps('Error during transcription process.')
        }

def transcribe_audio(audio_file):

    model = whisper.load_model("medium")
    response = model.transcribe(audio_file)

    # Retrieve the transcription
    transcription = response['text']
    return transcription

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf_path = '/tmp/transcription.pdf'
    pdf.output(pdf_path)
    return pdf_path

def upload_to_s3(local_path, bucket, key):
    s3 = boto3.client('s3')
    s3.upload_file(local_path, bucket, key)
