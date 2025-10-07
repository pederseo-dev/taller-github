# Importar dependencia para funciones de aleatoriedad
import random 

def obtener_lista_palabras():
    """
    Funcion que genera una lista de 20 palabras, asegura que esten en minuscula con .lower() y retorna la lista para utilizarla luego.
    """
    lista_de_palabras = [
    "barro", "juego", "zumba", "calor", "hielo", "lanza", "borde", "salsa", "pulso",
    "brisa", "tacho", "fluir", "nubes", "vigor", "joven", "raton",
    "marea", "llama", "tenaz", "crisp"
]
    lista_palabras_en_minuscula = [palabra.lower() for palabra in lista_de_palabras]
    return lista_palabras_en_minuscula 
 
def seleccionar_palabra_secreta():
    """
    Funcion que selecciona una palabra de la lista de manera aleatoria.
    """
    palabra_secreta = obtener_lista_palabras()
    return random.choice(palabra_secreta)

