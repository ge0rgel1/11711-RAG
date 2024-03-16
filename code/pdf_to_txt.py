import pdfplumber
import os

def convert_pdf_folder_to_txt(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            # Open and convert each PDF to text
            try:
                with pdfplumber.open(input_path) as pdf:
                    with open(output_path, 'w', encoding='utf-8') as output_file:
                        for page in pdf.pages:
                            text = page.extract_text()
                            if text:  # Ensure there's text on the page before writing
                                output_file.write(text)
                print(f"Successfully converted {filename} to text.")
            except Exception as e:
                print(f"Failed to convert {filename}. Error: {e}")

# Example usage
input_folder = './'  # Replace with your PDF folder path
output_folder = './'  # Replace with your desired output folder path
convert_pdf_folder_to_txt(input_folder, output_folder)
