import pytest
from crypto.core import (
    decrypt_bytes,
    decrypt_string,
    encrypt_bytes,
    encrypt_string,
    generate_basic_key,
    generate_symbolic_key,
)


class TestCrypto:
    def test_basic_key_generation(self):
        """Test that the basic key generation works as expected."""
        key = generate_basic_key(10)
        assert key is not None
        assert len(key) == 10

    def test_symbolic_key_generation(self):
        """Test that the symbolic key generation works as expected."""
        _, key = generate_symbolic_key(10)
        assert key is not None
        assert len(key) == 10

    def test_encryption(self):
        """Test that the encryption and decryption functions work as expected."""
        testStr = "THIS IS A TEST STRING"
        key = "THIS IS A TEST STRING"
        enc = encrypt_string(testStr, key)
        assert testStr != enc
        dec = decrypt_string(enc, key)
        assert testStr == dec

    def test_encryption_with_incorrect_key_gives_rubbish(self):
        """Test that the wrong key does not return correct results."""
        testStr = "THIS IS A TEST STRING"
        key = "THIS IS A TEST STRING"
        enc = encrypt_string(testStr, key)
        assert testStr != enc
        key = "THIS IS NOT STRING!!!"
        dec = decrypt_string(enc, key)
        assert testStr != dec

    def test_encryption_throws_exception_if_key_is_incorrect_length(self):
        """Test that the key of the wrong length gives an exception"""
        testStr = "THIS IS A TEST STRING"
        key = "THIS IS THE WRONG LENGTH KEY"
        with pytest.raises(ValueError):
            enc = encrypt_string(testStr, key)

    def test_decryption_throws_exception_if_key_is_incorrect_length(self):
        """Test that the key of the wrong length gives an exception"""
        testStr = "THIS IS A TEST STRING"
        key = "THIS IS THE WRONG LENGTH KEY"
        with pytest.raises(ValueError):
            edecnc = decrypt_string(testStr, key)

    def test_encryption_with_saved_symbolic_function(self):
        """Test that the encryption and decryption functions work as expected."""
        testStr = "THIS IS A TEST STRING"
        _, key = generate_symbolic_key(len(testStr))
        enc = encrypt_string(testStr, key)
        assert testStr != enc

    def test_decryption_with_saved_symbolic_function(self):
        """Test that the encryption and decryption functions work as expected."""
        testStr = "THIS IS A TEST STRING"
        _, key = generate_symbolic_key(len(testStr))
        enc = encrypt_string(testStr, key)
        assert testStr != enc
        dec = decrypt_string(enc, key)
        assert testStr == dec

    def test_encryption_can_encrypt_very_long_strings(self):
        """Test that the encryption and decryption functions work as expected."""
        testStr = "THIS IS A TEST STRING" * 1000
        _, key = generate_symbolic_key(len(testStr))
        enc = encrypt_string(testStr, key)
        assert testStr != enc
        dec = decrypt_string(enc, key)
        assert testStr == dec

    def test_encryption_works_for_byte_array(self):
        """Test that ecrypt_bytes works as expected."""
        testStr = "THIS IS A TEST STRING"
        key = "THIS IS A TEST STRING"
        enc = encrypt_bytes(testStr.encode(), key.encode())
        assert testStr.encode() != enc
        dec = decrypt_bytes(enc, key.encode())
        assert testStr.encode() == dec
