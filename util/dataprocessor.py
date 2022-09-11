from genericpath import isfile
import os


def process_csv(inPath: str, outPath: str):
    """
    process the data file to the correct format expected (NN NN)
    """
    # check if file exists
    if not os.path.isfile(inPath):
        raise FileNotFoundError("File not found")

    if os.path.isfile(outPath):
        print("Deleting old " + outPath)
        os.remove(outPath)

    with open(inPath, "r") as f:
        lines = f.readlines()
    with open(outPath, "w") as outf:
        for line in lines:
            outf.write(line.replace("	", ","))

    print("Processing complete.")
