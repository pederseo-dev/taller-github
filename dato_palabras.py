import random

def obtener_lista_palabras():
    lista = [
    "barro", "crisp", "zumba", "calor", "hielo", "lanza", "borde", "salsa", "pulso",
    "brisa", "tacho", "tenaz", "nubes", "vigor", "joven", "raton",
    "marea", "llama", "tenaz", "crisp"
]
    return lista.lower()

def seleccionar_palabra_secreta():
    palabra= obtener_lista_palabras()
    return random.choice(palabra)