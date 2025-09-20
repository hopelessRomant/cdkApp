# AWS CDK Tutorial: Deploying a Simple Lambda Application

## About this Tutorial

In this tutorial, you will create and deploy a simple application on AWS using the **AWS CDK**.  
The application consists of an **AWS Lambda function** that returns a `Hello World!` message when invoked.  
The function will be invoked through a **Lambda Function URL** that serves as a dedicated HTTP(S) endpoint for your Lambda function.

---

## Tutorial Steps

Through this tutorial, you will perform the following:

1. **Create your project**  
   Create a CDK project using the CDK CLI `cdk init` command.

2. **Configure your AWS environment**  
   Configure the AWS environment that you will deploy your application into.

3. **Bootstrap your AWS environment**  
   Prepare your AWS environment for deployment by bootstrapping it using the CDK CLI `cdk bootstrap` command.

4. **Develop your app**  
   Use constructs from the AWS Construct Library to define your Lambda function and Lambda function URL resources.

5. **Prepare your app for deployment**  
   Use the CDK CLI to build your app and synthesize an AWS CloudFormation template.

6. **Deploy your app**  
   Use the CDK CLI `cdk deploy` command to deploy your application and provision your AWS resources.

7. **Interact with your application**  
   Interact with your deployed Lambda function on AWS by invoking it and receiving a response.

8. **Modify your app**  
   Modify your Lambda function and deploy to implement your changes.

9. **Delete your app**  
   Delete all resources that you created by using the CDK CLI `cdk destroy` command.
