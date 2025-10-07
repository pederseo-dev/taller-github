def mostrar_mensaje_bienvenida(longitud_palabra=5, intentos_maximos=6):

    print("=" * 50)
    print()
    print(f"¡Bienvenido a Woordle!")
    print()
    print(f"Tienes que adivinar una palabra de {longitud_palabra} letras.")
    print(f"Tienes {intentos_maximos} intentos para adivinar la palabra.")

    print()
    print("Después de cada intento, recibirás pistas:")
    print("  ✓ = Letra correcta en posición correcta")
    print("  ? = Letra presente pero en otra posición")
    print("  X = Letra no está en la palabra")

    print()
    print("=" * 50)

def mostrar_retroalimentacion(intento, estados):
    intento_mayus = intento.upper()
    letras = " ".join(intento_mayus)

    mapa = {
    'correcta': '✓',
    'presente': '?',
    'ausente': 'X'
    }

    simbolos = [mapa[estado] for estado in estados]

    linea_simbolos = " ".join(simbolos)

    print("  " + letras)
    print("  " + linea_simbolos)

def mostrar_mensaje_victoria(secreta, intentos):
    print(f'Felicidades! Lograste adivinar la palabra: {secreta.upper()}, en {intentos} intentos.')

def mostrar_mensaje_derrota(secreta):
    print(f"Lo siento, la palabra era: {secreta.upper()}. Inténtalo de nuevo, ÁNIMO!!!")