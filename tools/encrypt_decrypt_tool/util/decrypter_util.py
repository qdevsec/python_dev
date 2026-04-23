from util.encrypter_util import xor_bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
import base64


####
# results is usually in bytes
# plaintext_str = plaintext_bytes.decode("utf-8") or just .decode() defaults to utf-8
# options for decode
# asci, latin-1, utf-8, utf-16, utf-32, cp1252, mbcs


"""
decrypts AES-encrypted ciphertext using CBC mode and PKCS7 padding

ciphertext parameter: encrypted data as bytes
key parameter: byte options 16 = AES-128, 24 = AES-192, 32 = AES-256
iv parameter: Initialization vector (16 bytes for AES)

returns plaintext as bytes
"""

# Example values
# ciphertext = bytes.fromhex("8ea2b7ca516745bfeafc49904b496089")
# key = b"thisisasecretkey" # 16-byte key for AES-128
# iv = b"thisisaninitvect"  # 16-byte Initialization Vector

# Decrypt
# plaintext = decrypt_aes(ciphertext, key, iv)

# Convert bytes to string (if text)
# print("Decrypted:", plaintext.decode())

def aes_decryption(ciphertext: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes:
    
    # debug
    # print(f"{type(ciphertext)} {type(key)} {type(nonce)} {type(tag)}")
    
    d_ciphertext = base64.b64decode(ciphertext)
    d_key = base64.b64decode(key)
    d_nonce = base64.b64decode(nonce)
    d_tag = base64.b64decode(tag)

    # debug
    print(f"{type(d_ciphertext)} {type(d_key)} {type(d_nonce)} {type(d_tag)}")

    cipher = AES.new(d_key, AES.MODE_GCM, nonce=d_nonce)
    print(cipher.decrypt_and_verify(d_ciphertext, d_tag))

    return cipher.decrypt_and_verify(d_ciphertext, d_tag)

# deprecated
# def aes_decrypt(ciphertext, key, iv):
#     cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
#     decryptor = cipher.decryptor()

#     padded_data = decryptor.update(ciphertext) + decryptor.finalize()

#     unpadder = PKCS7(128).unpadder()
#     data = unpadder.update(padded_data) + unpadder.finalize()

    # return data

def xor_decrypt(encoded_text: str, key: str) -> str:
    encrypted = base64.b64decode(encoded_text.encode())
    decrypted = xor_bytes(encrypted, key.encode())
    print(decrypted.decode())

    return decrypted.decode()

#------------------ Example Usage -------------------
# you would load your private key from a .pem file
# example:
# with open("private_key.pem", "rb") as f:
#     private_key_data = f.read()

# encrypted_message = b'...' # Your RSA-encrypted bytes
# decrypted_message = rsa_decrypt(encrypted_message, private_key_data)
# print(decrypted_message.decode())


def decrypt_rsa(cipher: list, private_key: tuple):

    # debug
    # print(f"{type(cipher)}: {cipher}")
    # print(f"{type(private_key)}: {private_key}")
    d, n = private_key

    # pow(base, exp, mod) same as (base ** exp) % mod
    decrypted_bytes = [pow(byte, d, n) for byte in cipher]
    message = bytes(decrypted_bytes).decode('utf-8')
    print(message)
    return message

"""
## deprecated

decrypts rsa-encrypted ciphertext using a private key in PEM format
ciphertext parameter: encrypted message as bytes
private_key_pem parameter: the private key in PEM format as bytes
"""
def rsa_decrypt(ciphertext: bytes, private_key_pem: bytes, password = None) -> bytes:

    # get private key from PEM
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=password  # if key is encrypted use password, 
    )

    # decrypt the ciphertext
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext


## caesar cipher decryption (text-based)
# print(caesar_decrypt("Khoor", 3)) --> should result in Hello

def caesar_decrypt(text, shift):
    result = ""

    # print(f"Debug: {text} {shift}")

    for char in text:
        # acts as filter, caesar only shift letters, if you
        # try to shift space or num of ! math will not work
        # to make sure decryption logic is only on A-Z or a-z
        if char.isalpha():
            # first check if upper case or not
            start = ord('A') if char.isupper() else ord('a')

            # convert char to 0-25 index
            # subtract shift to go backward
            # Use % 26 to wrap around correctly
            # convert back to ascii
            # ord() converts char to unicode, chr() reverses this
            # Uppercase (A-Z): numbers 65 to 90
            # Lowercase (a-z): numbers 97 to 122

            new_char = chr((ord(char) - start - shift) % 26 + start)
            result += new_char
        
        # if not letter (eg space) code skips math and adds
        # original character to results as is (eg )
        else:
            # Leaves spaces and punctuation as they are
            result += char

    print(result)

    
    return result

# deprecated moved to main.py
# select right decryption function based on user input
# def decryption_selector():

#     decrypted = ""

#     choice = input("👋 What ciphertext do you want to decrypt? [rsa, aes, caesar, xor] ")
#     if choice == "rsa": 
#         ciphertext, pemkey, password = input("Provide rsa options? ciphertext pemkey password(optional, type None if no pass) ").split()
#         decrypted = rsa_decrypt(ciphertext, pemkey, password)
    
#     elif choice == "aes":
#         ciphertext, key, iv = input("provide aes options: ciphertext key iv ").split()
#         decrypted = aes_decrypt(ciphertext, key, iv)

#     elif choice == "xor":
#         data, key = input("provide xor options: data key ").split()
#         decrypted = xor_decrypt(data, key)

#     elif choice == "caesar":
#         text, shift = input("provide caesar options, text shift: ").split()
#         decrypted = caesar_decrypt(text, int(shift))

#     # caesar is the only non byte returned result, adding this
#     print(decrypted) if choice == "caesar" else print(f"here : {decrypted.decode()}")
    
#     answer = input("Would you like to decrypt again? ")
#     start_program() if answer == "y" else print("bye")

    
# def start_program():
#     decryption_selector()

