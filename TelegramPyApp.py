import requests

CHATID = ''
BOTTOKRN = ''
mensaje = ''
requests.post('https://api.telegram.org/[BOTTOKEN]/sendMessage',data={'chat_id': '[CHATID]', 'text': 'Resultado de la prueba:'})
requests.post('https://api.telegram.org/[BOTTOKEN]/sendMessage',data={'chat_id': '[CHATID]', 'text': mensaje})