import sys
import subprocess
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad


def xor(a, b, c):
    result = a ^ b ^ c
    return result


def call_oracle(ciphertext, iv):
    result = subprocess.run(
        ['python', 'oracle.py', ciphertext.hex(), iv.hex()],
        capture_output=True, text=True
    )

    return int(result.stdout.strip())


def decrypt_block(ciphertext, iv, block, discovered_plaintext):
    if block == 0:
        c = iv + ciphertext[:8]
    else:
        c = iv + ciphertext[8 * block:8 * (block + 1)]
    c = bytearray(c)

    for pos in range(7, -1, -1):
        found_char = 0
        for i in range(256):
            c[pos] = i
            oracle_result = call_oracle(c, iv)
            if oracle_result == 1:
                if block == 0:
                    found_char = xor(i, iv[pos], 8 - pos)
                else:
                    found_char = xor(i, ciphertext[8 * (block - 1) + pos], 8 - pos)
                break
        discovered_plaintext[pos] = found_char
        for j in range(pos, 8):
            if block == 0:
                x_j = xor(8 - pos + 1, discovered_plaintext[j], iv[j])
            else:
                x_j = xor(8 - pos + 1, discovered_plaintext[j], ciphertext[8 * (block - 1) + j])
            c[j] = x_j

    return discovered_plaintext


def main():
    if len(sys.argv) != 3:
        print("Args should be: python ex1.py <ciphertext> <iv>")
        sys.exit(1)

    ciphertext = bytes.fromhex(sys.argv[1])
    iv = bytes.fromhex(sys.argv[2])

    plaintext = bytearray()
    num_blocks = len(ciphertext) // 8

    for block in range(num_blocks - 1, -1, -1):
        discovered_plaintext = bytearray(b'\x00' * 8)
        discovered_plaintext = decrypt_block(ciphertext, iv, block, discovered_plaintext)
        # print("Block number", block + 1, "plaintext discovered:", discovered_plaintext)
        plaintext = discovered_plaintext + plaintext

    padded_data1 = unpad(plaintext, 8)
    print(padded_data1.decode())


if __name__ == "__main__":
    main()
