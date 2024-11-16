import unittest
from ..emails.validator import EmailValidator


class TestValidateEmail(unittest.TestCase):

    def test_email_valid(self):
        validator = EmailValidator()
        self.assertTrue(validator.validar("test@example.com"))
        self.assertTrue(validator.validar("nombre.apellido@dominio.co"))

    def test_email_invalid(self):
        validator = EmailValidator()
        self.assertFalse(validator.validar("test@.com"))
        self.assertFalse(validator.validar("usuario@dominio"))
        self.assertFalse(validator.validar("usuario@dominio.123"))
        self.assertFalse(validator.validar("usuario@dominio..com"))


if __name__ == "__main__":
    unittest.main()
