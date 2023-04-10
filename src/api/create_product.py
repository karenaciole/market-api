import uuid
import boto3
from datetime import datetime

from botocore.exceptions import ClientError


def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')

    product = event["body"]
    item = {
        "_id": {"S": str(uuid.uuid4())},
        "name": {"S": product["name"]},
        "description": {"S": product["description"]},
        "category": {"S": product["category"]},
        "brand": {"S": product["brand"]},
        "price": {"N": product["price"]},
        "inventory": {
            "M": {
                "total": {"N": product["inventory"]["total"]},
                "available": {"N": product["inventory"]["available"]}
            },
        },
        "images": {
            "L": [
                {"S": image} for image in product["images"]
            ]
        },
        "created_at": {"S": str(datetime.now())},
        "updated_at": {"S": str(datetime.now())},
    }

    try:
        dynamodb.put_item(
            TableName='Products',
            Item=item
        )
    except ClientError as err:
        return err.response['ResponseMetadata']['HTTPStatusCode']

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': 'Product created with ID: ' + item["_id"]["S"]
    }
