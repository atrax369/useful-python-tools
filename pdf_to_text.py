# EN: PDF Text Extractor Script
# AZ: PDF-dən Mətni Çıxaran Skript

import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        # EN: Open the PDF file / AZ: PDF faylını açır
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            print(f"\nPages / Səhifə sayı: {len(reader.pages)}")
            print("-" * 30)

            # EN: Extract text from each page
            # AZ: Hər səhifədən mətni çıxarır
            full_text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                full_text += page.extract_text()

            # EN: Save to a text file / AZ: Mətn faylına yadda saxlayır
            with open("output_text.txt", "w", encoding="utf-8") as text_file:
                text_file.write(full_text)
            
            print("✅ Success! Text extracted to 'output_text.txt'")
            print("✅ Uğurlu! Mətn 'output_text.txt' faylına köçürüldü.")

    except Exception as e:
        print(f"❌ Error / Xəta: {e}")

if __name__ == "__main__":
    path = input("Enter PDF file path / PDF faylının yolunu daxil edin: ")
    extract_text_from_pdf(path)
