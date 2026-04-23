import tkinter as tk
from util.decrypter_util import decrypt_rsa, aes_decryption, xor_decrypt, caesar_decrypt
from util.encrypter_util import rsa_encrypt, aes_encrypt, xor_encrypt, caesar_encrypt

"""
implement UI feature
"""

REGISTRY_ALGORITHMS = {
    "AES": {
        "encrypt": aes_encrypt,
        "decrypt": aes_decryption
    },
    "RSA": {
        "encrypt": rsa_encrypt,
        "decrypt": decrypt_rsa
    },
    "XOR": {
        "encrypt": xor_encrypt,
        "decrypt": xor_decrypt
    },
    "CAESAR": {
        "encrypt": caesar_encrypt,
        "decrypt": caesar_decrypt
    }
}

# deprecated using registry

# ENCRYPT_MAP = {
#     "AES": aes_encrypt,
#     "RSA": rsa_encrypt,
#     "XOR": xor_encrypt,
#     "CAESAR": caesar_encrypt
# }

# DECRYPT_MAP = {
#     "AES": aes_decryption,
#     "RSA": decrypt_rsa,
#     "XOR": xor_decrypt,
#     "CAESAR": caesar_decrypt
# }

# # extract encryption algos from keys
# E_ALGORITHMS = list(ENCRYPT_MAP.keys())



# # extract decryption algos from keys
# D_ALGORITHMS = list(DECRYPT_MAP.keys())

ALGORITHMS = list(REGISTRY_ALGORITHMS.keys())

def encrypt():
    text = input_box.get("1.0", tk.END).strip()
    algo = algo_var.get()

    # result = ENCRYPT_MAP[algo](text)
    result = REGISTRY_ALGORITHMS[algo]["encrypt"](text)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def decrypt():
    text = input_box.get("1.0", tk.END).strip()
    algo = algo_var.get()

    # result = DECRYPT_MAP[algo](text)
    result = REGISTRY_ALGORITHMS[algo]["decrypt"](text)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

# UI
root = tk.Tk()
root.title("Crypto Tool")

# Input
tk.Label(root, text="Input").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()

# Select algo, defaults to aes
algo_var = tk.StringVar(value="AES")

tk.Label(root, text="Algorithm").pack()
# controls options user can choose 
tk.OptionMenu(root, algo_var, *ALGORITHMS).pack()

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Encrypt", command=encrypt).pack(side="left", padx=5)
tk.Button(frame, text="Decrypt", command=decrypt).pack(side="left", padx=5)

# Output
tk.Label(root, text="Output").pack()
output_box = tk.Text(root, height=5, width=50)
output_box.pack()

root.mainloop()