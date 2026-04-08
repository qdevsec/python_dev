from util.decrypter_util import *
from util.encrypter_util import *


def selector(answer):

    # Encryption
    if answer == "encrypt":
        response = str.lower(input("cool we're encrypting today, here are the options \n" \
                                "[rsa, aes, xor, caesar] "))
        
        if response == 'rsa':
            rsa_encrypt()

        if response == 'aes':
            aes_encrypt()

        if response == 'rsa':
            xor_encrypt()

        if response == 'caesar':
            caesar_encrypt()

    # Decryption
    if answer == "decrypt":
        response = str.lower(input("cool we're decrypting today, here are the options \n" \
                                "[rsa, aes, xor, caesar] "))
        
        if response == 'rsa':
            rsa_decrypt()

        if response == 'aes':
            aes_decryption()

        if response == 'rsa':
            xor_decrypt()

        if response == 'caesar':
            caesar_decrypt()

def start():
    answer = str.lower(input("Hello, 🔓 decrypt or encrypt 🔐 ? "))
