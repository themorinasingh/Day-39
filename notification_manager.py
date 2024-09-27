from twilio.rest import Client
ACCOUNT_SID = 'AC5b1ea9d6587975328c87032bca2bac81'
AUTH_TOKEN = '0f22f3f32e75b42978f7707071f82688'

class NotificationManager:
    def __init__(self):
        self.message = ""

    def message_maker(self, flight_price, from_iata, to_iata, from_date, to_date):
        message = f'Low Price Alert! \nOnly {flight_price} to fly from {from_iata} to {to_iata}. On {from_date} until {to_date}'
        self.message = message

    def send_msg(self, flight_price, from_iata, to_iata, from_date, to_date):
        self.message_maker(flight_price, from_iata, to_iata, from_date, to_date)

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            from_='+12076790712',
            body = self.message,
            to = '+15062694986'
        )


