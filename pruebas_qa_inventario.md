# Pruebas QA Manuales para inventario.json

## Introducción
Este documento contiene las pruebas QA manuales para el archivo `inventario.json`, que almacena los datos del inventario. Las pruebas se centran en la validación del formato JSON y la estructura de los datos.

**Archivo bajo prueba:** `inventario.json`  
**Herramientas necesarias:** Editor de texto, terminal para ejecutar Python o herramientas de validación JSON.

## Casos de Prueba

### Caso 1: Validar formato JSON válido
**ID:** QA_INV_001  
**Descripción:** Verificar que el archivo sea un JSON válido.  
**Precondiciones:** Archivo `inventario.json` existe.  
**Pasos:**
1. Abrir `inventario.json` en un editor.
2. Usar una herramienta de validación JSON (ej. `python -m json.tool inventario.json` en terminal).
3. Verificar que no haya errores.  
**Resultado esperado:** El archivo se valida sin errores de sintaxis.  
**Resultado real:** [Completar durante la ejecución]

### Caso 2: Verificar estructura de datos (lista de objetos)
**ID:** QA_INV_002  
**Descripción:** Verificar que el contenido sea una lista de objetos con campos requeridos.  
**Precondiciones:** Archivo con datos.  
**Pasos:**
1. Abrir `inventario.json`.
2. Verificar que sea una lista `[]`.
3. Cada objeto debe tener: "id", "marca", "modelo", "estado", "asignado_a".  
**Resultado esperado:** La estructura coincide con el esquema esperado.  
**Resultado real:** [Completar durante la ejecución]

### Caso 3: Verificar archivo vacío
**ID:** QA_INV_003  
**Descripción:** Verificar que un archivo vacío o con lista vacía sea válido.  
**Precondiciones:** Archivo con `[]`.  
**Pasos:**
1. Verificar contenido.
2. Validar con herramienta JSON.  
**Resultado esperado:** Se valida correctamente como lista vacía.  
**Resultado real:** [Completar durante la ejecución]

## Notas Finales
- Este archivo es generado/modificado por `data_manager.py`, así que las pruebas aquí son para validación post-generación.