import time
import json
def es_ganador(tarjeton, numeros_extraidos):
    numeros_extraidos_format = set(f"{obtener_letra(num)}-{num}" for num in numeros_extraidos if num != "FREE")

    for row in zip(tarjeton['B'], tarjeton['I'], tarjeton['N'], tarjeton['G'], tarjeton['O']):
        if all(f"{letra}-{num}" in numeros_extraidos_format or num == "FREE" for letra, num in zip(['B', 'I', 'N', 'G', 'O'], row)):
            return True

    for letra in ['B', 'I', 'N', 'G', 'O']:
        if all(f"{letra}-{num}" in numeros_extraidos_format or num == "FREE" for num in tarjeton[letra]):
            return True

    if all(f"{letra}-{num}" in numeros_extraidos_format or num == "FREE" for letra, num in zip(['B', 'I', 'N', 'G', 'O'], [tarjeton['B'][0], tarjeton['I'][1], tarjeton['N'][2], tarjeton['G'][3], tarjeton['O'][4]])):
        return True
    if all(f"{letra}-{num}" in numeros_extraidos_format or num == "FREE" for letra, num in zip(['B', 'I', 'N', 'G', 'O'], [tarjeton['O'][0], tarjeton['G'][1], tarjeton['N'][2], tarjeton['I'][3], tarjeton['B'][4]])):
        return True

    return False

def generar_numero_aleatorio(lim_inferior, lim_superior, numeros_extraidos):
    Xo = int(time.time())
    a = 1103515245
    c = 12345
    m = 32768

    while True:
        Xn = (a * Xo + c) % m
        numero_aleatorio = lim_inferior + (Xn * (lim_superior - lim_inferior) // m)
        if numero_aleatorio not in numeros_extraidos:
            numeros_extraidos.add(numero_aleatorio)
            return numero_aleatorio, numeros_extraidos
        Xo = Xn


def obtener_letra(numero):
    if numero <= 15:
        return 'B'
    elif numero <= 30:
        return 'I'
    elif numero <= 45:
        return 'N'
    elif numero <= 60:
        return 'G'
    elif numero <= 75:
        return 'O'

def simulador_bingo():
    numeros_extraidos = set()
    while len(numeros_extraidos) < 75:
        numero, numeros_extraidos = generar_numero_aleatorio(1, 76, numeros_extraidos)
        letra = obtener_letra(numero)
        balota = f"{letra}-{numero}"
        print(f"Balota Extraida: {balota}")
        if len(numeros_extraidos)==74:
          break

    print("Números llamados hasta ahora:")
    print(sorted(f"{obtener_letra(num)}-{num}" for num in numeros_extraidos))
    
    bal=(f"{obtener_letra(num)}-{num}" for num in numeros_extraidos)
    return bal

def cargar_tarjetones(archivo_json):
    with open(archivo_json, 'r') as file:
        data = json.load(file)
    return data['tarjetones']

def verificar_coincidencias(tarjetones, numeros_extraidos):
    resultados = {}
    for tarjeton in tarjetones:
        id_tarjeton = tarjeton['id']
        coincidencias = []
        for letra, numeros in tarjeton.items():
            if letra in ['B', 'I', 'N', 'G', 'O']:
                for numero in numeros:
                    if numero != "FREE" and numero in numeros_extraidos:
                        coincidencias.append(f"{letra}-{numero}")
        resultados[id_tarjeton] = coincidencias
    return resultados

def generar_tablero(lim_inferior , lim_superior, numeros_extraidos):
    Xo = int(time.time())
    a = 1103515245
    c = 12345
    m = 32768

    while True:
        Xn = (a * Xo + c) % m
        numero_aleatorio = lim_inferior + (Xn * (lim_superior - lim_inferior) // m)
        if numero_aleatorio not in numeros_extraidos:
            numeros_extraidos.add(numero_aleatorio)
            return numero_aleatorio, numeros_extraidos
        Xo = Xn