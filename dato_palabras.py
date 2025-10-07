#importa libreria random para aleatorizar
import random 

#funcion que crea una lista de palabras y asegura las palabras en minusculas retornandolas
def obtener_lista_palabras():
    lista = [
    "barro", "juego", "zumba", "calor", "hielo", "lanza", "borde", "salsa", "pulso",
    "brisa", "tacho", "fluir", "nubes", "vigor", "joven", "raton",
    "marea", "llama", "tenaz", "crisp"
]
    lista_minus=[palabra.lower() for palabra in lista]
    return lista_minus

# funcion que selecciona una de las palabras de la lista (usa random libreria importada)
def seleccionar_palabra_secreta():
    palabra= obtener_lista_palabras()
    return random.choice(palabra)

