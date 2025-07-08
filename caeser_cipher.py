alphabet =[chr(i) for i in range(ord('a'),ord('z')+1)]
print(alphabet)


def caesar(original_text,shift_amount,encode_or_decode):
    cipher_text =""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letters in original_text:
        if letters not in alphabet:
            cipher_text += letters
        shift_position = alphabet.index(letters)+ shift_amount
        shift_position %= len(alphabet)
        cipher_text += alphabet[shift_position]
    print(f"Here is the {encode_or_decode} word : {cipher_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text = input("Type the message \n")
    shift = int(input("Type shift number\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart = input("Type 'yes' to continue.Otherwise 'no'").lower()
    if restart == 'no':
        should_continue = False
        print("Bye")