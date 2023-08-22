import random

# settings
dir = "/Users/japyliwanag/Local Files/Files Unsorted/Code/REFERENCES/"
filename = "10k.txt"
num_guess = 6

# init vars
guesses = {}
word = ""

# generate dict of guesses
for i in range(num_guess):
    guesses[str(i)] = ["_", "_", "_", "_", "_"]

# Read the words from the file and create a list
file_path = dir + filename
with open(file_path) as f:
    words = f.read().splitlines()

# Filter words with 5 characters and store in a new list
five_lett_words = [word for word in words if len(word) == 5]

# get random word
word = five_lett_words[random.randint(0, len(five_lett_words) - 1)]

# print
for key in guesses:
    guess_word = ""
    for char_key in range (0, len(guesses[key])):
        guess_word += guesses[key][char_key] + " "

    print(f"{guess_word}")

# # print random word
# for x in range(10):
#     print(five_letter_words[random.randint(0, len(five_letter_words)-1 )])