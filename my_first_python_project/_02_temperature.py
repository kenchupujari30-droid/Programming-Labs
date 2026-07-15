city = "India"
temperature =22.5
is_raining = False
forecast = [22.5, 23.1, 21.8]

print(type(city), type(temperature),type(is_raining),type(forecast))

# F-STRINGS -- mixing variables into text
# An f-string is a string with `f` right before the opening quote.
# Anything inside { } gets swapped out for the variable's real value.

print(f" The temperature in {city} is {temperature} degrees.")
print(f"That is {temperature *9 / 5 + 32:.1f}°F.")

# -----------------------------------------------------------------------
# CONTROL FLOW -- the agent's decision-making, in miniature
# -----------------------------------------------------------------------

