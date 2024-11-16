import re
import logging
import os


logging.basicConfig(
    filename=os.path.join('logs', 'validation.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class EmailValidator:
    def __init__(self):
        self.regex = re.compile(r'([A-Za-z]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def validar(self, correo: str):
        try:
            if not isinstance(correo, str):
                raise ValueError("El correo debe ser una cadena de texto.")
            if re.fullmatch(self.regex, correo):
                logging.info(f"Validación exitosa: {correo} es válido.")
                return True
            else:
                logging.warning(f"Validación fallida: {correo} no es válido.")
                return False
        except ValueError as ve:
            logging.error(f"Error de valor: {ve}")
            raise
        except Exception as e:
            logging.error(f"Error inesperado en la validación de {correo}: {e}")
            raise
