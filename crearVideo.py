from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import textwrap
from crearFechaTexto import crear_texto_fecha
from imgNumber import leer_num_img


fuente = ImageFont.truetype('recursos/fuentes/Araboto Bold 400.ttf', 45)
fuente2 = ImageFont.truetype('recursos/fuentes/ARIAL.ttf', 30)

def crear_video(texto):
    num_img = str(leer_num_img()) # <--- Llamo a la funcion para leer el numero de imagen
    video = VideoFileClip(f'img/{num_img}.mp4')

    ancho_original, alto_original = video.size
    video = video.resize(width = int((770 * ancho_original) / alto_original))
    ancho_nuevo, alto_nuevo = video.size
    print(ancho_nuevo, alto_nuevo)

    base = Image.new('RGB', (1280, 1014), (15, 15, 15))
    img_base = Image.new('RGB', (1280, 770), (0, 0, 0))
    
    crear_texto(base, texto)

    img_base.save('recursos/temporal/img_base.png')
    
    clipBase = ImageClip('recursos/temporal/base.png')
    clipBase = clipBase.set_duration(video.duration)

    clipImgBase = ImageClip('recursos/temporal/img_base.png')
    clipImgBase = clipImgBase.set_duration(video.duration)

    inicio_clip = 64 - video.duration

    if video.duration > 64:
        inicio_clip = 0

    clipBarraRoja = VideoFileClip('recursos/barra_roja_larga.gif').subclip(inicio_clip, 64)
    clipBarraRoja = clipBarraRoja.set_duration(video.duration)

    posicion = int((1280 - ancho_nuevo) / 2)

    videoFinal = CompositeVideoClip([clipBase, clipImgBase.set_position((0, 0)), video.set_position((posicion, 0)), clipBarraRoja.set_position((0, 765))])
    videoFinal.write_videofile(f'exported/{num_img}.mp4', fps = video.fps)


def crear_texto(base, texto):
    if len(texto) > 109:
        texto = texto[:110] + '...'

    texto_fecha = crear_texto_fecha()
    dibujo_texto_principal = ImageDraw.Draw(base)
    dibujo_texto_principal_2 = ImageDraw.Draw(base)
    y_text = 810

    alto_img = 0
    lines = textwrap.wrap(texto, width = 58)
    for line in lines:
        line_width, line_height = fuente.getsize(line)
        dibujo_texto_principal.text((30, y_text), line, font=fuente, fill = 'white')
        alto_img += line_height
        y_text += line_height

    dibujo_texto_principal_2.text((30, y_text + 30), texto_fecha, font=fuente2, fill = 'gray')
    line_width, line_height = fuente2.getsize(texto_fecha)

    base = base.crop((0, 0, 1280, y_text + line_height + 60))
    base.save('recursos/temporal/base.png')
