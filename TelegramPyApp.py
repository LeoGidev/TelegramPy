import requests

CHATID = 'tu_chat_id_aqui'
BOTTOKEN = 'tu_bot_token_aqui'
mensaje = 'Resultado de la prueba'

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
