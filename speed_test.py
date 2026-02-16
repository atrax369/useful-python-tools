# EN: Internet Speed Test Script
# AZ: İnternet Sürətini Ölçən Skript

import speedtest

def run_speed_test():
    try:
        # EN: Initialize the Speedtest object
        # AZ: Speedtest obyektini başladır
        st = speedtest.Speedtest()
        
        print("Finding best server... / Ən yaxşı server axtarılır...")
        st.get_best_server()
        
        print("Testing Download Speed... / Yükləmə sürəti yoxlanılır...")
        download_speed = st.download()
        
        print("Testing Upload Speed... / Göndərmə sürəti yoxlanılır...")
        upload_speed = st.upload()
        
        # EN: Convert from bits to Megabits
        # AZ: Bit-dən Meqabit-ə çevirir
        print("\n" + "="*30)
        print(f"🚀 Download: {download_speed / 10**6:.2f} Mbps")
        print(f"🚀 Upload: {upload_speed / 10**6:.2f} Mbps")
        print(f"📍 Ping: {st.results.ping} ms")
        print("="*30)
        
    except Exception as e:
        print(f"❌ Error / Xəta: {e}")

if __name__ == "__main__":
    run_speed_test()
