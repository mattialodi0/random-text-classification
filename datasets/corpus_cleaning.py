import os
import random
import re

def clean_corpus(input_file, output_file):
    """
    Cleans a text corpus by removing non-alphanumeric characters,
    converting text to lowercase, and removing extra whitespace.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output cleaned text file.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Remove non-alphanumeric characters (except spaces)
            # cleaned_line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
            # Remove text between angle brackets and round brackets
            cleaned_line = re.sub(r'<[^>]*>', '', line)
            cleaned_line = re.sub(r'\([^)]*\)', '', cleaned_line)
            # Convert to lowercase
            cleaned_line = cleaned_line.lower()
            # Remove extra whitespace
            cleaned_line = ' '.join(cleaned_line.split())
            # Write cleaned line to output file
            outfile.write(cleaned_line + '\n')

# if __name__ == "__main__":
#     input_path = './corpus.txt'
#     output_path = './cleaned_corpus.txt'
#     clean_corpus(input_path, output_path)
