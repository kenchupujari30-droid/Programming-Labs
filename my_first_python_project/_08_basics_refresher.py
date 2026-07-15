"""
_0_basics_refresher.py

A quick brush-up, nothing new. Variables, types, f-strings, control
flow -- exactly what Class 1 covered. No mention of AI or agents
anywhere in this file, and none in the next four files either. These
are just Python skills, worth knowing on their own merit.

Run with: uv run _0_basics_refresher.py
"""
# --- Variables and data types ---
city = "Tokiyo"            #str
temperature = 40.1         #float
is_rainnig = False         #bool
print(type(city),type(temperature),type(is_rainnig))

# --- f-strings ---

print(f"{city} is currently {temperature}°C")
print(f"That's {temperature * 9 / 5 + 32:.1f}°F.")

#----------------control flow-----------
if temperature > 30:
  print("pack light clothes ")
elif temperature > 15:
  print("A light jacket shuold be enough")
else:
  print("pack a warm coat")

# --- Comparison and boolean operators, quickly ---
print(5 == 5,5 !=3, 10 > 20)
has_ticket = True
has_id = True
if has_ticket and has_id:
  print("Ready to board")

#if __name__ == " __main__":
  print("\nRefresher done..Nothing above is new ---moving strain into data structure")
