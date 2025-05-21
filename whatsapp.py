from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def enviar_whatsapp(mensagem):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    message = client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        body=mensagem,
        to=os.getenv("TWILIO_WHATSAPP_TO")
    )

    print(f"Mensagem enviada com SID: {message.sid}")