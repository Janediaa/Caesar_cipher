def encrypt(message, shift_key):
    str1 = ""
    for char in message.lower():
        if char.isalpha():
            new_char = ord(char) + shift_key
            if new_char > ord('z'):
                new_char -= 26
                str1 += chr(new_char)
            else:
                str1 += chr(new_char)
        else :
            str1 += char
    return str1

def decrypt(message, shift):
    str2 = ""
    for char in message.lower():
        if char.isalpha():
            new_code = ord(char) - shift
            if new_code < ord('a'):
                new_code += 26
                str2 += chr(new_code)
            else :
                str2 += chr(new_code)
        else :
            str2 += char
    return str2

val = int(input("Enter value : "))

if val == 1:
    message = input("Plain text : ")
    shift = int(input("Shift_key : "))
    encrypted_msg = encrypt(message, shift)

    print("Cipher text : ", encrypted_msg)

elif val == 2:
    message = input("cipher text : ")
    shift = int(input("Shift_key : "))
    decrypted = decrypt(message, shift)

    print("plain text : ", decrypted)

else :
    print("Invalid choice")
    print("Exiting")