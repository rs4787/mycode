#!/usr/bin/env python3

message = 'Discogs recommends '

# This word bank is for conditions underwhich we keep / add to our collection
keepers = ["5", "4", "mint", "good", "great", "almost mint"]

toEbay = ["3", "acceptable", "slightly scratched"]

# wrap connection in a int() to accept decimals as numbers
connection = input("What is the condition of your vinyl?").lower()

# if input value was equal to Mint
#if connection == "5":      # == is asking "is this equal to?"
#if connection == "5" or connection == "4" or connection == "mint":
#elif connection == "4":
#    message = message + 'Keeping vinyl.'
#elif connection == "3":


if connection in keepers:
    message = message + 'Keeping vinyl.'   # = is "assignment"
elif connection in toEbay:
    message = message + 'Getting rid of vinyl.'
else:
    message = message + 'Throwing away vinyl.'
print(message)
