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
            elif message_text == '/Ayuda':
                self.send_message(chat_id, 'Hola! Comandos disponibles: /start, /Ayuda, /archivo')
            elif message_text == '/archivo':
                # Ruta del archivo a enviar 
                file_path = 'ruta/al/archivo.xlsx'
                self.send_document(chat_id, file_path)
            else:
                self.send_message(chat_id, f'Comando no reconocido, por favor utilice uno de los comandos disponibles: {message_text}')

# Uso de la clase
bot_token = 'bot_token_aqui'
bot = TelegramBot(bot_token)

# Bucle para recibir y manejar actualizaciones
offset = None
while True:
    updates = bot.get_updates(offset)
    if updates['result']:
        bot.handle_updates(updates)
        # Actualizar el offset para obtener solo nuevos mensajes
        offset = updates['result'][-1]['update_id'] + 1
