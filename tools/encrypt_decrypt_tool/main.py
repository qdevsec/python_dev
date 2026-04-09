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
            aes_encrypt()
            retry()

        if response == 'rsa':
            xor_encrypt()
            retry()

        if response == 'caesar':
            caesar_encrypt()
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
            aes_decryption()
            retry()

        if response == 'xor':
            xor_decrypt()
            retry()

        if response == 'caesar':
            caesar_decrypt()
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