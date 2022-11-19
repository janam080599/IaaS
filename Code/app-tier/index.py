import base64
from urllib import response
import boto3
from botocore.exceptions import ClientError
import os
import time
import datetime
import logging  
import io
aws_access_key_id ='AKIARTA6RNMBL5FC5ELP'
aws_secret_access_key = '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'
region_name = 'us-east-1'
request_queue_url = 'https://sqs.us-east-1.amazonaws.com/109585722114/cse-546-p1-input'
response_queue_url = 'https://sqs.us-east-1.amazonaws.com/109585722114/cse-546-p1-output'
endpoint_url = 'https://sqs.us-east-1.amazonaws.com'
s3_input_bucket = "cse-546-p1-input"
s3_output_bucket = "cse-546-p1-output"
sqs = boto3.client('sqs', aws_access_key_id= aws_access_key_id, aws_secret_access_key=aws_secret_access_key, endpoint_url=endpoint_url, region_name=region_name)
s3_client = boto3.client('s3', aws_access_key_id= aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
s3 = boto3.resource(
    service_name='s3',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )
# Create a logging instance
logger = logging.getLogger('my_application')

# Assign a file-handler to that instance
fh = logging.FileHandler("index_logger.txt")
fh.setLevel(logging.INFO) # again, you can set this differently

# Add the handler to your logging instance
logger.addHandler(fh)

def receiveMessages() :
    print("in receive messages")
    try:
        response = sqs.receive_message(
            QueueUrl=request_queue_url,
                AttributeNames=[
                'SentTimestamp'
                ],
                MaxNumberOfMessages=10,
                MessageAttributeNames=[
                'All'
                ],
                VisibilityTimeout=30,
                # WaitTimeSeconds=20
            )


        # print("resp")
        # print(response)

    except Exception as e:
        print(str(e))
        return "Something went wrong"



    if 'Messages' in response :
        reciept_handle = response['Messages'][0]['ReceiptHandle']
        rr = response['Messages']

        print("rr")
        print(rr)
        deleteMessage(reciept_handle)
        return rr
    else :
        time.sleep(1)
        return receiveMessages()

def deleteMessage(receipt_handle) :
    sqs.delete_message(
        QueueUrl = request_queue_url,
        ReceiptHandle = receipt_handle
    )

def decodeMessage(fName, msg) :
    decodeit=open(fName,'wb')
    decodeit.write(base64.b64decode((msg)))
    decodeit.close()

def sendMessageInResponseQueue(fName, msg) :
    endpoint_url = 'https://sqs.us-east-1.amazonaws.com'
    resp = sqs.send_message(
    QueueUrl = response_queue_url,
        MessageBody=(
        fName + " " + msg
        )
    
    )
    
def upload_to_s3_input_bucket(file_name, bucket, object_name) :
    try:
        response = s3_client.upload_fileobj(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def upload_to_s3_output_bucket(s3, bucket_name, image_name, predicted_result) :
    content = (image_name, predicted_result)
    content = ' '.join(str(x) for x in content)
    s3.Object(s3_output_bucket, image_name).put(Body=content)

def initialize() :

    val = receiveMessages()
    
    if(val == None or len(val) == 0):
        print('here in none condition')
        return
    
    message = val[0]
    print(message)
    
    fName , encodedMssg=message['Body'].split()
    fName = fName + ".jpeg"
    img_file_name = fName
    logging.info('file name : ' + fName)
    outputFile = fName

    print("message body")
    print(message['Body'])

    print("fileName here")
    print(fName)

    msg_value = bytes(encodedMssg, 'ascii')
    qp = base64.b64decode(msg_value)
    print(qp)
    with open(fName, "wb") as fff:
        fff.write(qp)

    with open(fName, 'rb') as f:
        if upload_to_s3_input_bucket(f, s3_input_bucket, fName):
            logging.info("input file uploaded in S3 bucket")
            print("input file uploaded in S3 bucket")

    stdout = os.popen(f'python3 image_classification.py "{fName}"')
    result = stdout.read().strip()
    logging.info('result : ' + result)
    print("result " + result)

    with open(fName, 'rb') as f:
        upload_to_s3_output_bucket(s3, s3_output_bucket, img_file_name, result)
        sendMessageInResponseQueue(img_file_name, result)

    print(result)
    
    

logging.info('Timestamp : ' + str(datetime.datetime.now()))
while True :
    initialize()
