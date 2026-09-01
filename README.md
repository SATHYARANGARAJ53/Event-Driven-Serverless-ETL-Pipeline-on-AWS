# 🚀 Event-Driven Serverless ETL Pipeline on AWS

## 📌 Project Overview

This project demonstrates an end-to-end serverless ETL pipeline built using AWS services. The solution automatically processes data uploaded to Amazon S3, triggers ETL operations using AWS Glue, tracks workflow events through Amazon EventBridge, sends notifications using Amazon SNS, and provides monitoring and logging through Amazon CloudWatch.

The pipeline follows an event-driven architecture, enabling scalable and automated data processing without managing servers.

---

## 🎯 Project Goal

To design and implement an automated ETL workflow that:

- Ingests data into Amazon S3
- Triggers processing automatically using AWS Lambda
- Performs data transformation using AWS Glue
- Tracks service events with Amazon EventBridge
- Sends real-time notifications through Amazon SNS
- Monitors pipeline execution using Amazon CloudWatch

---

## 🏗️ Architecture

```text
                  +-------------+
                  |   Amazon S3 |
                  +-------------+
                         |
                         | File Upload Event
                         ▼
                  +-------------+
                  | AWS Lambda  |
                  +-------------+
                         |
                         | Start ETL Job
                         ▼
                  +-------------+
                  | AWS Glue    |
                  +-------------+
                         |
                         | Job State Events
                         ▼
                  +-------------+
                  | EventBridge |
                  +-------------+
                         |
                         ▼
                  +-------------+
                  | Amazon SNS  |
                  +-------------+
                         |
                         ▼
                Email Notifications

            CloudWatch monitors all services
```

---

## 🔄 Workflow

1. Upload a CSV file to an Amazon S3 bucket.
2. S3 event notification triggers an AWS Lambda function.
3. Lambda starts an AWS Glue ETL job.
4. AWS Glue reads, transforms, and writes processed data to S3.
5. EventBridge captures Glue Job State Change events.
6. SNS sends email notifications for job success or failure.
7. CloudWatch stores logs and metrics for monitoring and troubleshooting.

---

## 🛠️ Tech Stack

### AWS Services

- Amazon S3
- AWS Lambda
- AWS Glue
- Amazon EventBridge
- Amazon SNS
- Amazon CloudWatch

### Programming Language

- Python

### Core Concepts

- ETL (Extract, Transform, Load)
- Serverless Computing
- Event-Driven Architecture
- Data Transformation
- Cloud Monitoring & Logging
- Workflow Automation

---

## ✨ Key Features

- Fully serverless ETL workflow
- Automated data processing
- Event-driven architecture
- Real-time email notifications
- Centralized logging and monitoring
- Scalable and cost-efficient solution
- Minimal operational overhead

---

## 📚 What I Learned

Through this project, I gained hands-on experience in:

- Building serverless data pipelines using AWS services
- Configuring S3 event triggers and Lambda integrations
- Creating and executing AWS Glue ETL jobs
- Implementing event-driven workflows using EventBridge
- Configuring SNS for automated notifications
- Monitoring and troubleshooting services with CloudWatch
- Managing IAM permissions and service integrations
- Understanding real-world cloud data engineering workflows

---

## 🎓 Skills Demonstrated

- AWS Cloud Services
- Data Engineering Fundamentals
- ETL Pipeline Development
- Serverless Architecture
- Event-Driven Design
- Cloud Monitoring & Observability
- Python Scripting
- AWS IAM and Security

---

## 👨‍💻 Author

**Sathya Rangaraj**  
Associate Engineer - Data & AI

LinkedIn: *Add Your Profile Link*  
GitHub: *Add Your GitHub Profile Link*
