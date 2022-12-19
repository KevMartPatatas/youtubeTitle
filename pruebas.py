import facebook as fb
import json

# token_de_acceso = 'EAAJZCZAtZCHrxsBAOUK8I7s6BNb6SBDeEmTYFHO9n7uecbAvPZAzmBIYQHWlW6AcCNJShYaXsTRi2QtEWZAHEC5DG4IGNmlGzhtAIwIIVCG7OKj42xYZCAUMYHZCxHGPBSVNOahZCtXH7n10mpMKdZAFDIxh86FMGE3QpE4HwLZC7uFKhzFgENrnQt'
# import requests

# url_solicitar_subir_video = 'https://graph.facebook.com/111183688507773/videos?access_token=' + token_de_acceso
# videos_subidos = requests.get(url_solicitar_subir_video).json()
# print(videos_subidos)

# graph = fb.GraphAPI(access_token = token_de_acceso)

# graph.put_object(parent_object='me', connection_name='feed',message='\U0001F606')
# print('\U0001F606')

ruta = 'recursos/recursos.json'

with open(ruta) as datos:
    post_id = json.load(datos)[0]['post_id']
    print(post_id)