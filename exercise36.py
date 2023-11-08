# Read a letter from the user
letter = input("Enter a letter of the alphabet: ")

# Convert the letter to lowercase for case insensitivity
letter = letter.lower()

# Check if the input is a single letter
if len(letter) == 1 and letter.isalpha():
    if letter in "aeiou":
        print(f"The letter {letter} is a vowel.")
    elif letter == "y":
        print("Sometimes 'y' is a vowel, and sometimes 'y' is a consonant.")
    else:
        print(f"The letter {letter} is a consonant.")
else:
    print("Please enter a single letter of the alphabet.")
