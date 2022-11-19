import os
import boto3
from flask import Flask, request, jsonify
import base64

app = Flask(__name__)
res = dict()
aws_access_key_id ='AKIARTA6RNMBL5FC5ELP'
aws_secret_access_key = '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'
region_name = 'us-east-1'
request_queue_url = 'https://sqs.us-east-1.amazonaws.com/109585722114/cse-546-p1-input'
response_queue_url = 'https://sqs.us-east-1.amazonaws.com/109585722114/cse-546-p1-output'
endpoint_url = 'https://sqs.us-east-1.amazonaws.com'
sqs = boto3.resource('sqs', aws_access_key_id= aws_access_key_id, aws_secret_access_key=aws_secret_access_key, endpoint_url=endpoint_url, region_name=region_name)
sqs_client = boto3.client('sqs', aws_access_key_id= aws_access_key_id, aws_secret_access_key=aws_secret_access_key, endpoint_url=endpoint_url, region_name=region_name)
s3 = boto3.resource(
        service_name='s3',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

@app.route("/upload")
def showHomePage():
    return "This is home page"

@app.route('/', methods=["GET", "POST"])
def upload_the_image():
    cnt = 0
    output = None
    print(request.files)
    if 'myfile' in request.files:
        # print( request.files)
        image = request.files['myfile']
        # image1 = request.files['myfile']
        print(image)
        im = image.read()
        f_name = str(image).split(" ")[1][1:][:-1]
        
        print(f_name)
        if f_name != '':
            f_extension = os.path.splitext(f_name)[1]
            print(f_extension)
            byteform=base64.b64encode(im)
            value = str(byteform, 'ascii')
            str_byte=f_name.split('.')[0] + " " + value
            print(str_byte)
            print(sqs_client.send_message)
            resp = sqs_client.send_message(
                QueueUrl=request_queue_url,
                MessageBody=str_byte,
            )
            
            print(resp)
            print(f_name.split('.')[0])
            # return 'rhythm'
            try:
                output  = get_correct_response(f_name.split('.')[0])
                print("OUTPUT")
                print(output)
                return output

            except Exception as e:
                print(str(e))
                return "Something went wrong! x"
        else :
            return "Error with file name"
    else:
        return "File should be of type Image"

    # return jsonify("Something went wrong 2")

def get_number_of_msgs_in_res_queue() :
    response = sqs.get_queue_attributes(
            QueueUrl=response_queue_url,
            AttributeNames=[
                'ApproximateNumberOfMessages',
                'ApproximateNumberOfMessagesNotVisible'
            ]
        )

    return int(response['Attributes']['ApproximateNumberOfMessages'])

def get_correct_response(image) :
    result = ""

    print("BEFORE")

    while True:

        if image in res.keys():
            return res[image]

        response = sqs_client.receive_message(
            QueueUrl=response_queue_url,
            MaxNumberOfMessages=10,
            MessageAttributeNames=[
                'All'
            ],
        )


        if 'Messages' in response:
            msgs = response['Messages']
            print('RHYT')
            print(image)
            for msg in msgs:
                msg_body = msg['Body']
                res_image = msg_body.split(" ")[0]
                print("RES IMG")
                print(res_image.split(".")[0])

                res[res_image] = msg_body.split(" ")[1]

                receipt_handle = msg['ReceiptHandle']
                # print(receipt_handle)
                print(msg_body.split(" ")[1])
                sqs_client.delete_message(
                    QueueUrl = response_queue_url,
                    ReceiptHandle = receipt_handle
                )
                
                print("??")
                print(res_image.split(".")[0])
                print(image)
                if res_image.split(".")[0] == image :
                    return res[res_image]


if __name__ == "__main__":
    print("hello")
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4000)))
