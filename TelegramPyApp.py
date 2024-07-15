import requests

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'

# URL base de la API de Telegram
url = f'https://api.telegram.org/bot{BOTTOKEN}/sendMessage'

# Datos a enviar en la solicitud POST
data = {
    'chat_id': CHATID,
    'text': mensaje
}

# Enviar el mensaje
response = requests.post(url, data=data)

# Imprimir la respuesta para verificar si se envió correctamente
print(response.json())
