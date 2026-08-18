# Normas de Testing para ShellGPT (Fork con Gemini)

Este documento define la estrategia y las normas de testing para garantizar el correcto funcionamiento de la integración de los modelos de Gemini en ShellGPT.

## 1. Alcance de las Pruebas

Las pruebas deben cubrir la correcta configuración, el enrutamiento de los modelos según la operación solicitada y la integración con la librería `litellm`.

Modelos integrados:
- `gemini-pro-latest`: Por defecto (razonamiento/planificación).
- `gemini-flash-latest`: Para comandos `--shell` y `--code` (ejecución/generación).
- `gemini-flash-lite-latest`: Para el comando `--describe-shell` (procesamiento ligero).

## 2. Pruebas Unitarias

- **Configuración (`sgpt/config.py`):** 
  - Verificar que las variables de entorno o constantes relacionadas con Gemini se cargan correctamente.
  - Comprobar que los valores por defecto de los modelos son los esperados.
- **Enrutamiento (`sgpt/app.py`):**
  - Asegurar que la lógica de selección de modelo elige `gemini-flash-latest` cuando se usan las opciones `--shell` o `--code`.
  - Asegurar que elige `gemini-flash-lite-latest` cuando se usa `--describe-shell`.
  - Asegurar que elige `gemini-pro-latest` cuando no se pasan flags específicos (comportamiento por defecto).

## 3. Pruebas de Integración y Mocks

- **Integración con LiteLLM:**
  - Mockear las llamadas a la API generadora (ej. `litellm` / `openai`) para interceptar el parámetro `model` enviado.
  - Validar que el nombre del modelo enviado coincida exactamente con la regla de enrutamiento definida.
- **Manejo de Errores:**
  - Simular fallos de red o errores de autenticación (API Key inválida) y verificar que la herramienta los maneja adecuadamente.

## 4. Pruebas End-to-End (E2E)

- Ejecutar los comandos reales de la CLI en un entorno controlado (usando mocks para no consumir tokens reales):
  - `sgpt "Hola mundo"` -> Debe usar `gemini-pro-latest`.
  - `sgpt --shell "actualizar sistema"` -> Debe usar `gemini-flash-latest`.
  - `sgpt --code "fibonacci en python"` -> Debe usar `gemini-flash-latest`.
  - `sgpt --describe-shell "ls -la"` -> Debe usar `gemini-flash-lite-latest`.

## 5. Gestión de Dependencias

- Verificar mediante pruebas o linters que `pyproject.toml` requiere `litellm >= 1.97.0`.

## 6. Ejecución de Pruebas

- Todas las pruebas deben ejecutarse utilizando `pytest` en el directorio `tests/`.
- Validar mediante el script `scripts/test.sh`.

## 7. Pruebas de Memoria a Largo Plazo (RAG con ChromaDB)

- **Dependencias (`pyproject.toml`):**
  - Verificar que `chromadb` está incluido en las dependencias.
- **Persistencia y Acceso (`sgpt/memory.py`):**
  - Comprobar que la inicialización de ChromaDB crea la base de datos en `~/.config/shell_gpt/memory` (o un directorio temporal en las pruebas).
  - Validar que el método `save_memory(topic: str, fact: str)` utiliza `upsert` en ChromaDB pasando el parámetro `topic` como el ID del documento, en lugar de generar un UUID aleatorio.
  - Asegurar que si se guarda un nuevo `fact` con un `topic` ya existente, el documento anterior se sobrescribe o actualiza correctamente (comportamiento de upsert).
  - Validar el método `get_relevant_memories` con operaciones de lectura/escritura y búsqueda semántica básica.
- **Herramienta LLM (`sgpt/llm_functions/common/save_memory.py`):**
  - Verificar que la función `save_memory` está correctamente expuesta como una tool compatible con el esquema de OpenAI/LiteLLM.
- **Inyección en el Prompt (`sgpt/handlers/handler.py`):**
  - Mockear `get_relevant_memories` y comprobar que el texto recuperado se incluye correctamente en el system prompt antes de enviarlo al LLM.
- **Comportamiento del Rol por Defecto (`sgpt/role.py`):**
  - Revisar que el `DEFAULT_ROLE` incluye instrucciones claras para que el LLM use la herramienta `save_memory` de forma proactiva.
- **Inicialización de Memoria (`sgpt/app.py`):**
  - Probar el flag `--init-memory` verificando que lanza el proceso de escaneo de memoria automático sin errores.
