from dato_palabras import seleccionar_palabra_secreta
from validacion import verificar_victoria, validar_intento
from evaluacion import evaluar_intento
from pantalla import mostrar_mensaje_bienvenida, mostrar_retroalimentacion, mostrar_mensaje_victoria, mostrar_mensaje_derrota
from manejo_entrada import obtener_intento_jugador
import sys

def jugar():
    LONGITUD_PALABRA = 5
    INTENTOS_MAXIMOS = 6
    
    secreta = seleccionar_palabra_secreta()
    mostrar_mensaje_bienvenida()
    
    for intento in range(1,INTENTOS_MAXIMOS+1):
        print(f"Intento numero {intento}")
        palabra_intento = obtener_intento_jugador(intento, INTENTOS_MAXIMOS)
        while True:
            try:
                palabra_intento = obtener_intento_jugador(intento, INTENTOS_MAXIMOS)
                if validar_intento(palabra_intento, LONGITUD_PALABRA) == True:
                    break
            except KeyboardInterrupt:
                print("Mensaje de despedida")
                sys.exit(0)
        
        estados = evaluar_intento(secreta, palabra_intento)
        mostrar_retroalimentacion(intento, estados)
        
        if intento == INTENTOS_MAXIMOS:
            mostrar_mensaje_derrota(secreta)
        if verificar_victoria(estados):
            mostrar_mensaje_victoria(secreta, intento)
            break


if __name__ == "__main__":
    jugar()

    