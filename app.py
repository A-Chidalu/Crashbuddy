from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from twilio.rest import Client
from CarAccidentRecognition import get_result

app = Flask(__name__)

account_sid = 'AC05c0692e167c2f177d35ebb0a2662f84'
auth_token = 'fd2ee28ac05d4310c83d4ae68b5f6e8a'
client = Client(account_sid, auth_token)


@app.route("/sms", methods=['POST'])
def sms_reply():
    # Create a MessagingResponse object to generate TwiML.
    resp = MessagingResponse()

    # See if the number of images in the text message is greater than zero.
    if request.form['NumMedia'] != '0':

        # Grab the image URL from the request body.
        image_url = request.form['MediaUrl0']
        result = get_result(image_url)
        resp.message(result)

    else:
        resp.message('Please send an image.')

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
