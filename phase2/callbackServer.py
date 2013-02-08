from bottle import request, route, run

import twilio.twiml
from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Twilio Account SID
token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Twilio Auth Token

fromNum = "+15005550006"  # Twilio number to call from
toNum = "+15005550009"  # Number to call (can be non-Twilio number)

dns = "twilio.webserver.com"  # replace with your webserver name
port = 8080
webserver = "http://" + dns + ":" + str(port) + "/"
smsReceivedCallback = webserver + "smsReceived"
callConnectedCallback = webserver + "callConnected"


@route('/smsReceived', method='POST')
def sms_received():
        # should probably do some sort of validation here
        words = request.forms.Body.split()
        callback = callConnectedCallback + "?playbackUrl=" + words[1]

        client = TwilioRestClient(account, token)
        call = client.calls.create(to=toNum, from_=fromNum, url=callback)

@route('/callConnected', method='POST')
@route('/callConnected', method='GET')  # useful for testing
def call_connected():
        # should probably do some sort of validation here too
        url = request.query.playbackUrl
        xml = '<?xml version="1.0" encoding="utf-8"?>\n'
        xml += '<Response><Play>' + url + '</Play></Response>'
        return xml

run(host=dns, port=port)