# AWS Serverless API 

## Dependencies
|  Package   |  Version  |
| :--------: | :-------: |
|   python   | >= 3.8 |

## About

An AWS API using the Serverless Framework, Lambda functions, and DynamoDB for a CRUD system that manages market products. 

Each product must have the following schema, and you have to make sure the API doesn't allow different objects and that it returns the proper HTTP codes:

```json
Product object schema

{
  "_id": "string",
  "name": "string",
  "description": "string",
  "category": "string",
  "brand": "string",
  "price": "number",
  "inventory": {
    "total": "number",
    "available": "number"
  },
  "images": ["string"],
  "created_at": "Date",
  "updated_at": "Date"
}
```

## Deployment

In order to deploy the application to the AWS Cloud, simply run:

```
make build
make deploy
```

Please remove the resources and clean the stack by running:

```
make remove
make clean
```

## **Environment**


### Dependencies
|  Package   |  Version  |
| :--------: | :-------: |
|   serverless | latest |
|   boto3      | latest  |

### Setting up Serverless

1. Install ```serverless framework```: https://www.serverless.com/framework/docs/getting-started

### AWS
You are required to create an [AWS account](https://aws.amazon.com) if you don't have one yet.

### Dependencies
|  Package   |  Version  |
| :--------: | :-------: |
|   aws-cli   |  latest |

### Setting up AWS

1. Install ```aws-cli```: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2. Configure credentials on your local machine, by running:

```bash
$ aws configure
AWS Access Key ID [None]: <Your-Access-Key-ID>
AWS Secret Access Key [None]: <Your-Secret-Access-Key-ID>
Default region name [None]: us-west-1
Default output format [None]: json
```
View [CLI Config](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) for reference.

3. Create AWS credentials including the following IAM policies: ```AWSLambdaFullAccess```, ```AmazonS3FullAccess```, ```AmazonAPIGatewayAdministrator``` and ```AWSCloudFormationFullAccess```.

Run:
```sh
aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AWSLambdaFullAccess --user-name <username>

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name <username>

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator --user-name <username>

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AWSCloudFormationFullAccess --user-name <username>
```
