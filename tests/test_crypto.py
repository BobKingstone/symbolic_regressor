import numpy as np
from crypto.core import (
    decrypt_nparray,
    encrypt_nparray,
    encrypt_string,
    decrypt_string,
    encrypt_xor_bytes,
    generate_basic_key,
    generate_byte_array_symbolic_key,
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

    def test_encrypt_xor_bytes(self):
        testStr = "THIS IS A TEST STRING"
        test_bytes = bytes(testStr, "utf-8")
        key = bytes("THIS IS A TEST STRING", "utf-8")
        enc_bytes = encrypt_xor_bytes(test_bytes, key)
        assert enc_bytes is not None
        assert len(enc_bytes) == len(test_bytes)

    def test_decrypt_bytes(self):
        testStr = "THIS IS A TEST STRING"
        test_bytes = bytes(testStr, "utf-8")
        key = bytes("THIS IS A TEST STRING", "utf-8")
        enc_bytes = encrypt_xor_bytes(test_bytes, key)
        dec_bytes = encrypt_xor_bytes(enc_bytes, key)
        assert dec_bytes != enc_bytes
        assert dec_bytes == test_bytes
        assert dec_bytes.decode("utf-8") == testStr

    def test_encryption_works_with_symbolic_key(self):
        testStr = "THIS IS A TEST STRING"
        _, key = generate_byte_array_symbolic_key(len(testStr))
        print(key)
        enc_bytes = encrypt_xor_bytes(testStr.encode(), key)
        assert enc_bytes is not None
        assert len(enc_bytes) == len(testStr)
        assert enc_bytes != testStr.encode()

    def test_decryption_works_with_symbolic_key(self):
        testStr = "THIS IS A TEST STRING"
        _, key = generate_byte_array_symbolic_key(len(testStr))
        enc_bytes = encrypt_xor_bytes(testStr.encode(), key)
        dec_bytes = encrypt_xor_bytes(enc_bytes, key)
        assert dec_bytes != enc_bytes
        assert dec_bytes == testStr.encode()
        assert dec_bytes.decode("utf-8") == testStr

    def test_string_encryption_works(self):
        testStr = "THIS IS A TEST STRING"
        enc_bytes, _ = encrypt_string(testStr)
        assert enc_bytes is not None
        assert len(enc_bytes) == len(testStr)
        assert enc_bytes != testStr.encode()

    def test_string_decryption_works(self):
        testStr = "THIS IS A TEST STRING"
        enc_bytes, key = encrypt_string(testStr)
        dec_bytes = decrypt_string(enc_bytes, key)
        assert dec_bytes != enc_bytes
        assert dec_bytes == testStr

    def test_encrypt_np_array(self):
        test_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        enc_bytes, _ = encrypt_nparray(test_array)
        assert enc_bytes is not None

    def test_decrypt_np_array(self):
        test_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        enc_bytes, key = encrypt_nparray(test_array)
        dec_array = decrypt_nparray(enc_bytes, key)
        assert dec_array is not None
        assert (dec_array == test_array).all()
