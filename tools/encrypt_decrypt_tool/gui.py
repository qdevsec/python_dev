import tkinter as tk
from util.decrypter_util import decrypt_rsa, aes_decryption, xor_decrypt, caesar_decrypt
from util.encrypter_util import rsa_encrypt, aes_encrypt, xor_encrypt, caesar_encrypt

"""
implement UI feature
"""

REGISTRY_ALGORITHMS = {
    "AES": {
        "encrypt": {
            "func": aes_encrypt,
            "params": ["plaintext"]
        },
        "decrypt": {
            "func": aes_decryption,
            "params": ["ciphertext", "key", "nonce", "tag"]
        }        
    },
    "RSA": {
        "encrypt": {
            "func": rsa_encrypt,
            "params": ["message"]
        },
        "decrypt": {
            "func": decrypt_rsa,
            "params": ["cipher", "private_key"]
        }     
    },
    "XOR": {
        "encrypt": {
            "func": xor_encrypt,
            "params": ["text", "key"]
        },
        "decrypt": {
            "func": xor_decrypt,
            "params": ["encoded_text", "key"]
        }  
    },
    "CAESAR": {
        "encrypt": {
            "func": caesar_encrypt,
            "params": ["text", "shift"]
        },
        "decrypt": {
            "func": caesar_decrypt,
            "params": ["text", "shift"]
        } 
    }
}


ALGORITHMS = list(REGISTRY_ALGORITHMS.keys())

# only using one button
# def encrypt():
#     text = input_box.get("1.0", tk.END).strip()
#     algo = algo_var.get()

#     # result = ENCRYPT_MAP[algo](text)
#     result = REGISTRY_ALGORITHMS[algo]["encrypt"]["func"](text)

#     output_box.delete("1.0", tk.END)
#     output_box.insert(tk.END, result)

# def decrypt():
#     text = input_box.get("1.0", tk.END).strip()
#     algo = algo_var.get()
#     func = REGISTRY_ALGORITHMS[algo]["decrypt"]["func"](text)

#     # get inputs
#     kwargs = {key: entry.get().strip() for key, entry in entries.items()}

#     try:
#         result = func(**kwargs)
#     except Exception as e:
#         result = f"Error: {e}"

    # result = DECRYPT_MAP[algo](text)
    # result = D_REGISTRY_ALGORITHMS[algo]["decrypt"](text)

    # output_box.delete("1.0", tk.END)
    # output_box.insert(tk.END, result)

def build_fields(*args):
    algo = algo_var.get()
    operation = operation_select.get()
    # clear stale widgets
    for widget in param_frame.winfo_children():
        widget.destroy()
    entries.clear()

    params = REGISTRY_ALGORITHMS[algo][operation]["params"]

    for param in params:
        label = tk.Label(param_frame, text=param.capitalize())
        label.pack()

        entry = tk.Entry(param_frame, width=40)
        entry.pack()

        entries[param] = entry

# for the submit button
def submit():
    algo = algo_var.get()
    operation = operation_select.get()

    config = REGISTRY_ALGORITHMS[algo][operation]
    func = config["func"]

    # print(f"Debug: algo: {algo} operation: {operation} config: {config} func: {func}")

    kwargs = {k: e.get().strip() for k, e in entries.items()}

    print(f"kwargs: {kwargs}")

    try:
        result = func(**kwargs)

        # check the returned data type so dictionaries can be parsed
        if isinstance(result, dict):
            result = "\n".join(f"{k}: {v}" for k, v in result.items())

    except Exception as e:
        print("Seems like an error exception...")
        result = f"Error: {e}"
    
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

# UI
root = tk.Tk()
root.title("Crypto Tool - GUI")

entries = {}


# Input
tk.Label(root, text="Input").pack()
input_box = tk.Text(root, height=5, width=70)
input_box.pack()

# Instruction text area
# height is lines, width is characters
ins_text_area = tk.Text(root, height=16, width=70, wrap="word")
ins_text_area.insert(1.0, "Usage: \n" \
                          "RSA encrypt: paste message to be encrypted in input box \n" \
                          "RSA decrypt: provide cipher [list], provide cipher [tuple] \n" \
                          "------ \n"\
                          "AES encrypt: paste message to be encrypted in input box \n" \
                          "AES decrypt: paste info separated by space example: ciphertext key nonce tag \n" \
                          "------ \n" \
                          "XOR encrypt: paste message and key: 'Hello, world' 'secret' \n" \
                          "XOR decrypt: paste info separated by space example: '<encrypted>' '<key>' \n" \
                          "------ \n" \
                          "caesar encrypt: paste message in the input box: '<message>' 'shift right #' \n" \
                          "caesar decrypt: provide message and shift left #")
ins_text_area.config(state="disabled") # read-only
ins_text_area.pack()

# Select algo, defaults to aes
algo_var = tk.StringVar(value="AES")
operation_select = tk.StringVar(value="encrypt")

# tk.Label(root, text="Algorithm").pack()
# controls options user can choose 
# tk.OptionMenu(root, algo_var, *ALGORITHMS).pack()

# Buttons
# frame = tk.Frame(root)
# frame.pack(pady=10)

# tk.Button(frame, text="Encrypt", command=encrypt).pack(side="left", padx=5)
# tk.Button(frame, text="Decrypt", command=decrypt).pack(side="left", padx=5)

# Frames
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

param_frame = tk.Frame(root)
param_frame.pack(pady=10)

# Output
tk.Label(root, text="Output").pack()
output_box = tk.Text(root, height=5, width=70)
output_box.pack()

# Dropdown
algo_menu = tk.OptionMenu(top_frame, algo_var, *REGISTRY_ALGORITHMS.keys())
algo_menu.pack()

# Radio buttons
mode_frame = tk.Frame(root)
mode_frame.pack()

tk.Radiobutton(mode_frame, text="Encrypt", variable=operation_select, value="encrypt").pack(side="left")
tk.Radiobutton(mode_frame, text="Decrypt", variable=operation_select, value="decrypt").pack(side="left")

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)



# trigger rebuild when selection changes
algo_var.trace_add("write", build_fields)
operation_select.trace_add("write", build_fields)

# initialize fields
build_fields()

root.mainloop()