# Importar dependencia para funciones de aleatoriedad
import random 

def obtener_lista_palabras():
    """
    Genera y devuelve una lista de 20 palabras en minúsculas.

    Retorna:
        list[str]: Lista de palabras en minúsculas.
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
    Selecciona y devuelve una palabra al azar de la lista de palabras.

    Retorna:
        str: Palabra elegida aleatoriamente.
    """
    
    palabra_secreta = obtener_lista_palabras()
    return random.choice(palabra_secreta)

