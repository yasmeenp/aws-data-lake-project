import boto3
import pandas as pd
from io import StringIO

# ---------- CONFIG ----------
s3 = boto3.client('s3')
source_bucket = 'yasmeen-youtube-raw'
destination_bucket = 'yasmeen-youtube-processed'
USD_TO_INR = 83.0

# ---------- LIST ALL CSV FILES ----------
response = s3.list_objects_v2(Bucket=source_bucket, Prefix='')
if 'Contents' in response:
    for obj in response['Contents']:
        file_key = obj['Key']
        if file_key.endswith('.csv'):
            # Read CSV
            csv_obj = s3.get_object(Bucket=source_bucket, Key=file_key)
            csv_data = csv_obj['Body'].read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))

            # Transform: convert USD to INR
            df['revenue_inr'] = df['revenue_usd'] * USD_TO_INR

            # Write transformed CSV back to S3
            output_key = f"processed/{file_key}"
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            s3.put_object(Bucket=destination_bucket, Key=output_key, Body=csv_buffer.getvalue())

            print(f"✅ Transformed file uploaded to s3://{destination_bucket}/{output_key}")
else:
    print("⚠️ No CSV files found in raw bucket")
