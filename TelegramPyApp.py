import requests

class TelegramBot:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'

    def send_message(self, chat_id, message):
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(url, data=data)
        return response.json()

    def send_document(self, chat_id, file_path):
        url = f'{self.base_url}/sendDocument'
        files = {'document': open(file_path, 'rb')}
        data = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=data)
        return response.json()

    def get_updates(self, offset=None):
        url = f'{self.base_url}/getUpdates'
        params = {'offset': offset}
        response = requests.get(url, params=params)
        return response.json()
    def handle_updates(self, updates):
        for update in updates['result']:
            chat_id = update['message']['chat']['id']
            message_text = update['message']['text']
            if message_text == '/start':
                self.send_message(chat_id, 'Bot iniciado.')
             elif message_text == '/help':
                self.send_message(chat_id, 'Comandos disponibles: /start, /help, /sendfile')
            
            

# Uso de la clase
bot_token = 'tu_bot_token_aqui'
chat_id = 'tu_chat_id_aqui'
mensaje = 'mensaje'
archivo = 'ruta/al/archivo.xlsx'

bot = TelegramBot(bot_token, chat_id)

# Enviar mensaje
respuesta_mensaje = bot.send_message(mensaje)
print(respuesta_mensaje)

# Enviar archivo
respuesta_archivo = bot.send_document(archivo)
print(respuesta_archivo)
