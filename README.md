# 🚀 AWS Event-Driven ETL Pipeline (S3 → Lambda → Glue → Athena)

## 📘 Overview
This project demonstrates a **real-world, event-driven ETL pipeline** built entirely on AWS.  
When a new CSV file is uploaded to an S3 bucket, a Lambda function automatically triggers an AWS Glue Python Shell job that cleans and transforms the data, writes it back to another S3 bucket, and makes it queryable via AWS Athena.

---

### **Data Flow**
1. **S3 (Raw Bucket)** – Stores raw CSV uploads  
2. **Lambda** – Automatically triggered on new file uploads  
3. **Glue (Python Shell)** – Processes and transforms the data  
4. **S3 (Processed Bucket)** – Stores transformed output  
5. **Glue Crawler** – Updates schema in Glue Data Catalog  
6. **Athena** – Executes SQL queries on processed data  

---

## 🧩 AWS Services Used

| Layer | Service | Purpose |
|-------|----------|----------|
| Storage | **Amazon S3** | Raw & processed data layers |
| Trigger | **AWS Lambda** | Triggers Glue job on file upload |
| ETL | **AWS Glue (Python Shell)** | Runs data transformation code |
| Metadata | **AWS Glue Crawler** | Updates Athena schema |
| Query | **Amazon Athena** | SQL querying on processed data |
| Monitoring | **Amazon CloudWatch** | Logs for Lambda & Glue |


