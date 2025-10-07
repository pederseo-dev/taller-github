def validar_intento(intento,longitud_palabra): 
    """
    Recibe la cantidad de intentos y la longitud de la palabra ingresada
    """
    if longitud_palabra == 5 and intento.isalpha():
        return (True,"") #Retorna True si es que tiene exactamente 5 letras
    elif longitud_palabra!= 5:
        return (False,"Debe tener exactamente 5 letras") #Retorna False si no tiene exactamente 5 letras
    else:
        return (False, "Solo se permiten Letras") #Esto es por si no ingreso una letra
    
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
    
