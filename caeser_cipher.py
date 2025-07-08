# Generate a list of all lowercase letters a–z using ASCII values
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]


# Caesar cipher function: encrypts or decrypts text based on shift
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""  # This will hold the final encrypted/decrypted message

    # If decoding, reverse the shift to go backwards
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each letter in the input text
    for letters in original_text:
        # If the character is not a letter (e.g., space, punctuation), keep it unchanged
        if letters not in alphabet:
            cipher_text += letters
            continue  # Skip to the next character

        # Find the new position after applying the shift
        shift_position = alphabet.index(letters) + shift_amount

        # Use modulo to wrap around if we go past 'z'
        shift_position %= len(alphabet)

        # Add the shifted letter to the result
        cipher_text += alphabet[shift_position]

    # Show the final result to the user
    print(f"Here is the {encode_or_decode} word: {cipher_text}")


# Loop to keep the program running until user says 'no'
should_continue = True
while should_continue:
    # Ask the user whether to encode or decode
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()

    # Get the message from the user
    text = input("Type the message:\n").lower()

    # Get the shift amount from the user
    shift = int(input("Type shift number:\n"))

    # Call the Caesar function with the provided inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to go again
    restart = input("Type 'yes' to continue. Otherwise, type 'no':\n").lower()
    if restart == 'no':
        should_continue = False
        print("Bye")
