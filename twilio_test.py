from twilio.rest import TwilioRestClient 

account_sid = 'AC3890c333f557809720e9a37e80a1236d'
auth_token = 'c8e36f595009dbbcfcd6a649e6cc67de'

client = TwilioRestClient(account_sid, auth_token) 
 
client.messages.create(
  to="7815261943", 
  from_="+17818195644",
  body="Hi Mike!"
)