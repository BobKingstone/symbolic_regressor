import os
import sys
from collections import Counter
from math import log

from crypto.core import (
    decrypt_bytes,
    encrypt_bytes,
    generate_symbolic_key,
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


def write_encrypted_string_to_file(enc_string: str):
    # convert enc_string to binary
    binary_string = bytearray(enc_string, "utf-8")
    # delete file if it exists
    if os.path.isfile(FOMATTED_DATA_PATH):
        os.remove(FOMATTED_DATA_PATH)

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
            print("AHHHHHAHAHAHAHAH")
            generate_symbolic_key(10)
            # encrypt_string_as_bytes_with_symbolic_key(sys.argv[2])
    else:
        print("To process data: process")
        print("To generate key function: generate")
        print("To encrypt string: encrypt <string>")
        print("To decrypt string: decrypt <b64_enc_str> <b64_key>")
        print("To generate key function with custom rounds: generate <rounds>")
