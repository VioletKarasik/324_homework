import unittest
from caesar_cipher import caesar_encrypt, caesar_decrypt

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_lowercase(self):
        self.assertEqual(caesar_encrypt("hello", 3), "khoor")
    
    def test_encrypt_uppercase(self):
        self.assertEqual(caesar_encrypt("WORLD", 5), "BTWQI")
    
    def test_encrypt_mixed_case(self):
        self.assertEqual(caesar_encrypt("Hello World", 4), "Lipps Asvph")
    
    def test_encrypt_with_non_letters(self):
        self.assertEqual(caesar_encrypt("Hello, World! 123", 1), "Ifmmp, Xpsme! 123")
    
    def test_decrypt_lowercase(self):
        self.assertEqual(caesar_decrypt("khoor", 3), "hello")
    
    def test_decrypt_uppercase(self):
        self.assertEqual(caesar_decrypt("BTWQI", 5), "WORLD")
    
    def test_encrypt_decrypt_consistency(self):
        original = "The Quick Brown Fox"
        encrypted = caesar_encrypt(original, 7)
        decrypted = caesar_decrypt(encrypted, 7)
        self.assertEqual(original, decrypted)
    
    def test_large_shift(self):
        self.assertEqual(caesar_encrypt("abc", 6), "ghi")  # 6 % 26 = 6


if __name__ == "__main__":
    unittest.main()