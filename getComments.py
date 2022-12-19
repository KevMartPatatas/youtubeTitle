import facebook as fb
import requests
import time
from getReactions import get_reactions
from descargarArchivos import *
from postID import leer_postID


token_de_acceso = 'EAAJZCZAtZCHrxsBAOcqIrqobe6MQsfalvZBiGzwqZCxvnwIOEDKvY1GU6rtOJ3hrLYRvdgJQZBnbQlQAZC4SF7tuGcZApU49zlZBnHRnZCwiE4aKK2MBWQA3jGz1eLdNgCaoJ07cknGDQObZAhsqvRuUWPbfEYwop022T8W0nLQBSOcZCknHbRMVRH1q'
graph = fb.GraphAPI(access_token = token_de_acceso)

def getCommets():
    num_voto_mayor = -100
    num_total_req = 0
    id_post = leer_postID()

    comentarios = graph.get_connections(id = f'111183688507773_{id_post}', connection_name = 'comments')

    for comentario in comentarios['data']: # <--- Itero los comenterios
        id_comentario = comentario['id'] # <--- Me da el ID del comentario

        url_solicitar_informacion_comentario = f'https://graph.facebook.com/{id_comentario}?fields=attachment&access_token={token_de_acceso}'

        repetir = True
        while repetir == True:
            try:
                solicitud_informacion_comentario = requests.get(url_solicitar_informacion_comentario).json() # <--- Hago la solicitud y guardo la informacion en esa variable
                repetir = False
            except:
                print('se repite')
                time.sleep(5)
                repetir = True

        if (len(solicitud_informacion_comentario) == 2): # <--- Me comprueba que el comentario tenga una archivo adjunto
            tipo_archivo_adjunto = solicitud_informacion_comentario['attachment']['type'] # <--- Me devulve el tipo de archivo adjunto

            if (tipo_archivo_adjunto == 'photo' or tipo_archivo_adjunto == 'video_inline'): # <--- Me comprueba que el archivo adjunto sea una foto o una foto
                mensaje = comentario['message'].strip()
                mensaje_separado = mensaje.split()

                if (mensaje_separado[0].lower() == '!req'):
                    repetir = True
                    while repetir == True:
                        try:
                            voto_total = get_reactions(id_comentario) # <--- Llamo a la funcion para conseguir el numero de votos, pasandole como parametro el id del comentario
                            repetir = False
                        except:
                            time.sleep(5)
                            repetir = True

                    num_total_req += 1
                    texto = mensaje.lower().split('!req')[1].strip()

                    if (voto_total >= num_voto_mayor): # <--- Comprueba que, el numero de votos sea mayor al numero mayor de votos en cada iteracion
                        num_voto_mayor = voto_total # <--- guardo el voto total en la variable de numero de votos mayor en cada iteracion
                        texto_final = texto

                        if tipo_archivo_adjunto == 'photo':
                            src = solicitud_informacion_comentario['attachment']['media']['image']['src'] # <--- Me da la url de la imaagen para descargar
                        elif tipo_archivo_adjunto == 'video_inline':
                            src = solicitud_informacion_comentario['attachment']['media']['source']

                        tipo_archivo = tipo_archivo_adjunto


    if num_voto_mayor != -100: # <--- Despues de salir del bucle. Simplemente me comrpueba que, de todos los comentarios haya por lo menos un comentario que cumpla con las caracteristicas
        if tipo_archivo == 'photo':
            descargar_imagen(src) # <--- Llamo a la funcion para descargar la imagen, le paso como parametro el link directo de la imagen
        else:
            if tipo_archivo == 'video_inline':
                descargar_video(src)
        return [texto_final, num_voto_mayor, num_total_req, tipo_archivo, src]

    else:
        return [num_voto_mayor]