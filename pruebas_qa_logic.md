# Pruebas QA Manuales para logic.py

## Introducción
Este documento contiene las pruebas QA manuales para el módulo `logic.py`. Las pruebas se centran en las funciones `register_computer()`, `assign_computer()`, `update_status()` y `view_inventory()`, verificando su comportamiento en diferentes escenarios, incluyendo casos normales, de borde y de error.

**Archivo bajo prueba:** `logic.py`  
**Dependencias:** `data_manager.py` y archivo `inventario.json`  
**Herramientas necesarias:** Editor de texto, terminal para ejecutar Python, acceso al sistema de archivos.

## Casos de Prueba

### Caso 1: Registrar un computador nuevo
**ID:** QA_LG_001  
**Descripción:** Verificar que `register_computer()` registra un computador correctamente cuando no existe.  
**Precondiciones:** Inventario vacío o sin el ID especificado.  
**Pasos:**
1. Asegurarse de que el inventario esté vacío o no contenga el ID "PC001".
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import register_computer
   result = register_computer("PC001", "Dell", "Inspiron")
   print(result)
   ```
3. Verificar el contenido de `inventario.json`.  
**Resultado esperado:** Se imprime "✅ Computador registrado." y el archivo contiene el nuevo computador con estado "Excelente" y asignado_a None.  
**Resultado real:** [Completar durante la ejecución]

### Caso 2: Intentar registrar un computador que ya existe
**ID:** QA_LG_002  
**Descripción:** Verificar que `register_computer()` rechaza el registro si el ID ya existe.  
**Precondiciones:** Un computador con ID "PC001" ya registrado.  
**Pasos:**
1. Registrar previamente un computador con ID "PC001".
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import register_computer
   result = register_computer("PC001", "HP", "Pavilion")
   print(result)
   ```
3. Verificar que el inventario no cambia.  
**Resultado esperado:** Se imprime "❌ El computador ya existe." y el inventario permanece sin cambios.  
**Resultado real:** [Completar durante la ejecución]

### Caso 3: Asignar un computador disponible
**ID:** QA_LG_003  
**Descripción:** Verificar que `assign_computer()` asigna correctamente un computador no asignado.  
**Precondiciones:** Un computador registrado y no asignado.  
**Pasos:**
1. Registrar un computador con ID "PC001".
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import assign_computer
   result = assign_computer("PC001", "Juan Pérez")
   print(result)
   ```
3. Verificar el contenido de `inventario.json`.  
**Resultado esperado:** Se imprime "✅ Computador asignado." y el campo "asignado_a" se actualiza a "Juan Pérez".  
**Resultado real:** [Completar durante la ejecución]

### Caso 4: Intentar asignar un computador ya asignado
**ID:** QA_LG_004  
**Descripción:** Verificar que `assign_computer()` rechaza la asignación si ya está asignado.  
**Precondiciones:** Un computador ya asignado.  
**Pasos:**
1. Asignar un computador a alguien.
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import assign_computer
   result = assign_computer("PC001", "Ana López")
   print(result)
   ```
3. Verificar que el inventario no cambia.  
**Resultado esperado:** Se imprime "❌ Ya está asignado." y el campo "asignado_a" permanece igual.  
**Resultado real:** [Completar durante la ejecución]

### Caso 5: Asignar un computador que no existe
**ID:** QA_LG_005  
**Descripción:** Verificar que `assign_computer()` maneja IDs inexistentes.  
**Precondiciones:** Ninguna específica.  
**Pasos:**
1. Ejecutar el siguiente código en Python:
   ```python
   from logic import assign_computer
   result = assign_computer("PC999", "Juan Pérez")
   print(result)
   ```
**Resultado esperado:** Se imprime "❌ Computador no encontrado.".  
**Resultado real:** [Completar durante la ejecución]

### Caso 6: Actualizar estado a un valor válido
**ID:** QA_LG_006  
**Descripción:** Verificar que `update_status()` actualiza el estado correctamente.  
**Precondiciones:** Un computador registrado.  
**Pasos:**
1. Registrar un computador.
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import update_status
   result = update_status("PC001", "Dañado")
   print(result)
   ```
3. Verificar el contenido de `inventario.json`.  
**Resultado esperado:** Se imprime "✅ Estado actualizado." y el estado cambia a "Dañado".  
**Resultado real:** [Completar durante la ejecución]

### Caso 7: Actualizar estado con valor inválido
**ID:** QA_LG_007  
**Descripción:** Verificar que `update_status()` rechaza estados inválidos.  
**Precondiciones:** Un computador registrado.  
**Pasos:**
1. Ejecutar el siguiente código en Python:
   ```python
   from logic import update_status
   result = update_status("PC001", "Roto")
   print(result)
   ```
**Resultado esperado:** Se imprime "❌ Estado inválido." y el estado no cambia.  
**Resultado real:** [Completar durante la ejecución]

### Caso 8: Ver inventario vacío
**ID:** QA_LG_008  
**Descripción:** Verificar que `view_inventory()` maneja un inventario vacío.  
**Precondiciones:** Inventario vacío.  
**Pasos:**
1. Asegurarse de que `inventario.json` esté vacío o no exista.
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import view_inventory
   result = view_inventory()
   print(result)
   ```
**Resultado esperado:** Se imprime "📭 Inventario vacío.".  
**Resultado real:** [Completar durante la ejecución]

### Caso 9: Ver inventario con datos
**ID:** QA_LG_009  
**Descripción:** Verificar que `view_inventory()` muestra correctamente la lista de computadores.  
**Precondiciones:** Al menos un computador registrado.  
**Pasos:**
1. Registrar y asignar algunos computadores.
2. Ejecutar el siguiente código en Python:
   ```python
   from logic import view_inventory
   result = view_inventory()
   print(result)
   ```
**Resultado esperado:** Se imprime una lista formateada con los detalles de los computadores.  
**Resultado real:** [Completar durante la ejecución]

## Notas Finales
- Limpiar el inventario entre pruebas para evitar interferencias.
- Registrar cualquier desviación y reportar bugs si corresponde.