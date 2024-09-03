# 16-Bit CSV File Converter

This Python script reads data from a text file, performs 16-bit conversion on the data, and writes it to a new CSV file. Below is a detailed overview of the script's functionality and usage.

## Features

- **Data Conversion**: The script reads data from a text file and converts it to 16-bit integer format.
- **Customizable**: Users can specify the input and output filenames as command-line arguments.

## Requirements

- Python 3.x
- NumPy
- Pandas

## Usage

```bash
python script.py <input_filename> <output_filename>
```

- **<input_filename>**: The path to the input text file containing the data to be converted.
- **<output_filename>**: The path to the output CSV file where the converted data will be saved.

## Script Overview

- **read_text_file(filename)**: 
    - Reads data from the specified text file using Pandas.
    - Returns a Pandas DataFrame containing the read data.

- **write_16_bit_file(data, output_filename)**: 
    - Performs 16-bit conversion on the data.
    - Writes the converted data to a new CSV file specified by `output_filename`.

- **Main Execution**:
    - Checks if the correct number of command-line arguments is provided.
    - Verifies if the input file exists.
    - Reads data from the input file.
    - Converts the data to 16-bit format.
    - Writes the converted data to the output file.
    - Prints a success message upon completion.

## Notes

- Ensure that the input text file contains data in a format readable by Pandas, with appropriate delimiters.
- The script performs 16-bit conversion by scaling the data to fit within the range of 16-bit signed integers (-32768 to 32767).
- Adjust the delimiter parameter (`delimiter='\s+'`) in `read_text_file()` as needed to match the format of your input data.
- Be cautious of the input data range and scaling factors to avoid data loss during conversion.
