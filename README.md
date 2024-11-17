
## Descripción del código

### `validator.py`

El archivo `validator.py` contiene la clase `EmailValidator`, que implementa la validación de correos electrónicos utilizando una expresión regular. El comportamiento principal de la clase es el siguiente:

1. **Validación de formato**: Usa una expresión regular para validar si un correo electrónico tiene el formato correcto.
2. **Manejo de errores**: Si el correo no es una cadena de texto, se lanza una excepción `ValueError`. Si ocurre un error inesperado durante la validación, también se maneja y se registra en un archivo de log.
3. **Archivos de log**: Se guarda un archivo de log (`logs/validation.log`) con el resultado de cada validación: éxito o fallo.

### `validator_run.py`

Este script contiene un conjunto de correos electrónicos para probar la validación. El script crea una instancia de la clase `EmailValidator` y valida una lista de correos electrónicos. Los resultados de las validaciones se imprimen en la terminal.

### `validation.log`

El archivo de log (`validation.log`) guarda los resultados de las validaciones, incluyendo las direcciones de correo electrónico y el tipo de validación (si fue exitosa o fallida).

