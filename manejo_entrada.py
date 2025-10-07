from validacion import validar_intento

# Funcion para retornar palabra valida o un mensaje de error.

def obtener_intento_jugador(numero_intento, intentos_maximos):

    cantidad_intentos = 0

    while True:
            
            print(f"Intento {cantidad_intentos + 1}/{intentos_maximos}")
            # Solicitamos al usuario que ingrese una palabra y convertimos a minusculas y sacamos los espacios
            palabra_valida = input("Ingresa una palabra: ").strip().lower() 
            
            # Desempaquetamos el return de validar_intento()
            bandera, mensaje = validar_intento(numero_intento,len(palabra_valida))

            # Si bandera == True
            if bandera:
                return palabra_valida
            else:
                print(mensaje)

