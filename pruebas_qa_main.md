# Pruebas QA Manuales para main.py

## Introducción
Este documento contiene las pruebas QA manuales para el script `main.py`, que es la interfaz de usuario del sistema de inventario. Las pruebas se centran en el menú y las opciones de interacción, verificando que las entradas se procesen correctamente y se llamen las funciones apropiadas.

**Archivo bajo prueba:** `main.py`  
**Dependencias:** `logic.py`, `data_manager.py` y `inventario.json`  
**Herramientas necesarias:** Terminal para ejecutar Python, capacidad para ingresar inputs manualmente.

## Casos de Prueba

### Caso 1: Ejecutar el menú y seleccionar opción inválida
**ID:** QA_MAIN_001  
**Descripción:** Verificar que el menú se muestra y maneja opciones inválidas.  
**Precondiciones:** Ninguna específica.  
**Pasos:**
1. Ejecutar `python main.py` en la terminal.
2. Cuando aparezca el menú, ingresar "9" (opción inválida).
3. Observar la salida.  
**Resultado esperado:** Se imprime "❌ Opción inválida" y el menú se muestra nuevamente.  
**Resultado real:** [Completar durante la ejecución]

### Caso 2: Registrar un computador a través del menú
**ID:** QA_MAIN_002  
**Descripción:** Verificar que la opción 1 registra un computador correctamente.  
**Precondiciones:** Inventario vacío.  
**Pasos:**
1. Ejecutar `python main.py`.
2. Seleccionar opción "1".
3. Ingresar ID: "PC001", Marca: "Dell", Modelo: "Inspiron".
4. Verificar el mensaje y el archivo `inventario.json`.  
**Resultado esperado:** Se imprime "✅ Computador registrado." y el computador se agrega al inventario.  
**Resultado real:** [Completar durante la ejecución]

### Caso 3: Asignar un computador a través del menú
**ID:** QA_MAIN_003  
**Descripción:** Verificar que la opción 2 asigna un computador.  
**Precondiciones:** Un computador registrado y no asignado.  
**Pasos:**
1. Registrar un computador previamente.
2. Ejecutar `python main.py`.
3. Seleccionar opción "2".
4. Ingresar ID: "PC001", Camper: "Juan Pérez".
5. Verificar el mensaje y el inventario.  
**Resultado esperado:** Se imprime "✅ Computador asignado." y el campo asignado_a se actualiza.  
**Resultado real:** [Completar durante la ejecución]

### Caso 4: Ver inventario a través del menú
**ID:** QA_MAIN_004  
**Descripción:** Verificar que la opción 3 muestra el inventario.  
**Precondiciones:** Inventario con al menos un computador.  
**Pasos:**
1. Ejecutar `python main.py`.
2. Seleccionar opción "3".
3. Observar la salida.  
**Resultado esperado:** Se imprime la lista de computadores en formato legible.  
**Resultado real:** [Completar durante la ejecución]

### Caso 5: Actualizar estado a través del menú
**ID:** QA_MAIN_005  
**Descripción:** Verificar que la opción 4 actualiza el estado.  
**Precondiciones:** Un computador registrado.  
**Pasos:**
1. Ejecutar `python main.py`.
2. Seleccionar opción "4".
3. Ingresar ID: "PC001", Estado: "Dañado".
4. Verificar el mensaje y el inventario.  
**Resultado esperado:** Se imprime "✅ Estado actualizado." y el estado cambia.  
**Resultado real:** [Completar durante la ejecución]

### Caso 6: Salir del programa
**ID:** QA_MAIN_006  
**Descripción:** Verificar que la opción 5 sale del programa.  
**Precondiciones:** Ninguna específica.  
**Pasos:**
1. Ejecutar `python main.py`.
2. Seleccionar opción "5".
3. Observar que el programa termina.  
**Resultado esperado:** Se imprime "👋 Saliendo..." y el programa finaliza.  
**Resultado real:** [Completar durante la ejecución]

### Caso 7: Manejo de entradas no numéricas en el menú
**ID:** QA_MAIN_007  
**Descripción:** Verificar que entradas no válidas en el menú se manejen.  
**Precondiciones:** Ninguna específica.  
**Pasos:**
1. Ejecutar `python main.py`.
2. Ingresar "abc" en lugar de un número.
3. Observar la salida.  
**Resultado esperado:** Se imprime "❌ Opción inválida" (asumiendo que input() maneja strings).  
**Resultado real:** [Completar durante la ejecución]

## Notas Finales
- Las pruebas requieren interacción manual con la terminal.
- Limpiar el inventario entre pruebas.
- Registrar cualquier comportamiento inesperado.