import base64
import random
import struct
import string

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
    # print("Key: " + str(key))
    return random_numbers, key


def encrypt_bytes(data: bytes, key: list):
    """encrypts the bytes using the given key"""
    buf = struct.pack("%sf" % len(key), *key)
    return xor_bytes(data, buf)


def decrypt_bytes(data: bytes, key: bytes):
    """decrypts the given bytes with the key"""
    return _enc_XOR_bytes(data, key)


def encrypt_string(data: str, key: list):
    """encrypts the string using the given key"""
    # convert key list to string
    key_str = "".join(key)
    return _enc_XOR_string(data, key)


def decrypt_string(data, key):
    """decrypts the given bytes with the key"""
    return _enc_XOR_string(data, key)


def get_base64encode_data(data: str):
    """returns the base64 encoded data"""
    return base64.b64encode(bytes(data, "utf-8"))


def get_base64encode_from_bytes(data: bytes):
    """returns the base64 encoded data"""
    return base64.b64encode(data)


def get_base64encode_from_bytes(data: bytes):
    """returns the base64 encoded data"""
    return base64.b64encode(data)


def get_base64decode_data(data: bytes):
    """returns the base64 decoded data"""
    return bytes(base64.b64decode(data)).decode("utf-8")


def _enc_XOR_string(data: bytes, key: bytes):
    """XORs the data with the key"""
    if len(data) != len(key):
        raise ValueError("Strings must be the same length")

    return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(data, key)])


def _enc_XOR_bytes(data: bytes, key: bytes):
    """XORs the data with the key"""
    if len(data) != len(key):
        raise ValueError("data must be the same length")

    return bytes([a ^ b for a, b in zip(data, key)])


def xor_bytes(data, key):
    return bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key])))
