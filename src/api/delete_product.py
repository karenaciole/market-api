import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):

    dynamodb = boto3.client('dynamodb')
    product_id = event['pathParameters']

    try:
        dynamodb.delete_item(
            TableName='Products',
            Key={
                '_id': {
                    'S': product_id['_id']
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
        'body': 'Product with ID: ' + product_id['_id'] + ' deleted.'
    }
