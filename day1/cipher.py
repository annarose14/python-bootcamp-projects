alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODD-1: Create a function called 'encrypt' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # Non-alphabetic characters remain the same
    print(f"Here is the encoded result: {cipher_text}")



# def decrypt(original_text, shift_amount):
#   output_text = ""
#     for letter in original_text:
#         if letter in alphabet:
#             shifted_position = alphabet.index(letter) - shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#         else:
#             cipher_text += letter  # Non-alphabetic characters remain the same
#     print(f"Here is the encoded result: {output_text}")

    # Encrypt or decrypt based on the direction
if direction == 'encode':
    encrypt(original_text=text, shift_amount=shift)
elif direction == 'decode':
    encrypt(original_text=text, shift_amount=-shift)
else:
    print("Invalid direction!")


#####

