# Instantiate a variable named favorite_foods which is a dictionary 
# where names (strings) are keys and names of food (strings) are values. 
# Instantiate the dictionary with the following pairs: 
# “Jess”: “dried mangoes” and “Ian”: “chocolate almonds”
favorite_foods = {
    "Jess": "dried mangoes",
    "Ian": "chocolate almonds",
    "Ruk": "oreos"
}

# Write the code to read the value for “Jess” 
print(favorite_foods["Jess"])

# Write the code to update the value of “Ian” to “breakfast tacos”
favorite_foods["Ian"]="breakfast tacos"
print(favorite_foods)

# Write the code to add another entry to the dictionary, 
# where the key is “Jane” and the value is “sweet potatoes” 
favorite_foods["Jane"]="sweet potatoes"
print(favorite_foods)

# Write the code to delete the”Ian” key (there are two ways to do this)
del favorite_foods["Ian"]
print(favorite_foods)

# Write the code needed to loop through favorite_foods and print each key and value 
for food in favorite_foods:
    print(food + ": " + favorite_foods[food])

# Someone saw you entering people's favorite foods manually and it hurt their soul. 
# They sent you a file of everyone’s favorite foods called “fave_foods.txt”. 
# Store that file to a variable named “fave_foods” and open it for reading. 
favorite_foods = open("favorite_foods.txt", "r")

# Create a variable called “lines” which stores a list of strings which are the lines of the file. 
# Write the code needed to extract the lines from the file.
lines = favorite_foods.readlines()