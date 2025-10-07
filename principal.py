from datos_palabras.py import seleccionar_palabra_secreta
from validacion.py import verificar_victoria
from evaluacion.py import evaluar_intento
from pantalla.py import mostrar_mensaje_bienvenida, mostrar_retroalimentacion, mostrar_mensaje_victoria, mostrar_mensaje_derrota
from manejo_entrada.py import obtener_intento_jugador
import sys

def jugar():
    LONGITUD_PALABRA = 5
    INTENTOS_MAXIMOS = 6
    palabra_s = seleccionar_palabra_secreta()
    print("mensaje de bienvenida")
    for i in range(1,INTENTOS_MAXIMOS,1):
        pass


if __name__ == "__main__":
    while True:
        try:
            jugar()
            sys.exit(0) 
        except KeyboardInterrupt:
            print("Mensaje de despedida")
            sys.exit(0)

    