import unittest
from src.bil import Bil

class TestBil(unittest.TestCase):
    def test_antal_hjul(self):
        min_bil = Bil("Volkswagen Golf", 300000)
        self.assertEqual(min_bil.hjul, 4)