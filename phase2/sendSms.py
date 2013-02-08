from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Twilio Account SID
token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Twilio Auth Token

fromNum = "+15005550006"  # Twilio number to send SMS from
toNum = "+15005550009"  # Number to send SMS to (can be non-Twilio number)

message = "CALLME"

client = TwilioRestClient(account, token)

message = client.sms.messages.create(to=toNum, from_=fromNum, body=message)