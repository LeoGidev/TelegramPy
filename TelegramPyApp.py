import requests

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'

    def send_message(self, message):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': message
        }
        response = requests.post(url, data=data)
        return response.json()

    def send_document(self, file_path):
        url = f'{self.base_url}/sendDocument'
        files = {'document': open(file_path, 'rb')}
        data = {'chat_id': self.chat_id}
        response = requests.post(url, files=files, data=data)
        return response.json()

# Uso de la clase
bot_token = 'tu_bot_token_aqui'
chat_id = 'tu_chat_id_aqui'
mensaje = 'Resultado de la prueba'
archivo = 'ruta/al/archivo.xlsx'

bot = TelegramBot(bot_token, chat_id)

# Enviar mensaje
respuesta_mensaje = bot.send_message(mensaje)
print(respuesta_mensaje)

# Enviar archivo
respuesta_archivo = bot.send_document(archivo)
print(respuesta_archivo)
