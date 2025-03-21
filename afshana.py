# task.py

# Ask the user for their name and age
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate the year the user will turn 100
import datetime
current_year = datetime.datetime.now().year
year_turn_100 = current_year + (100 - age)

# Print the result
print(f"Hello {name}, you will turn 100 years old in the year {year_turn_100}.")
