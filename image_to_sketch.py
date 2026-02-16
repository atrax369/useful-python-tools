# EN: Convert any photo into a pencil sketch
# AZ: İstənilən şəkli qara qələm eskizinə çevirən skript

import cv2

def create_sketch(image_path, output_name):
    try:
        # EN: Load the image / AZ: Şəkli yükləyir
        img = cv2.imread(image_path)
        
        # EN: Convert to Gray Scale / AZ: Boz rəng tonuna çevirir
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # EN: Invert the image / AZ: Şəkli tərs çevirir (invert)
        inverted_image = 255 - gray_image
        
        # EN: Blur the image / AZ: Şəkli dumanlandırır (blur)
        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
        
        # EN: Final Sketch / AZ: Eskiz halına gətirir
        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        
        # EN: Save result / AZ: Nəticəni yadda saxlayır
        cv2.imwrite(f"{output_name}.png", pencil_sketch)
        print(f"✅ Sketch saved as / Eskiz yadda saxlanıldı: {output_name}.png")
        
    except Exception as e:
        print(f"❌ Error / Xəta: {e}")

if __name__ == "__main__":
    path = input("Enter image path / Şəkil yolunu daxil edin: ")
    out = input("Output file name / Çıxış faylının adı: ")
    create_sketch(path, out)
