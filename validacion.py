def validar_intento(intento,longitud_palabra):

    if longitud_palabra == 5 and intento.isalpha():
        return (True,"")
    elif longitud_palabra!= 5:
        return (False,"Debe tener exactamente 5 letras")
    else:
        return (False, "Solo se permiten Letras")
    

    
