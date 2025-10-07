def validar_intento(intento,longitud_palabra):

    if longitud_palabra == 5 and intento.isalpha():
        return (True,"")
    elif longitud_palabra!= 5:
        return (False,"Debe tener exactamente 5 letras")
    else:
        return (False, "Solo se permiten Letras")
    
def verificar_victoria(estados):
    cantida_estados = len(estados)
    contador = 0
    for i in estados:
        if i == "correcta":
            contador += 1
    if contador == cantida_estados:
        return True
    else:
        return False
    
