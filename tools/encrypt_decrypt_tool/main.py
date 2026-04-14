import ast
from util.decrypter_util import *
from util.encrypter_util import *


def selector(answer):

    # Encryption
    if answer == "encrypt":
        response = str.lower(input("cool we're encrypting today, here are the options \n" \
                                "[rsa, aes, xor, caesar] "))
        
        if response == 'rsa':
            message = input("Please provide the message you want to encrypt: ")
            rsa_encrypt(message)
            retry()

        if response == 'aes':
            message = input("Please provide the message you want to encrypt: ")
            # format_message = 'b' + message + "'"
            aes_encrypt(message)
            retry()

        if response == 'xor':
            message = input("Please provide the message you want to encrypt: ")
            key = input("Please provide the key: ")
            xor_encrypt(message, key)
            retry()

        if response == 'caesar':
            text = input("Please provide the message you want to encrypt: ")
            shift = input("Please provide the shift right number: ")
            caesar_encrypt(text, int(shift))
            retry()

    # Decryption
    if answer == "decrypt":
        response = str.lower(input("cool we're decrypting today, here are the options: \n" \
                                "[rsa, aes, xor, caesar] "))
        
        if response == 'rsa':
            cipher = ast.literal_eval(input("please provide the cipher [list]: "))
            private_key = ast.literal_eval(input("please provide the cipher [tuple]: "))
            decrypt_rsa(cipher, private_key)
            retry()

        if response == 'aes':
            ciphertext = input("Ciphertext: ")
            key = input("key: ")
            nonce = input("nonce: ")
            tag = input("tag: ")
            aes_decryption(ciphertext, key, nonce, tag)
            retry()

        if response == 'xor':
            message = input("Please provide the message you want to decrypt: ")
            key = input("Please provide the key: ")
            xor_decrypt(message, key)
            retry()

        if response == 'caesar':
            text = input("Please provide the message you want to decrypt: ")
            shift = input("Please provide the shift left number: ")
            caesar_decrypt(text, int(shift))
            retry()

def retry():
    res = input("would you like to restart? [y / n] ")
    
    if res == 'y':
        start()
    elif res == 'n':
        print("Until next time 👋 ")
    else:
        print("Until next time 👋 ")


def start():
    answer = str.lower(input("Hello, 🔓 decrypt or encrypt 🔐 ? "))
    selector(answer)


## Begin
start()