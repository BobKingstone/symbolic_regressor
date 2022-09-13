from io import BytesIO
import base64
import random
import struct
import string

import numpy as np

from symbolic_src.chromosome import chromosome
from symbolic_src.genepool import load_key_function


def generate_basic_key(size):
    """
    generates a key of the given size
    """
    key = "".join(random.choice(string.ascii_letters) for _ in range(size))
    return key


def generate_symbolic_key(size: int):
    """
    Generates the key using the key function

    :param size: the size of the key
    :return: random_numbers used to generate key
    :return: the key
    :rtype: str

    """
    # generate random numbers the same length as the key
    random_numbers = [random.uniform(0, 1) for _ in range(size)]
    key_function = load_key_function()
    # compute the key
    key = []
    for i in range(size):
        key.append(key_function.compute_for_value(random_numbers[i]))
    print("Key: " + str(key))
    return random_numbers, key


def generate_byte_array_symbolic_key(size: int):
    random_numbers = [random.uniform(0, 1) for _ in range(size)]
    key_function = load_key_function()
    # create bytearray
    key = []
    for i in range(size):
        key.append(key_function.compute_for_value(random_numbers[i]))

    key_bytes = struct.pack("%sf" % len(key), *key)
    print(key_bytes)
    return random_numbers, key_bytes


def encrypt_string(data: str):
    """Encrypts the given string using a symbolic generated key."""
    _, key = generate_byte_array_symbolic_key(len(data))
    enc_bytes = encrypt_xor_bytes(data.encode("utf-8"), key)
    return enc_bytes, key


def decrypt_string(data: bytes, key: bytes):
    """Decrypts the data using the key"""
    dec_bytes = encrypt_xor_bytes(data, key)
    return dec_bytes.decode("utf-8")


def encrypt_nparray(data: np.array):
    """XORs the data with the key"""
    np_bytes = BytesIO()
    np.save(np_bytes, data, allow_pickle=False)
    nparray = np_bytes.getvalue()
    _, key = generate_byte_array_symbolic_key(len(nparray))
    return encrypt_xor_bytes(nparray, key), key


def decrypt_nparray(data: bytes, key: bytes):
    """Decrypts the data using the key"""
    dec_bytes = encrypt_xor_bytes(data, key)
    np_bytes = BytesIO(dec_bytes)
    return np.load(np_bytes, allow_pickle=False)


def get_base64encode_data(data: str):
    """returns the base64 encoded data"""
    return base64.b64encode(bytes(data, "utf-8"))


def get_base64encode_from_bytes(data: bytes):
    """returns the base64 encoded data"""
    return base64.b64encode(data)


def get_base64encode_from_bytes(data: bytes):
    """returns the base64 encoded data"""
    return base64.b64encode(data)


def encrypt_xor_bytes(data: bytes, key: bytes):
    """XORs the data with the key"""
    return bytes(a ^ b for a, b in zip(data, key))
