import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    url = f'https://{bucket}.s3.amazonaws.com/{key}'

    response = dynamodb.update_item(
        Table='string',
        Key={
            '_id': '_id'    # tip: set post _id as object metadata in S3
        },
        UpdateExpression='SET medias = medias + :media',
        ExpressionAttributeValues={
            ':media': [url]
        },
        ReturnValues='UPDATED_NEW'
    )

    return dict()