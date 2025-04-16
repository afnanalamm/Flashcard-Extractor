import json
import os
import re

def clean_data(text):   # copilot
    # Clean the data by removing unnecessary characters and fixing syntax errors
    text = text.replace('\"', '').strip()
    if text and not text.endswith('.'):
        text = re.sub(r'(?<![\.\?!])$', '.', text)  # Add a full stop if missing
    return text

def extract_flashcards2(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    cleaned_pairs = []
    for knol in data.get('knols', []):
        values = knol.get('values', {})
        if 'Front' in values and 'Back' in values:
            front = clean_data(values['Front'])
            back = clean_data(values['Back'])
            cleaned_pairs.append((front, back))

    output_path = os.path.join(os.path.dirname(input_file), output_file)
    with open(output_path, 'w') as out:
        for front, back in cleaned_pairs:
            out.write(f"Front: {front}\nBack: {back}\n\n")

if __name__ == "__main__":
    input_file = r"geography_glossary.json"
    output_file = "NEWEST_Extracted_Flashcards.txt"
    extract_flashcards2(input_file, output_file)
