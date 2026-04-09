import os
import random
from sympy import isprime, mod_inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# To-Dos
# finish aes, xor, ceasar encryption functions

##### Helper functions

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

def rsa_encrypt(message):

    # generate keys
    pub, priv = generate_keys()

    # unpack the public key
    e, n = pub

    message_bytes = message.encode('utf-8')
    cipher = [pow(byte, e, n) for byte in message_bytes]
    print("Encrypted: ", cipher)
    # return cipher

    # key = RSA.generate(bits=2048)
    # private_key = key.export_key()
    # public_key = key.public_key().export_key()

    # cipher = PKCS1_OAEP.new(public_key)

    # encrypted_message = cipher.encrypt(message)

    # # jot down private key
    # with open("private_k.pem", 'wb') as file:
    #     file.write(private_key)

    # # jot down public key
    # with open("public_k.pem", 'wb') as file:
    #     file.write(public_key)

    # print("don't forget your keys, located in the same folder")

    # return encrypted_message

def aes_encrypt(key: bytes, plaintext: bytes) -> dict:
    # 16 bytes -> aes-128
    # 24 bytes -> aes-a92
    # 32 bytes -> aes-256 

    """
    Encrypt plaintext using AES-GCM
    
    args: 
    - key (bytes): 32-byte key (AES-256)
    - plaintext (bytes): data to encrypt
    
    Returns: dict containing nonce and ciphertext
    """
    if len(key) != 32: # require strongest key
        raise ValueError("Key must be 32 bytes for AES-256")
    
    # generate random 12-byte nonce (number used once) (recommended for GCM)
    nonce = os.urandom(12)

    aesgcm = AESGCM(key)

    # encrypt (no associated data for now)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    return {
        "nonce": nonce,
        "ciphertext": ciphertext
    }

def xor_encrypt():
    pass

def caesar_encrypt():
    pass

# deprecated moved to main.py
# # select right encryption function based on user input
def encryption_selector():

    encrypted = ""

    choice = input("👋 What ciphertext do you want to encrypt? [rsa, aes, caesar, xor] ")
    if choice == "rsa": 
        message = input("Provide message: ") 
        encrypted = rsa_encrypt(message)
    
    elif choice == "aes":
        ciphertext, key, iv = input("provide aes options: ciphertext key iv ").split()
        encrypted = aes_encrypt(ciphertext, key, iv)

    elif choice == "xor":
        data, key = input("provide xor options: data key ").split()
        encrypted = xor_encrypt(data, key)

    elif choice == "caesar":
        text, shift = input("provide caesar options, text shift: ").split()
        encrypted = caesar_encrypt(text, int(shift))

    
    answer = input("Would you like to encrypt again? ")
    start_program() if answer == "y" else print("bye")

    
def start_program():
    encryption_selector()
