## Member names:

Janam Vaidya

Rhythm Patel

Rishabh Pandat

## Member Tasks:

Janam:

Created a post api to facilitate upload of images from the user. That api is responsible for sending the message to the request queue and also for listening to the response from response queue.
Created the image upload flow for SQS and S3 bucket.
Contributed in creating shell files for automation.
Worked on report and documentation.

Rhythm:

Worked primarily on the app tier side of things. Responsible for decoding the image from the request queue and running the image classification model on the input image and again uploading the output to the S3 bucket and sending back the output in the response queue.
Created the download flow for SQS and S3 bucket.
Contributed in creating shell files for automation.
Worked on report and documentation.

Rishabh:

Responsible for setting up the necessary AWS infrastructure like S3, SQS, EC2 instances.
Testing and evaluation of the appliaction.
Worked on report and documentation.

## AWS Credentials

aws_access_key_id ='AKIASR4TXSHBVYMAGTE2'

aws_secret_access_key = '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'

## PEM Key

MIIEpQIBAAKCAQEAp5wv+ZV61kAdtLkjSb3rwTlYr+XEDtvQI2SpeTJp57xW1e9f
V1wwW5zGhM+FoF9LES5n75WslaybkVRJtmJlZMCYZ1dQJZKAfSjMynDaFHwX/t5rlgrG8foe+Fr68UNHtIHyiN7cNeteidfORM6g8Ciw51XaicxDNUXtyE1LlMQQL5Nh/7FO/ov+ayN+NwRUSSyNxyz95Jp+jiBczOWNH2IpdjDA24wxOoZRWM9sNL4j1HaWwogQGvmWp245e/97bW9d7vJqRc4fTE+43LeJuKjX1l+OXCPt9g2TFvJjLar3A4bfrsChuo61mND/8RbhZpfIGIcTDWGl0i+VXj2tIQIDAQABAoIBAQClKFBVvSe3aqJa7HuLNGvUkG+FlACnK45i8dPVKwoUYQ+n6yGlcZ/tBgTP5bUknAHaQkIEYRYYvmbkw4uG/lou92C1o+HDxCJ8MfHqIV2jBcyXRg/5X1E+K1rNGslfZw6HHe0hVYjkULNtXItSXdFUFKSMr5qSYgZvviJaV1/8i8WA6VWmYr+L5aX1V66rN43e5Xd3ru4XI2lFY4MsF5BPiIVtQ1t9pWpCbCyBL1nY2bcsTt7k4MkNAU8j6GWlKJMvquAGyObkbRJrdU/oei1DXfi59sXFRhhq5dCLZ8Fe3l++OzDLUqac2TIZLd/jWXp/wObxNXNRzLZwnRaTFrWJAoGBANW/cu3e7nmWZJ4KLmMRe6/b+CT78OjeYDUgUGWgIWoV76flAPPoaENrhaBhvza9nMq5OfebOpu6XafnwXvb7d/Mts1z5hDMEfPA88X50FwfhCYxaWTG6z7lLax3k8vg/iAnSKGa7n+Hiv2Pte06NoalrfjXp2Br5+/c2FRcLkTfAoGBAMi9+O2n0dmrdg73ThglZ/D3LWQqxTJb74U6zEbPKyQYT0rUkSqObiWkGbWpR0R5Fx7PDXuMT8Uc8l4PAA3Yt1+b4F/DEvSEmuIiHFuMyNJByIqzSkila29LPBARPm4sJV1GpX1sXAQ/bmA4GvtODLTg8khDm4kGh9idtcuckE3/AoGASeiSD+gm44n6Lp9snLrd3tgbvIYVLiA+egA7bHhrNWhyXsaThsMU0kMqiGNkH8R+o6ZageB96n0Nh1Jel7pbTShXCUGLCsHVb0iHwiv4PPJ02lP5kmwpyayrF1idlUCt/mY2+hI9Z4FxsO1xRZ78XaCKQGIpMPD+2PSvJLRfF1cCgYEAmrRlgmpCPLl6W6BV7B/v0fH8ZmTb4qqdlhSxV6TTP5cIjMfzNFPeKV4lfi3+QZP8sH6rilqhI2zikICI7yLkd2d+7O4+znjfkITvS9Lc9cVC0znHduMdQAFAQbW4YlndVdxbL6Tx6UglPTwf9yq4ejGeJvkLhfele9hXQZrgT2sCgYEAuO3RTSRqzODj40XLqBx+N8Q33cjf4p5cWn0AyExP89ZZ9C+eKN+67pNO6Eo/Dqq2FgSZclZC07yYC0U7r2CvNPw+FLguj/Np/Evz+ENfe2Vl084JK6hXBwokrRKr3/iKms34ak8mwxs3GY8TQ0OaZOUsWu7y+dITEpDxhhFHyMk=

## Additional Details

region_name = 'us-east-1'

request_queue_url = 'https://sqs.us-east-1.amazonaws.com/175866614211/p1_input_queue'

response_queue_url = 'https://sqs.us-east-1.amazonaws.com/175866614211/p1_output_queue'

s3_input_bucket = "cse546-p1-input"

s3_output_bucket = "cse546-p1-output"

## Steps to reproduce code

1. We have kept a shell file in web tier ec2 instance to run the webv2.py file. So this is the starting point of our application. This particular file has the post api that the user will use to send user requests. So we need to execute this file by the command sh autoweb.sh. Basically running webv2.py file.

2. We have also created a shell file to run the controller.py file which handles the scale in scale out approach of our application.

3. To run only the app tier ssh or login to the instance and run cd /home/ubuntu/classifier and then followed by python3 index.py
