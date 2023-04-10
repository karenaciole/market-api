import boto3
from botocore.exceptions import ClientError


def format_response(product):
    return {
        "_id": product["_id"]["S"],
        "name": product["name"]["S"],
        "description": product["description"]["S"],
        "category": product["category"]["S"],
        "brand": product["brand"]["S"],
        "price": product["price"]["N"],
        "inventory": {
            "total": product["inventory"]["M"]["total"]["N"],
            "available": product["inventory"]["M"]["available"]["N"]
        },
        "images": [image["S"] for image in product["images"]["L"]],
        "created_at": product["created_at"]["S"],
        "updated_at": product["updated_at"]["S"]
    }


def lambda_handler(event, context):

    dynamodb = boto3.client('dynamodb')

    try:
        product = dynamodb.get_item(
            TableName='Products',
            Key={
                '_id': {
                    'S': event['pathParameters']['_id']
                }
            }
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
        'body': format_response(product['Item'])
    }
