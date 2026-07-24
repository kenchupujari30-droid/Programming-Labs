"""
_011_error_handling.py

try/except -- catching a problem on purpose instead of letting it crash
your entire program. Still no AI, no agents.

Run with: uv run _011_error_handling.py
"""

# --- Without error handling, ANY unexpected problem stops everything. ---
# (Read, don't run, this comment: result = 10 / 0 would crash the whole
# program with a ZeroDivisionError.)

# --- try/except: catch it, decide what happens instead ---
try:
     
     result = 10 / 0  #10 / 2
except ZeroDivisionError:
     print("Cant divide by zero ----using 0 instead")
     result = 0
print(f"result is now: {result}")          

# --- A different failure, same shape ---

try:
     age = int("not a number") #10

except ValueError:
     print("That wasn't an valid number------using 0 instead.")
     age = 0
print(f"age is now: {age}")     

# --- Catching more than one possible problem ---
def safe_divide(a, b):
     try:
          return a / b
     except ZeroDivisionError:
          return 0
     except TabError:
          return 0
print(safe_divide(10, 2), safe_divide(10, 0), safe_divide(10, 3))  #safe_divide(10, "x")

# --- finally: runs no matter what happened ---
def read_setting(value):
     try:
          return int(value)
     except ValueError:
          print(f"{value!r} isn't a number, defaulting to 0.")
          return 0
     finally:
          print("Done attempting to read this settings.")

read_setting("42")
read_setting("oops")          

#--- Trying it back to File 1's data structures: a missing dict key ---

# weather_reading = {"city:" "Tokyo", "temperature_c: 22.5"}
# try:
#      print(weather_reading["city"])  # this key doesn't exist  #["humidity"]
# except KeyError:
#      print("No humidity data available---thats fine we will skip it")


weather_reading = {
    "city": "Tokyo",
    "temperature_c": 22.5,
    "humidity": 65
}
humidity = weather_reading.get("humidity")

if humidity is None:
    print("No humidity data available.")
else:
    print(humidity)


if __name__ == "__main__":
    print("\nError handling done. Every risky operation above was caught -- nothing crashed.")