# Pruebas QA Manuales para data_manager.py

## Introducción
Este documento contiene las pruebas QA manuales para el módulo `data_manager.py`. Las pruebas se centran en las funciones `load_data()` y `save_data()`, verificando su comportamiento en diferentes escenarios, incluyendo casos normales, de borde y de error.

**Archivo bajo prueba:** `data_manager.py`  
**Dependencias:** Archivo `inventario.json` (se crea/modifica durante las pruebas)  
**Herramientas necesarias:** Editor de texto, terminal para ejecutar Python, acceso al sistema de archivos.

## Casos de Prueba

### Caso 1: Cargar datos cuando el archivo no existe
**ID:** QA_DM_001  
**Descripción:** Verificar que `load_data()` devuelve una lista vacía cuando el archivo `inventario.json` no existe.  
**Precondiciones:** El archivo `inventario.json` no debe existir en el directorio.  
**Pasos:**
1. Asegurarse de que `inventario.json` no existe (eliminarlo si es necesario).
2. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import load_data
   result = load_data()
   print(result)
   ```
3. Observar la salida en la consola.  
**Resultado esperado:** Se imprime `[]` (lista vacía). No se crea ningún archivo nuevo.  
**Resultado real:** [Completar durante la ejecución]

### Caso 2: Cargar datos desde un archivo válido
**ID:** QA_DM_002  
**Descripción:** Verificar que `load_data()` carga correctamente datos JSON válidos.  
**Precondiciones:** Crear un archivo `inventario.json` con contenido JSON válido, por ejemplo: `[{"id": 1, "nombre": "Producto A", "cantidad": 10}]`.  
**Pasos:**
1. Crear o editar `inventario.json` con datos válidos.
2. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import load_data
   result = load_data()
   print(result)
   ```
3. Observar la salida en la consola.  
**Resultado esperado:** Se imprime la lista de datos cargados, por ejemplo: `[{'id': 1, 'nombre': 'Producto A', 'cantidad': 10}]`.  
**Resultado real:** [Completar durante la ejecución]

### Caso 3: Cargar datos desde un archivo JSON corrupto
**ID:** QA_DM_003  
**Descripción:** Verificar que `load_data()` maneja archivos JSON corruptos y muestra un mensaje de advertencia.  
**Precondiciones:** Crear un archivo `inventario.json` con contenido JSON inválido, por ejemplo: `{"id": 1, "nombre": "Producto A", "cantidad": 10` (falta cierre).  
**Pasos:**
1. Crear o editar `inventario.json` con datos corruptos.
2. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import load_data
   result = load_data()
   print(result)
   ```
3. Observar la salida en la consola y verificar el mensaje impreso.  
**Resultado esperado:** Se imprime `⚠️ Archivo JSON corrupto. Reiniciando datos...` y luego `[]` (lista vacía).  
**Resultado real:** [Completar durante la ejecución]

### Caso 4: Guardar datos válidos
**ID:** QA_DM_004  
**Descripción:** Verificar que `save_data()` guarda correctamente una lista de datos en `inventario.json`.  
**Precondiciones:** Ninguna específica.  
**Pasos:**
1. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import save_data
   data = [{"id": 1, "nombre": "Producto A", "cantidad": 10}]
   save_data(data)
   ```
2. Verificar el contenido del archivo `inventario.json` con un editor de texto.  
**Resultado esperado:** El archivo `inventario.json` contiene el JSON formateado correctamente:  
```json
[
    {
        "id": 1,
        "nombre": "Producto A",
        "cantidad": 10
    }
]
```  
**Resultado real:** [Completar durante la ejecución]

### Caso 5: Guardar datos vacíos
**ID:** QA_DM_005  
**Descripción:** Verificar que `save_data()` maneja correctamente una lista vacía.  
**Precondiciones:** Ninguna específica.  
**Pasos:**
1. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import save_data
   data = []
   save_data(data)
   ```
2. Verificar el contenido del archivo `inventario.json` con un editor de texto.  
**Resultado esperado:** El archivo `inventario.json` contiene `[]` (lista vacía en JSON).  
**Resultado real:** [Completar durante la ejecución]

### Caso 6: Manejo de errores en save_data (permisos insuficientes)
**ID:** QA_DM_006  
**Descripción:** Verificar que `save_data()` maneja errores de permisos y muestra un mensaje de error.  
**Precondiciones:** Cambiar los permisos del directorio para que no se pueda escribir (en sistemas Unix: `chmod 444 .` o similar). Nota: Restaurar permisos después.  
**Pasos:**
1. Cambiar permisos del directorio para denegar escritura.
2. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import save_data
   data = [{"id": 1, "nombre": "Producto A", "cantidad": 10}]
   save_data(data)
   ```
3. Observar la salida en la consola.
4. Restaurar permisos del directorio.  
**Resultado esperado:** Se imprime un mensaje de error como `Error al guardar datos: [descripción del error]`. El archivo no se modifica.  
**Resultado real:** [Completar durante la ejecución]

### Caso 7: Cargar datos con caracteres especiales (UTF-8)
**ID:** QA_DM_007  
**Descripción:** Verificar que `load_data()` y `save_data()` manejan correctamente caracteres especiales y UTF-8.  
**Precondiciones:** Crear `inventario.json` con caracteres especiales, por ejemplo: `[{"id": 1, "nombre": "Producto ñoño", "cantidad": 10}]`.  
**Pasos:**
1. Crear o editar `inventario.json` con caracteres UTF-8.
2. Ejecutar el siguiente código en Python:
   ```python
   from data_manager import load_data
   result = load_data()
   print(result)
   ```
3. Verificar que los caracteres se cargan correctamente.
4. Luego, guardar los mismos datos y verificar el archivo.  
**Resultado esperado:** Los caracteres especiales se imprimen y guardan correctamente sin corrupción.  
**Resultado real:** [Completar durante la ejecución]

## Notas Finales
- Después de cada prueba, limpiar el archivo `inventario.json` si es necesario para evitar interferencias.
- Registrar cualquier desviación en "Resultado real" y reportar bugs si corresponde.
- Estas pruebas asumen un entorno Python estándar. Ajustar según el sistema operativo.