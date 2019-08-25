from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC05c0692e167c2f177d35ebb0a2662f84"
# Your Auth Token from twilio.com/console
auth_token = "fd2ee28ac05d4310c83d4ae68b5f6e8a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16479097033",
    from_="+12267967251",
    body="This is most likely a Large Hood Dent with a likelihood of 74%")

print(message.sid)