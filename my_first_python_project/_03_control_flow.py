city = "India"
temperature =22.5
is_raining = False
forecast = [22.5, 23.1, 21.8]


if is_raining:
  print("Bring an Umbrella.")
else:
  print("No Umbrella Needed.")

  for day_temp in forecast:
    if day_temp > 23:
       print(f"{day_temp}°c - warm day")
    else:
      print(f"{day_temp}°c - mild day")

if __name__ == "__main__":
    print("\nEvery one of these types and decisions reappears, unchanged, inside the agent you build later.")