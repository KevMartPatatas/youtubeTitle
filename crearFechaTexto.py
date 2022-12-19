import random

def crear_texto_fecha():
    m_o_k = random.choice(['M', 'K'])
    
    if m_o_k == 'M':
        visitas = random.randint(1, 18)
        unidad_tiempo = random.choice(['semanas', 'meses', 'años'])

        if unidad_tiempo == 'semanas':
            tiempo = random.randint(1, 4)
            if tiempo == 1:
                unidad_tiempo = 'semana'
        if unidad_tiempo == 'meses':
            tiempo = random.randint(1, 11)
            if tiempo == 1:
                unidad_tiempo = 'mes'
        if unidad_tiempo == 'años':
            tiempo = random.randint(1, 15)
            if tiempo == 1:
                unidad_tiempo = 'año'

        texto_visitas = f'{visitas} {m_o_k} de vistas hace {str(tiempo)} {unidad_tiempo}'

    else:
        visitas = random.randint(1, 999)
        unidad_tiempo = random.choice(['horas', 'días', 'semanas', 'meses'])

        if unidad_tiempo == 'horas':
            tiempo = random.randint(1, 23)
            if tiempo == 1:
                unidad_tiempo = 'hora'
        if unidad_tiempo == 'días':
            tiempo = random.randint(1, 6)
            if tiempo == 1:
                unidad_tiempo = 'día'
        if unidad_tiempo == 'semanas':
            tiempo = random.randint(1, 4)
            if tiempo == 1:
                unidad_tiempo = 'semana'
        if unidad_tiempo == 'meses':
            tiempo = random.randint(1, 11)
            if tiempo == 1:
                unidad_tiempo = 'mes'

        texto_visitas = f'{visitas} {m_o_k} vistas hace {tiempo} {unidad_tiempo}'

    return texto_visitas