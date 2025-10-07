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
    """
    Recibi una lista de string, donde estan los estados de cada letra
    """
    contador = 0 #Inicializo mi contador
    for i in estados:
        if i == "correcta": #Si el itirador es igual a la palabra correcta
            contador += 1   #Si es igual el contador suma 1
    if contador == 5: #Si el contador es igual a la cantidad de estado (5) retorna true si no retorna false
        return True
    else:
        return False
    
