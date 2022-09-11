import sys
from collections import Counter
from math import log

from crypto.core import (
    decrypt_string,
    encrypt_bytes,
    encrypt_string,
    generate_symbolic_key,
    get_base64decode_data,
    get_base64encode_data,
    get_base64encode_from_bytes,
)
from symbolic_src.genepool import generate_key_function
from util.dataprocessor import process_csv

FOMATTED_DATA_PATH = "data/formatted_data.csv"
INPUT_DATA_FILE_PATH = "data/raw_data.csv"


def calculate_string_entropy(string: str):
    counts = Counter(string)
    freq = ((i / len(string)) for i in counts.values())
    str_entropy = sum(-f * log(f, 2) for f in freq)
    print(str_entropy)


def encrypt_string_as_bytes_with_symbolic_key(message: str):
    input, key = generate_symbolic_key(len(message))
    enc_bytes = encrypt_bytes(message.encode(), key)
    b64string = get_base64encode_from_bytes(enc_bytes)
    print(enc_bytes)
    print(b64string)
    calculate_string_entropy(enc_bytes)
    return b64string


def encrypt_string_with_symbolic_key(message: str):
    input, key = generate_symbolic_key(len(message))
    enc_string = encrypt_string(message, key)
    b64string = get_base64encode_data(enc_string)
    print(enc_string)
    print(b64string)
    calculate_string_entropy(message)
    calculate_string_entropy(enc_string)
    write_encrypted_string_to_file(enc_string)

    return b64string


def decrypt_string_with_symbolic_key(b64_enc_str: str, b64_key: str):
    key = get_base64decode_data(b64_key)
    enc_string = get_base64decode_data(b64_enc_str)
    dec_string = decrypt_string(enc_string, key)
    print("Decrypted String: " + dec_string)

    return dec_string


def write_encrypted_string_to_file(enc_string: str):
    # convert enc_string to binary
    binary_string = bytearray(enc_string, "utf-8")
    with open("encrypted_data.enc", "ab") as f:
        f.write(binary_string)


if __name__ == "__main__":
    """Main entry point of the app"""

    if len(sys.argv) > 1:
        if sys.argv[1] == "generate":
            if len(sys.argv) > 2:
                generate_key_function(FOMATTED_DATA_PATH, sys.argv[2])
            else:
                generate_key_function(FOMATTED_DATA_PATH)
        elif sys.argv[1] == "process":
            process_csv(INPUT_DATA_FILE_PATH, FOMATTED_DATA_PATH)
        elif sys.argv[1] == "encrypt":
            encrypt_string_as_bytes_with_symbolic_key(sys.argv[2])
        elif sys.argv[1] == "decrypt":
            decrypt_string_with_symbolic_key(sys.argv[2], sys.argv[3])
    else:
        print("To process data: process")
        print("To generate key function: generate")
        print("To encrypt string: encrypt <string>")
        print("To decrypt string: decrypt <b64_enc_str> <b64_key>")
        print("To generate key function with custom rounds: generate <rounds>")
