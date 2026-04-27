import os
import random
import base64
from sympy import isprime, mod_inverse
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP, AES
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# To-Dos
# finish aes, xor, ceasar encryption functions

##### Helper functions

#--- xor encryption helper---#

# works on bytes not strings
# data: the input (plaintext or ciphertext) as bytes (the encrypt and decrypt xor functions use this)
# key: the encryption key, also bytes
# returns new bytes after XOR operation
def xor_bytes(data: bytes, key: bytes) -> bytes:

    """
    # enumerate loops over each byte in data, gives 
    #   i -> index(0, 1, 2, ...)
    #   b -> the actual byte value

    Example:
    data = b"ABC"
    enumerate -> (0, 65), (1, 66), (2, 67)  

    key[i % len(key)] <-- repeat the key if it's shorter than the data

    Example:
    key = b"XY   # length = 2

    i=0 -> key[0 % 2] = key[0]
    i=1 -> key[1 % 2] = key[1]

    b ^ key[...] <- XORs the current data byte with corresponding key byte
    bytes() wraps around logic to covert list of XORed byte values into a bytes object
    """
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

#---- function to generate a random prime ----#
# for better security primes should be 1024 - 4096
def generate_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if isprime(p):
            return p

#---- function RSA key generation ----#
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p: # ensure p != q
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537 # common choice
    if phi % e == 0:
        # fallback if e divides phi(n)
        e = 3
        while phi % e == 0:
            e += 2
    
    # Compute d
    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    print("Public Key: ", public_key)
    print("Private Key: ", private_key)

    return public_key, private_key

# asymmetric
def rsa_encrypt(message):

    # generate keys
    pub, priv = generate_keys()

    # unpack the public key
    e, n = pub

    message_bytes = message.encode('utf-8')
    cipher = [pow(byte, e, n) for byte in message_bytes]
    print("Encrypted: ", cipher)

    return cipher
    
# symmetric
def aes_encrypt(plaintext: str) -> dict:
    # 16 bytes -> aes-128
    # 24 bytes -> aes-192
    # 32 bytes -> aes-256 

    """
    Encrypt plaintext using AES-GCM
    
    args: 
    - key (bytes): 32-byte key (AES-256) <-- generated in the function
    - plaintext (bytes): Secret message
    
    Returns: dict containing nonce and ciphertext
    """

    # generate secure key
    key = get_random_bytes(32) # AES-256

    print(f"Orginal: {plaintext}")
    print("\n")


    message_bytes = plaintext.encode("utf-8") # need to convert plaintext to bytes

    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message_bytes)


    res_dict = {
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "key": base64.b64encode(key).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "tag": base64.b64encode(tag).decode()
    }

    for key, value in res_dict.items():
        print(f"{key}, Value: {value}")

    return res_dict

# symmetric
"""
usage example

text = "Hello, World!"
key = "secret"
"""
def xor_encrypt(text: str, key: str) -> str:
    
    # converts text, key to bytes passes it to xor_bytes helper
    encrypted = xor_bytes(text.encode(), key.encode())
    print(base64.b64encode(encrypted).decode())

    return base64.b64encode(encrypted).decode()


"""
usage example

message = "Hello, World!"
shift = 3

caesar_encrypt(message, 3)
"""
def caesar_encrypt(text, shift):
    result = ""
    # loop through the characters in text
    for c in text:
        
        # check if character is a letter, only shifting letters
        if c.isalpha():
            # determine if uppercase or lowercase ord() converts letters to ascii, chr() converts back to char
            base = ord('A') if c.isupper() else ord('a')

            # Shift character and wrap around alphabet
            shifted = (ord(c) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # this else is for non alphabet characters
            result += c

    print(result)
    return result

# deprecated moved to main.py
# # select right encryption function based on user input
# def encryption_selector():

#     encrypted = ""

#     choice = input("👋 What ciphertext do you want to encrypt? [rsa, aes, caesar, xor] ")
#     if choice == "rsa": 
#         message = input("Provide message: ") 
#         encrypted = rsa_encrypt(message)
    
#     elif choice == "aes":
#         ciphertext, key, iv = input("provide aes options: ciphertext key iv ").split()
#         encrypted = aes_encrypt(ciphertext, key, iv)

#     elif choice == "xor":
#         data, key = input("provide xor options: data key ").split()
#         encrypted = xor_encrypt(data, key)

#     elif choice == "caesar":
#         text, shift = input("provide caesar options, text shift: ").split()
#         encrypted = caesar_encrypt(text, int(shift))

    
#     answer = input("Would you like to encrypt again? ")
#     start_program() if answer == "y" else print("bye")

    
# def start_program():
#     encryption_selector()
