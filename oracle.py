from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import unpad


def oracle(ciphertext, key, iv):
    try:
        cipher = DES.new(key, DES.MODE_CBC, iv)
        decrypted_padded_data = cipher.decrypt(ciphertext)
        unpad(decrypted_padded_data, 8)
        print(1, end='')
    except (ValueError, KeyError):
        print(0, end='')


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Args should be: python oracle.py <ciphertext> <iv>")
        sys.exit(1)
    ciphertext = bytes.fromhex(sys.argv[1])
    iv = bytes.fromhex(sys.argv[2])

    with open('key.txt', 'rb') as f:
        key = f.read()
        f.close()

    oracle(ciphertext, key, iv)
