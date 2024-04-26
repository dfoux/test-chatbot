import os
import random
import re
from PyPDF2 import PdfReader

def get_random_sentence(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text_list = []
        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text()
            text_list.append(page_text)
        pdf_text = ' '.join(text_list)
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|…|\?)\s', pdf_text)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        if sentences:
            return random.choice(sentences)
        else:
            return None

def main():
    pdf_path = input("Enter the location of the PDF file: ")
    if not os.path.exists(pdf_path):
        print("File not found.")
        return
    random_sentence = get_random_sentence(pdf_path)
    if random_sentence:
        print("Random sentence from the PDF:")
        print(random_sentence)
    else:
        print("No sentences found in the PDF.")

if __name__ == "__main__":
    main()
