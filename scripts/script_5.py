"""
Instructions:

- Use the JSON function loads to convert fast_food_franchise_string to a Python object.
- Assign the resulting Python object to fast_food_franchise_2.
"""
# Make a list of fast food chains.
import json
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Import the JSON library.

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

fast_food_franchise_2 = json.loads(fast_food_franchise_string)
print(type(fast_food_franchise_2))
