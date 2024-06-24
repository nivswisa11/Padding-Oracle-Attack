# Padding Oracle Attack with DES

This repository contains a Python implementation of a padding oracle attack on a block cipher using the DES encryption algorithm. The attack aims to decrypt a given ciphertext by exploiting a vulnerability in the padding scheme used.

This project was developed as part of the course "Communication Security" (אבטחת תקשורת).

## Prerequisites

To run the code, you need to have the following:

- Python 3.x
- `pycryptodome` library (install with `pip install pycryptodome`)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/guyreuveni33/Padding-Oracle-Attack.git
   ```

2. Navigate to the project directory:

   ```sh
   cd Padding-Oracle-Attack
   ```

## Usage

### Oracle

The `oracle.py` script acts as the padding oracle. It attempts to decrypt the ciphertext using the provided key and IV, and checks if the padding is correct. It returns `1` if the padding is correct, and `0` otherwise.

1. Create a file named `key.txt` containing the DES key in binary format.
2. Run the oracle script:

   ```sh
   python oracle.py <ciphertext> <iv>
   ```

   Replace `<ciphertext>` and `<iv>` with the appropriate values in hexadecimal format.

### Attack Script

The `attack.py` script performs the padding oracle attack to decrypt the given ciphertext.

1. Run the attack script:

   ```sh
   python attack.py <ciphertext> <iv>
   ```

   Replace `<ciphertext>` and `<iv>` with the appropriate values in hexadecimal format. The decrypted plaintext will be displayed in the console output.

### Example

1. Generate the ciphertext and IV using DES encryption.
2. Store the key in `key.txt`.
3. Run the oracle script to check the padding:

   ```sh
   python oracle.py <ciphertext> <iv>
   ```

4. Run the attack script to decrypt the ciphertext:

   ```sh
   python attack.py <ciphertext> <iv>
   ```

### Running Example

Here's an example using the provided ciphertext and key:

1. Create a `key.txt` file containing the key `poaisfun` in binary format.
2. Use the following commands in the terminal:

   ```sh
   python attack.py 33aaa3017e45337bd36342b3920be656 0000000000000000
   ```

   The expected output will be:

   ```
   Hello World
   ```

## Explanation

The padding oracle attack exploits a vulnerability in the padding scheme used in the DES block cipher. The attack works by iteratively modifying the ciphertext and utilizing the padding oracle function to retrieve the decrypted blocks.

The code consists of the following components:

- **oracle**: This function acts as the padding oracle. It attempts to decrypt the ciphertext using the provided key and IV, and checks if the padding is correct. It returns `1` if the padding is correct, and `0` otherwise.

- **decrypt_block**: This function performs the attack on a single block. It iteratively modifies the ciphertext and exploits the padding oracle to retrieve the decrypted block.

- **main**: The main function reads the command-line arguments (`<ciphertext>` and `<iv>`) and calls the `decrypt_block` function for each block in the ciphertext. The decrypted blocks are concatenated and displayed as the resulting plaintext.

## License

This project is licensed under the MIT License.

Feel free to explore, modify, and use the code according to the terms of the license.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For questions or feedback, please contact.

Made by Niv Swisa and Guy Reuveni.
