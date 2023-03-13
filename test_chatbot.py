import chardet
import os
import random

def get_random_sentence():
    # Open the PDF file and read the first 10 pages
    with open(os.path.join(os.path.dirname(__file__), 'sebenta.pdf'), 'rb') as pdf_file:
        # Read the PDF file as a byte string
        pdf_data = pdf_file.read(10 * 1024 * 1024) # Read up to 10MB of data

        # Determine the encoding of the byte string using chardet
        result = chardet.detect(pdf_data)
        encoding = result['encoding']

        # Decode the byte string using the detected encoding
        pdf_text = pdf_data.decode(encoding)

        # Split the text into sentences
        sentences = pdf_text.split('.')

        # Select a random sentence from the list of sentences and return it
        return random.choice(sentences)
