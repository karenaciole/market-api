import boto3
from datetime import datetime

from botocore.exceptions import ClientError


def update_data(request_body):
    """
    This function updates the product data removing the keys that are not allowed to be updated
    and removing the None values
    """

    body = {
        "_id": request_body.get("_id"),
        "name": request_body.get("name"),
        "description": request_body.get("description"),
        "category": request_body.get("category"),
        "brand": request_body.get("brand"),
        "price": request_body.get("price"),
        "images": request_body.get("images"),
        "created_at": request_body.get("created_at"),
        "updated_at": str(datetime.now())
    }

    not_allowed_keys = ["_id", "created_at"]

    if len(request_body.get('inventory', {})) == 0:
        request_body.pop('inventory', None)

    return {k: v for k, v in body.items() if v is not None and k not in not_allowed_keys}


def update_expression(update_product):
    """
    This function creates the update expression, expression attribute names and values for the dynamodb update_item
    method
    """

    update_expression_parts = []
    expression_attribute_names = {}
    expression_attribute_values = {}

    for attribute_name, attribute_value in update_product.items():
        update_expression_parts.append(f"#{attribute_name} = :{attribute_name}")
        expression_attribute_names[f"#{attribute_name}"] = attribute_name
        expression_attribute_values[f":{attribute_name}"] = {"S": attribute_value}

    expression = "SET " + ", ".join(update_expression_parts)

    return expression, expression_attribute_names, expression_attribute_values


def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')

    product = update_data(event["body"])

    expression, expression_attribute_names, expression_attribute_values = update_expression(product)

    try:
        response = dynamodb.update_item(
            TableName='Products',
            Key={'_id': {"S": event['body']['_id']}},
            UpdateExpression=expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names,
            ReturnValues="UPDATED_NEW"
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
        'body': response['Attributes']
    }
