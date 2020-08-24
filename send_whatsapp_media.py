from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "SOME_AUTH_SID"
# Your Auth Token from twilio.com/console
auth_token = "SOME_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=SOME_NUMBER,
    from_="+12267967251",
    body="This is most likely a Large Hood Dent with a likelihood of 74%")

print(message.sid)
