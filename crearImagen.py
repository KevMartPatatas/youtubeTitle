from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
from crearFechaTexto import crear_texto_fecha
from imgNumber import leer_num_img


fuente = ImageFont.truetype('recursos/fuentes/Araboto Bold 400.ttf', 45)
fuente2 = ImageFont.truetype('recursos/fuentes/ARIAL.ttf', 30)

def crear_imagen(texto):
    num_img = str(leer_num_img()) # <--- Llamo a la funcion para leer el numero de imagen
    img_principal = Image.open(f'img/{num_img}.png')

    ancho_img_barra_blanca = random.randint(200, 1100)
    ancho_img_barra_roja = random.randint(150, ancho_img_barra_blanca - 50)

    if ancho_img_barra_blanca - ancho_img_barra_roja > 400:
        ancho_img_barra_roja = ancho_img_barra_roja + 390

    base = Image.new('RGB', (1280, 1014), (15, 15, 15))
    img_base = Image.new('RGB', (1280, 770), (0, 0, 0))
    img_barra_transparente = Image.new('RGBA', (1280, 5), (250, 250, 250))
    img_barra_blanca = Image.new('RGB', (ancho_img_barra_blanca, 5), (200, 200, 200))
    img_barra_roja = Image.new('RGB', (ancho_img_barra_roja, 5), (255, 0, 0))

    img_barra_transparente.putalpha(80)

    ancho_original, alto_original = img_principal.size
    img_redimencionada = img_principal.resize((int((ancho_original * 770) / alto_original), 770))
    ancho_nuevo, alto_nuevo= img_redimencionada.size

    base.paste(img_base, (0, 0))
    base.paste(img_redimencionada, (int((1280 - ancho_nuevo) / 2), 0))
    base.paste(img_barra_transparente, (0, 765), img_barra_transparente)
    base.paste(img_barra_blanca, (0, 765))
    base.paste(img_barra_roja, (0, 765))
    
    crear_texto(base, texto)


def crear_texto(base, texto):
    num_img = str(leer_num_img()) # <--- Llamo a la funcion para leer el numero de imagen
    if len(texto) > 109:
        texto = texto[:110] + '...'

    # texto2 = '1 M de vistas hace 2 años'
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
    base.save(f'exported/{num_img}.png')
