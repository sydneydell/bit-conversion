import numpy as np
import pandas as pd
import os
import sys

# Read data from the text file
def read_text_file(filename):
    data = pd.read_csv(filename, delimiter='\s+', header=None)
    return data

# Write data to a 16 bit csv file
def write_16_bit_file(data, output_filename):
    num_samples, num_channels = data.shape
    
    for i in range(num_channels-1):
        data.iloc[:, i] = (data.iloc[:, i] * (32767 / data.iloc[:, i].abs().max())).astype(np.int16)

    data.to_csv(output_filename, index=False)        


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_filename> <output_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not os.path.isfile(input_filename):
        print("Error: Input file does not exist.")
        sys.exit(1)

    # Read data from text file
    data = read_text_file(input_filename)

    # Write data to EDF file
    write_16_bit_file(data, output_filename)

    print("Conversion completed successfully.")
