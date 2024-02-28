from django.test import TestCase
from .ciphers import caesar_encode

# Create your tests here.
class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = "hello"
        shift = 1
        expected = "ifmmp"
        actual = caesar_encode(plain_text, shift)
        self.assertEqual(expected, actual)

    def test_caesar_encoding_2(self):
        plain_text = "winter"
        shift = 3
        expected = "zlqwhu"
        actual = caesar_encode(plain_text, shift)
        self.assertEqual(expected, actual)

    def test_caesar_encoding_3(self):
        plain_text = "hello"
        shift = 26
        expected = "hello"
        actual = caesar_encode(plain_text, shift)
        self.assertEqual(expected, actual)

    def test_caesar_encoding_4(self):
        plain_text = "texter"
        shift = 4
        expected = "xibxiv"
        actual = caesar_encode(plain_text, shift)
        self.assertEqual(expected, actual)