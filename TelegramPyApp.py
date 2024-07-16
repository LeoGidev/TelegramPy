import requests
import pandas as pd

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

    def get_updates(self, offset=None):
        url = f'{self.base_url}/getUpdates'
        params = {'offset': offset}
        response = requests.get(url, params=params)
        return response.json()

    def handle_updates(self, updates, excel_handler):
        for update in updates['result']:
            chat_id = update['message']['chat']['id']
            message_text = update['message']['text']

            if message_text == '/start':
                self.send_message('Bot iniciado.')
            elif message_text == '/help':
                self.send_message('Comandos disponibles: /start, /help, /sendfile, /createexcel')
            elif message_text == '/sendfile':
                # Ruta del archivo que quieres enviar
                file_path = 'ruta/al/archivo.xlsx'
                self.send_document(file_path)
            elif message_text == '/createexcel':
                # Crear un archivo Excel con datos de ejemplo
                file_path = 'ruta/al/nuevo_archivo.xlsx'
                excel_handler.create_sample_excel(file_path)
                self.send_document(file_path)
            else:
                self.send_message(f'Comando no reconocido: {message_text}')

class ExcelHandler:
    def create_sample_excel(self, file_path):
        data = {
            'Nombre': ['Juan', 'Ana', 'Luis'],
            'Edad': [28, 22, 35],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
        }
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)

# Uso de las clases
bot_token = 'tu_bot_token_aqui'
chat_id = 'tu_chat_id_aqui'
bot = TelegramBot(bot_token, chat_id)
excel_handler = ExcelHandler()

# Bucle para recibir y manejar actualizaciones
offset = None
while True:
    updates = bot.get_updates(offset)
    if updates['result']:
        bot.handle_updates(updates, excel_handler)
        # Actualizar el offset para obtener solo nuevos mensajes
        offset = updates['result'][-1]['update_id'] + 1

