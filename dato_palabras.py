# Importar dependencia para funciones de aleatoriedad
import random 

def obtener_lista_palabras():
    """
    Funcion que genera una lista de 20 palabras, asegura que esten en minuscula con .lower() y retorna la lista para utilizarla luego.
    """
    lista = [
    "barro", "juego", "zumba", "calor", "hielo", "lanza", "borde", "salsa", "pulso",
    "brisa", "tacho", "fluir", "nubes", "vigor", "joven", "raton",
    "marea", "llama", "tenaz", "crisp"
]
    lista_minus=[palabra.lower() for palabra in lista]
    return lista_minus

def seleccionar_palabra_secreta():
    """
    Funcion que selecciona una palabra de la lista de manera aleatoria.
    """
    palabra= obtener_lista_palabras()
    return random.choice(palabra)

