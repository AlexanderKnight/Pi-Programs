#! python3
#textMyself.py - Defines the textmyself() function that texts a message
#passed to it as a string.

# Preset values:
accountSID = 'AC022c6c0b127b2d0ccc8ede2bfd865629'
authToken = 'f0bf6398299428bc21a476add09112e8'
myNumber = '+12072549233'
twilioNumber = '+12076186375'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

