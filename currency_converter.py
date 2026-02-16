# EN: Real-time Currency Converter
# AZ: Real zamanlı Valyuta Çevirici

import requests

def convert_currency(amount, from_currency, to_currency):
    # EN: We use a free API for exchange rates
    # AZ: Valyuta məzənnələri üçün ödənişsiz API istifadə edirik
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if to_currency.upper() in data["rates"]:
            rate = data["rates"][to_currency.upper()]
            result = amount * rate
            print(f"\n{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
            print(f"Rate / Məzənnə: {rate}")
        else:
            print("Currency not found! / Valyuta tapılmadı!")
            
    except Exception as e:
        print(f"❌ Error / Xəta: {e}")

if __name__ == "__main__":
    print("--- Currency Converter / Valyuta Çevirici ---")
    amount = float(input("Amount / Məbləğ: "))
    from_curr = input("From (e.g. USD) / Hansı valyutadan: ")
    to_curr = input("To (e.g. AZN) / Hansı valyutaya: ")
    
    convert_currency(amount, from_curr, to_curr)
