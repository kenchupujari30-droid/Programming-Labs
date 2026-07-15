#Method 1
#-----------------
# import requests

# BASE = "https://api.frankfurter.app"

# from_currency ="USD"
# to_currency = "INR"
# amount = 100

# url =f"{BASE}/latest"

# params = {
#        "from":from_currency,
#        "to":to_currency,
#        "amount":amount

# }

# try:
#     response = requests.get(url, params=params,timeout=10)

#     response.raise_for_status()
#     data = response.json()
#     converted_amount = data["rates"][to_currency]
#     print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
# except requests.exceptions.RequestException as e:
#          print("Request failed:", e)


#Method 2
#-------------

exchange_rate = 86.5   # 1 USD = 86.5 INR (example rate)

dollars = float(input("Enter amount in USD: "))

rupees = dollars * exchange_rate

print(f"${dollars:.2f} = ₹{rupees:.2f}")