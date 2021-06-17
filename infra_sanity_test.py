import boto3
from botocore.exceptions import ClientError
from sys import argv
import requests

ENV = argv[1]
url = argv[2]


SENDER = "sachin.saini@cloverbaytechnologies.com"
RECIPIENT = "yogesh.p@cloverbaytechnologies.com"
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"


# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("\r\n"
            )
# The HTML body of the email.
try:
            request_response = requests.head(url, timeout=10)
            status_code = request_response.status_code
except:
            pass
else:
            if status_code == 200:
                SUBJECT = "Infra Sanity Check Passed"
                BODY_HTML = """<html>
                <head></head>
                <body>
                  <h3>Kupos React Application on {} URL $2 accessible and returned status code {}</h3>
                </body>
                </html>
                            """.format(url, status_code)            
            else:
                SUBJECT = "Infra Sanity Check Failed!"
                BODY_HTML = """<html>
                <head></head>
                <body>
                  <h3>Kupos React Application on {} URL $2 Not accessible and returned status code {}</h3>
                </body>
                </html>
                            """.format(url, status_code)             

            # Try to send the email.

            client = boto3.client('ses',region_name=AWS_REGION)
            try:
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            RECIPIENT,
                        ],
                    },
                    Message={
                        'Body': {
                            'Html': {
                                'Charset': CHARSET,
                                'Data': BODY_HTML,
                            },
                            'Text': {
                                'Charset': CHARSET,
                                'Data': BODY_TEXT,
                            },
                        },
                        'Subject': {
                            'Charset': CHARSET,
                            'Data': SUBJECT,
                        },
                    },
                    Source=SENDER,
                    #ConfigurationSetName=CONFIGURATION_SET,
                )

            except ClientError as e:
                print(e.response['Error']['Message'])
            else:
                print("Email sent! Message ID:"),
                print(response['MessageId'])
