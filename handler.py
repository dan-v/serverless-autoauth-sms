import json
import urlparse

def auth(event, context):
    print(json.dumps(event))

    parsed = urlparse.urlparse("?" + event["body"])
    message = urlparse.parse_qs(parsed.query)['Body'][0]
    vpn_code = message[0:6]

    response_body = """<?xml version="1.0" encoding="UTF-8" ?>
    <Response>
        <Message>%s</Message>
    </Response>""" % vpn_code

    response = {
        "statusCode": 200,
        "body": response_body,
        "headers": {
            "Content-Type" : "text/xml"
        }
    }
    print(json.dumps(response))
    return response
