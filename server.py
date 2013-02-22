import os

from bottle import request, route, run, view

import twilio.twiml
from twilio.rest import TwilioRestClient

host = "localhost"
port = 8080
dns = "localhost"

# Only set these if not setting the environment variables
# To find these visit https://www.twilio.com/user/account
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Twilio Account SID
token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Twilio Auth Token
twilioNumber = "+15005550006"  # Twilio number to call from

onHeroku = False
if 'PORT' in os.environ:
    onHeroku = True
    port = os.environ.get("PORT", 5000)

if 'HOST' in os.environ:
    onHeroku = True
    host = os.environ.get("HOST", "0.0.0.0")

if "DNS" in os.environ:
    onHeroku = True
    dns = os.environ.get("DNS", "www.example.com")

if "TWILIO_ACCT" in os.environ:
    onHeroku = True
    account = os.environ.get("TWILIO_ACCT", "nothing")

if "TWILIO_TOKEN" is os.environ:
    onHeroku = True
    token = os.environ.get("TWILIO_TOKEN", "none")

if "TWILIO_NUMBER" is os.environ:
    onHeroku = True
    twilioNumber = os.environ.get("TWILIO_NUMBER", "+15005550006")


webserver = "http://" + dns + ":" + str(port) + "/"
smsReceivedCallback = webserver + "smsReceived"
callConnectedCallback = webserver + "callConnected"

@route('/')
@view('smsForm')
def index():
    return {"froms":[{"number":twilioNumber}],"message":None}
    
@route('/smsSend', method='POST')
@view('smsForm')
def sms_send():
    postData = request.forms
    toNum = postData.toNum
    fromNum = postData.fromNum
    body = postData.body
    client = TwilioRestClient(account, token)
    message = client.sms.messages.create(to=toNum, from_=fromNum, body=body)
    return {"froms":[{"number":fromNum}],"message":"text message was sent"}

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

run(host=host, port=port)