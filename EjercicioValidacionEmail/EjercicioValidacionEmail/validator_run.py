from emails.validator import EmailValidator


validator = EmailValidator()


correos = [
    "test@example.com",
    "nombre.apellido@dominio.co",
    "test@.com",
    "usuario@dominio",
    "usuario@dominio.123",
    "usuario@dominio..com",
]


for correo in correos:
    if validator.validar(correo):
        print(f"{correo} es válido.")
    else:
        print(f"{correo} no es válido.")
