# Event-Driven Serverless ETL Pipeline on AWS
2
 
3
## Project Goal
4
 
5
To build an automated, event-driven ETL pipeline using AWS services that processes files uploaded to Amazon S3, performs data transformations with AWS Glue, and provides real-time monitoring and notifications.
6
 
7
## About the Project
8
 
9
This project demonstrates a serverless ETL workflow built using AWS managed services. When a file is uploaded to Amazon S3, an AWS Lambda function is automatically triggered to start an AWS Glue ETL job. The transformed data is stored in S3, while EventBridge tracks job events and Amazon SNS sends email notifications on job completion or failure. Amazon CloudWatch is used for monitoring and logging the entire workflow.
10
 
11
## Architecture Flow
12
 
13
S3 → Lambda → AWS Glue → EventBridge → SNS → Email Notifications
14
 
15
CloudWatch is used for monitoring and logging across the pipeline.
16
 
17
## Tech Stack Used
18
 
19
### AWS Services
20
- Amazon S3
21
- AWS Lambda
22
- AWS Glue
23
- Amazon EventBridge
24
- Amazon SNS
25
- Amazon CloudWatch
26
 
27
### Programming Language
28
- Python
29
 
30
### Concepts
31
- ETL (Extract, Transform, Load)
32
- Serverless Computing
33
- Event-Driven Architecture
34
- Monitoring & Logging
35
- Workflow Automation
36
 
37
## Key Features
38
 
39
- Automated ETL processing
40
- Event-driven architecture
41
- Serverless implementation
42
- Real-time email notifications
43
- Centralized monitoring and logging
44
- Scalable and cost-effective workflow
45
 
46
## What I Gained
47
 
48
- Hands-on experience with AWS serverless services.
49
- Practical understanding of ETL workflow implementation using AWS Glue.
50
- Experience integrating S3, Lambda, Glue, EventBridge, SNS, and CloudWatch.
51
- Knowledge of event-driven data processing architectures.
52
- Skills in monitoring, troubleshooting, and logging cloud-based workflows.
53
- Experience building automated data pipelines in AWS.
