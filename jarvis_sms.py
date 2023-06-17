from twilio.rest import Client
import sms_k

def sms(body):
    client = Client(sms_k.account_sid, sms_k.auth_token)

    message = client.messages.create(
        body = body,
        from_ = sms_k.twilio_number,
        to = sms_k.my_phone_number
    )

    print(message.body)
    print('Message sent')

