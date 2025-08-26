import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input("Enter the message: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text +=  key[index]

print(f"The encrypted message is : '{cipher_text}'")

#DECRYPT
dec = input("Do you want to decrypt the message?(Y/N) : ").upper()
if dec == "Y":
    original_message = ""
    for letter in cipher_text:
        index = key.index(letter)
        original_message += chars[index]
    print(f"The original message is: '{original_message}'")