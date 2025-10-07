def obtener_intento_jugador(numero_intento, intentos_maximos):
        cantidad_intentos = 0
        while cantidad_intentos < intentos_maximos:
        
            print(f"Intento {cantidad_intentos + 1}/{intentos_maximos}")
            palabra_valida = input("Ingresa una palabra: ").strip().lower()
            if validar_intento(palabra_valida):
                  return palabra_valida
            else:
                print("Error")
            cantidad_intentos += 1


