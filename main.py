import facebook as fb
from imgNumber import *
from getComments import getCommets
from crearImagen import crear_imagen
from crearVideo import crear_video
import time
import requests
import schedule
from postID import *
from datetime import datetime
import os
from decouple import config

os.environ['TOKEN'] = config('TOKEN')
token_de_acceso = os.environ['TOKEN']
graph = fb.GraphAPI(access_token = token_de_acceso)

def main():
    num_img = leer_num_img()
    datos_retornados = getCommets()

    if len(datos_retornados) > 1:
        texto, num_voto_mayor, num_total_req, tipo_archivo, src = datos_retornados

        if tipo_archivo == 'photo':
            crear_imagen(texto)
            extension = 'png'
        elif tipo_archivo == 'video_inline':
            crear_video(texto)
            extension = 'video'

        repetir = True
        while repetir == True:
            try:
                post_id_viejo = leer_postID()
                mensaje = f'Su petición.\nNúmero de imagen: {str(num_img)}'

                if extension == 'png':
                    publicar_imagen = graph.put_photo(image = open(f'exported/{str(num_img)}.png', 'rb'), message = mensaje)
                    post_id_nuevo = publicar_imagen['id']
                    print(publicar_imagen['id'])
                    graph.put_comment(object_id = post_id_viejo, message = 'Ya hay una publicación mas reciente. No se tomarán en cuenta los pedidos en esta publicación.')
                else:
                    if extension == 'video':
                        url_solicitar_subir_video = 'https://graph.facebook.com/100088379456302/videos'
                        fp = f'exported/{str(num_img)}.mp4'
                        files = {'source': open(fp, 'rb')}
                        payload = {'access_token': token_de_acceso, 'title': f'Petición No. {str(num_img)}', 'description': mensaje}

                        try:
                            requests.post(url_solicitar_subir_video, files=files, data=payload, verify=False)
                            time.sleep(15)
                            url_solicitar_subir_video = 'https://graph.facebook.com/100088379456302/videos?access_token=' + token_de_acceso
                            videos_subidos = requests.get(url_solicitar_subir_video).json()
                            post_id_nuevo = videos_subidos['data'][0]['id']
                            print(videos_subidos['data'][0]['id'])
                            graph.put_comment(object_id = post_id_viejo, message = 'Ya hay una publicación mas reciente. No se tomarán en cuenta los pedidos en esta publicación.')
                        except:
                            pass
                post_id_nuevo = post_id_nuevo # <--- Si esto me da probemas despues, le agrego el ID de la pagina.
                repetir = False
            except:
                print('No se puede publicar la imagen debido al id')
                time.sleep(5)
                repetir = True

        repetir = True
        while repetir == True:
            try:
                mensaje = f'Número de votos: {str(num_voto_mayor)}\nNúmero de peticiones en la publicación anterior: {str(num_total_req)}\nPor favor, vota negativamente las malas imágenes y vota positivamente las buenas imágenes.\n\n¿Como hacer un petición? Comenta: !req + mensaje\n\nSistema de votación: \U0001F44D, \U0001F493, Me importa, \U0001F606, Me asombra: +1 voto\nMe entristece, Me enoja: -1 voto\n\nID del post: {post_id_nuevo}'
                graph.put_comment(object_id = post_id_nuevo, message = mensaje)
                repetir = False
            except:
                print('No se puede poner el comentario. ID invalido')
                time.sleep(5)
                repetir = True

        reestablecer_postID(post_id_nuevo)
        reescribir_numero_img()

    else:
        print('Ningun comentario valido')


if __name__ == '__main__':
    schedule.every(15).seconds.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
    # main()