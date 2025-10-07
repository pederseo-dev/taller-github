# TODO - Wordle Terminal (Taller Git)

## 📋 Descripción General

Este proyecto es un juego de Wordle para terminal. Cada participante desarrollará un módulo específico del juego. Al final, todos los módulos se integrarán en la rama principal mediante Git para formar el juego completo.

**IMPORTANTE**: Debes respetar exactamente los nombres de funciones, parámetros y tipos de retorno especificados. Esto garantiza que tu código funcione correctamente con el de los demás participantes.

---

## 📦 ARCHIVO 1: `datos_palabras.py`

**Responsabilidad**: Gestionar el banco de palabras del juego y seleccionar la palabra secreta.

### Función 1: `obtener_lista_palabras()`

```
FUNCIÓN: obtener_lista_palabras
PARÁMETROS: ninguno
RETORNA: lista de strings (palabras de 5 letras en minúsculas)

DESCRIPCIÓN:
Esta función debe retornar una lista con al menos 20 palabras de exactamente 5 letras.
Todas las palabras deben estar en minúsculas y ser palabras válidas en español.

EJEMPLO DE RETORNO:
["amigo", "perro", "cielo", "libro", ...]
```

**Tareas**:
1. Crea una lista con mínimo 20 palabras de 5 letras
2. Asegúrate de que todas estén en minúsculas
3. La función debe retornar esta lista

---

### Función 2: `seleccionar_palabra_secreta()`

```
FUNCIÓN: seleccionar_palabra_secreta
PARÁMETROS: ninguno
RETORNA: string (una palabra de 5 letras en minúsculas)

DESCRIPCIÓN:
Esta función debe seleccionar UNA palabra al azar de la lista de palabras disponibles.
Cada vez que se llame, puede retornar una palabra diferente (aleatoria).

PISTA: Investiga el módulo 'random' de Python
```

**Tareas**:
1. Llama a `obtener_lista_palabras()` para obtener las palabras disponibles
2. Selecciona una palabra al azar de esa lista
3. Retorna la palabra seleccionada

---

## 🔍 ARCHIVO 2: `validacion.py`

**Responsabilidad**: Validar las entradas del usuario y verificar condiciones de victoria.

### Función 1: `validar_intento(intento, longitud_palabra=5)`

```
FUNCIÓN: validar_intento
PARÁMETROS: 
  - intento: string (la palabra ingresada por el jugador)
  - longitud_palabra: int (opcional, por defecto 5)
RETORNA: tupla (bool, string)
  - Primer elemento: True si es válido, False si no lo es
  - Segundo elemento: mensaje de error (string vacío "" si es válido)

DESCRIPCIÓN:
Verifica que el intento cumpla las reglas del juego.
Reglas a verificar:
- Debe tener exactamente la longitud especificada
- Solo debe contener letras (sin números ni símbolos)

EJEMPLOS:
validar_intento("perro", 5) → (True, "")
validar_intento("per", 5) → (False, "Debe tener exactamente 5 letras.")
validar_intento("per2o", 5) → (False, "Solo se permiten letras.")
```

**Tareas**:
1. Verifica que la longitud del intento sea exactamente `longitud_palabra`
2. Verifica que el intento solo contenga letras (usa el método `.isalpha()`)
3. Retorna la tupla apropiada según las validaciones

---

### Función 2: `verificar_victoria(estados)`

```
FUNCIÓN: verificar_victoria
PARÁMETROS:
  - estados: lista de strings
RETORNA: bool (True si ganó, False si no)

DESCRIPCIÓN:
Determina si el jugador adivinó la palabra completa.
Esto ocurre cuando TODAS las letras tienen el estado 'correcta'.

La lista de estados contiene strings que pueden ser:
- 'correcta': letra en la posición correcta
- 'presente': letra existe pero en otra posición
- 'ausente': letra no existe en la palabra

EJEMPLO:
verificar_victoria(['correcta', 'correcta', 'correcta', 'correcta', 'correcta']) → True
verificar_victoria(['correcta', 'presente', 'correcta', 'correcta', 'correcta']) → False
```

**Tareas**:
1. Recorre todos los elementos de la lista `estados`
2. Verifica si TODOS son iguales a 'correcta'
3. Retorna True solo si todos son 'correcta', False en caso contrario

**PISTA**: Investiga la función `all()` de Python

---

## 🧮 ARCHIVO 3: `evaluacion.py`

**Responsabilidad**: Evaluar los intentos del jugador comparándolos con la palabra secreta.

### Función 1: `contar_letras_disponibles(secreta, intento)`

```
FUNCIÓN: contar_letras_disponibles
PARÁMETROS:
  - secreta: string (la palabra secreta)
  - intento: string (la palabra del jugador)
RETORNA: diccionario {string: int}
  - Clave: letra (char)
  - Valor: cantidad de veces que aparece disponible

DESCRIPCIÓN:
Cuenta cuántas veces aparece cada letra de la palabra secreta que NO está 
ya en su posición correcta. Esto es necesario para manejar letras repetidas.

IMPORTANTE: Solo cuenta las letras donde secreta[i] != intento[i]

EJEMPLO:
secreta = "perro"
intento = "puede"
- Posición 0: 'p' == 'p' → NO se cuenta
- Posición 1: 'e' != 'u' → se cuenta 'e'
- Posición 2: 'r' != 'e' → se cuenta 'r'
- Posición 3: 'r' != 'd' → se cuenta 'r'
- Posición 4: 'o' != 'e' → se cuenta 'o'

RETORNO: {'e': 1, 'r': 2, 'o': 1}
```

**Tareas**:
1. Convierte ambas palabras a minúsculas
2. Crea un diccionario vacío para los conteos
3. Recorre cada posición (índice) de las palabras
4. Si las letras en esa posición son DIFERENTES, incrementa el contador de la letra de `secreta`
5. Retorna el diccionario

---

### Función 2: `evaluar_intento(secreta, intento)`

```
FUNCIÓN: evaluar_intento
PARÁMETROS:
  - secreta: string (la palabra secreta)
  - intento: string (la palabra del jugador)
RETORNA: lista de strings con los estados de cada letra

DESCRIPCIÓN:
Evalúa cada letra del intento y determina su estado.
Estados posibles:
- 'correcta': letra en la posición correcta
- 'presente': letra existe en la palabra pero en otra posición
- 'ausente': letra no existe en la palabra

ALGORITMO (seguir este orden):
1. Convertir ambas palabras a minúsculas
2. Crear lista de estados inicializada con None
3. Obtener conteo de letras disponibles con contar_letras_disponibles()
4. PRIMER PASO: Marcar todas las posiciones 'correcta'
   - Recorrer cada posición
   - Si intento[i] == secreta[i], marcar estados[i] = 'correcta'
5. SEGUNDO PASO: Marcar 'presente' o 'ausente'
   - Recorrer cada posición que todavía es None
   - Si la letra tiene conteo disponible > 0: marcar 'presente' y decrementar conteo
   - Si no: marcar 'ausente'
6. Retornar lista de estados

EJEMPLO:
secreta = "perro"
intento = "raton"
→ ['ausente', 'ausente', 'ausente', 'presente', 'correcta']
```

**Tareas**:
1. Implementa el algoritmo descrito paso a paso
2. Usa la función `contar_letras_disponibles()` que ya creaste
3. Asegúrate de seguir el orden: primero todas las 'correcta', luego 'presente'/'ausente'

---

## 🖥️ ARCHIVO 4: `pantalla.py`

**Responsabilidad**: Mostrar información al usuario (mensajes y feedback visual).

### Función 1: `mostrar_mensaje_bienvenida(longitud_palabra=5, intentos_maximos=6)`

```
FUNCIÓN: mostrar_mensaje_bienvenida
PARÁMETROS:
  - longitud_palabra: int (opcional, por defecto 5)
  - intentos_maximos: int (opcional, por defecto 6)
RETORNA: None (solo imprime en pantalla)

DESCRIPCIÓN:
Muestra un mensaje de bienvenida que explique las reglas del juego.
Debe incluir:
- Título del juego
- Explicar que debe adivinar una palabra de X letras
- Explicar que tiene X intentos
- Explicar los símbolos:
  ✓ = Letra correcta en posición correcta
  ? = Letra presente pero en otra posición
  X = Letra no presente en la palabra
```

**Tareas**:
1. Usa `print()` para mostrar un mensaje bonito y claro
2. Incluye la información mencionada
3. Puedes usar símbolos como "=" para hacer líneas decorativas

---

### Función 2: `mostrar_retroalimentacion(intento, estados)`

```
FUNCIÓN: mostrar_retroalimentacion
PARÁMETROS:
  - intento: string (la palabra intentada)
  - estados: lista de strings (['correcta', 'presente', 'ausente', ...])
RETORNA: None (solo imprime en pantalla)

DESCRIPCIÓN:
Muestra visualmente el resultado del intento.
Debe mostrar DOS líneas:
1. Las letras del intento en mayúsculas, separadas por espacios
2. Los símbolos correspondientes a cada letra, separados por espacios

Mapeo de estados a símbolos:
- 'correcta' → '✓'
- 'presente' → '?'
- 'ausente' → 'X'

EJEMPLO:
intento = "gatos"
estados = ['correcta', 'ausente', 'presente', 'ausente', 'correcta']

SALIDA:
  G A T O S
  ✓ X ? X ✓
```

**Tareas**:
1. Convierte el intento a mayúsculas
2. Crea la línea de letras separadas por espacios
3. Crea un diccionario que mapee estados a símbolos
4. Crea la línea de símbolos separada por espacios
5. Imprime ambas líneas con una indentación (espacios al inicio)

---

### Función 3: `mostrar_mensaje_victoria(secreta, intentos)`

```
FUNCIÓN: mostrar_mensaje_victoria
PARÁMETROS:
  - secreta: string (la palabra secreta)
  - intentos: int (número de intentos que tomó)
RETORNA: None (solo imprime en pantalla)

DESCRIPCIÓN:
Muestra un mensaje de felicitación cuando el jugador gana.
Debe incluir:
- Un mensaje de felicitación
- La palabra que adivinó (en mayúsculas)
- La cantidad de intentos que necesitó
```

---

### Función 4: `mostrar_mensaje_derrota(secreta)`

```
FUNCIÓN: mostrar_mensaje_derrota
PARÁMETROS:
  - secreta: string (la palabra secreta)
RETORNA: None (solo imprime en pantalla)

DESCRIPCIÓN:
Muestra un mensaje cuando el jugador pierde.
Debe incluir:
- Un mensaje indicando que perdió
- Revelar cuál era la palabra secreta (en mayúsculas)
- Un mensaje de ánimo
```

---

## ⌨️ ARCHIVO 5: `manejo_entrada.py`

**Responsabilidad**: Interactuar con el usuario para obtener sus intentos.

### Función: `obtener_intento_jugador(numero_intento, intentos_maximos)`

```
FUNCIÓN: obtener_intento_jugador
PARÁMETROS:
  - numero_intento: int (intento actual, ej: 1, 2, 3...)
  - intentos_maximos: int (total de intentos permitidos, ej: 6)
RETORNA: string (palabra válida en minúsculas)

DESCRIPCIÓN:
Solicita al jugador que ingrese una palabra y valida que sea correcta.
Si no es válida, muestra el error y vuelve a solicitar hasta obtener una válida.

Debe:
1. Mostrar un prompt como "Intento 1/6 - Tu palabra: "
2. Leer la entrada del usuario
3. Eliminar espacios al inicio/final con .strip()
4. Convertir a minúsculas con .lower()
5. Validar usando validar_intento() del archivo validacion.py
6. Si es válida: retornarla
7. Si no es válida: mostrar el error y repetir desde el paso 1

IMPORTANTE: Esta función debe garantizar que SIEMPRE retorna una palabra válida.
```

**Tareas**:
1. Crea un bucle infinito (while True)
2. Dentro del bucle, solicita la entrada con `input()`
3. Procesa la entrada (strip y lower)
4. Valida usando `validar_intento()`
5. Si es válida, retorna (esto rompe el bucle)
6. Si no es válida, imprime el error y continúa el bucle

---

## 🎮 ARCHIVO 6: `principal.py`

**Responsabilidad**: Orquestar el juego completo usando todos los módulos anteriores.

### Función 1: `jugar()`

```
FUNCIÓN: jugar
PARÁMETROS: ninguno
RETORNA: None

DESCRIPCIÓN:
Función principal que ejecuta un juego completo de Wordle.

FLUJO DEL JUEGO:
1. Definir constantes: LONGITUD_PALABRA = 5, INTENTOS_MAXIMOS = 6
2. Seleccionar palabra secreta (usar seleccionar_palabra_secreta())
3. Mostrar mensaje de bienvenida
4. BUCLE para cada intento (desde 1 hasta INTENTOS_MAXIMOS):
   a. Obtener intento del jugador
   b. Evaluar el intento
   c. Mostrar retroalimentación
   d. Verificar victoria:
      - Si ganó: mostrar mensaje victoria y TERMINAR función
5. Si se acabaron los intentos: mostrar mensaje derrota

FUNCIONES QUE DEBES IMPORTAR Y USAR:
- De datos_palabras.py: seleccionar_palabra_secreta()
- De validacion.py: verificar_victoria()
- De evaluacion.py: evaluar_intento()
- De pantalla.py: mostrar_mensaje_bienvenida(), mostrar_retroalimentacion(),
                   mostrar_mensaje_victoria(), mostrar_mensaje_derrota()
- De manejo_entrada.py: obtener_intento_jugador()
```

**Tareas**:
1. Importa todas las funciones necesarias de los otros archivos
2. Implementa el flujo descrito paso a paso
3. Usa un bucle `for` para los intentos: `for intento in range(1, INTENTOS_MAXIMOS + 1):`
4. Usa `return` para terminar la función cuando el jugador gana

---

### Función 2: `principal()`

```
FUNCIÓN: principal
PARÁMETROS: ninguno
RETORNA: None

DESCRIPCIÓN:
Punto de entrada del programa. Ejecuta jugar() y maneja interrupciones.

DEBE:
1. Intentar ejecutar jugar()
2. Capturar KeyboardInterrupt (Ctrl+C) para salir elegantemente
3. Si se interrumpe: mostrar mensaje de despedida y salir con sys.exit(0)

ESTRUCTURA:
try:
    jugar()
except KeyboardInterrupt:
    # mostrar mensaje
    # salir con sys.exit(0)
```

**Tareas**:
1. Importa `sys` al inicio del archivo
2. Implementa el try-except según la estructura
3. Agrega al final del archivo:
   ```python
   if __name__ == '__main__':
       principal()
   ```

---

## 📝 Notas Importantes para Todos

### Imports Necesarios

Cada archivo debe importar lo que necesita:

- **datos_palabras.py**: `import random`
- **validacion.py**: ninguno
- **evaluacion.py**: debe importar `from datos_palabras import *` (solo si usas funciones de ahí)
- **pantalla.py**: ninguno
- **manejo_entrada.py**: `from validacion import validar_intento`
- **principal.py**: 
  ```python
  import sys
  from datos_palabras import seleccionar_palabra_secreta
  from validacion import verificar_victoria
  from evaluacion import evaluar_intento
  from pantalla import (mostrar_mensaje_bienvenida, mostrar_retroalimentacion,
                        mostrar_mensaje_victoria, mostrar_mensaje_derrota)
  from manejo_entrada import obtener_intento_jugador
  ```

### Reglas de Git para el Taller

1. Clona el repositorio
2. Crea una rama con tu nombre: `git checkout -b feat/nombre-rama`
3. Crea tu archivo asignado
4. Haz commits frecuentes con mensajes descriptivos
5. Cuando termines, haz push de tu rama
6. El instructor integrará todas las ramas en `staging`

### Testing Individual

Puedes probar tu archivo individualmente creando un pequeño script de prueba, pero NO lo incluyas en el commit final.

---

## ✅ Checklist de Entrega

Antes de hacer tu commit final, verifica:

- [ ] El nombre del archivo es exactamente como se especifica
- [ ] Los nombres de las funciones son exactos (respetan mayúsculas/minúsculas)
- [ ] Los parámetros tienen los nombres y orden correctos
- [ ] Los tipos de retorno son los especificados
- [ ] Incluiste los imports necesarios
- [ ] Tu código está comentado donde sea necesario
- [ ] Probaste que tu función hace lo que debe hacer

---
