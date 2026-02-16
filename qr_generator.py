# EN: QR Code Generator Script
# AZ: QR Kod Yaradan Skript

import qrcode

def generate_qr(data, file_name):
    try:
        # EN: Configure QR Code settings
        # AZ: QR Kodun tənzimləmələrini quraşdırır
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # EN: Add data and create the image
        # AZ: Məlumatı əlavə edir və şəkli yaradır
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        # EN: Save the file / AZ: Faylı yadda saxlayır
        img.save(f"{file_name}.png")
        print(f"✅ Success! QR code saved as {file_name}.png")
        print(f"✅ Uğurlu! QR kod {file_name}.png olaraq yadda saxlanıldı.")
        
    except Exception as e:
        print(f"❌ Error / Xəta: {e}")

if __name__ == "__main__":
    text_to_convert = input("Enter URL or Text / Link və ya mətn daxil edin: ")
    name = input("Enter file name (without .png) / Fayl adını daxil edin: ")
    generate_qr(text_to_convert, name)
