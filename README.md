# RSA Public Key Cryptosystem
This documentation is for the PSU-CRYPT Feistel cipher in Dr. Sarah Mocas' cryptography class (grad level). 

This program was authored by Robert Pelayo (rpelayo@pdx.edu)

# Running the program:
To run the program, python3 must be installed.
### Encrypt the file plaintext.txt:
```bash
python3 psu-crypt encrypt
```
This will encrypt the text inside the `plaintext.txt` file into the file `cyphertext.txt`

### Decrypt the file cyphertext.txt:
```bash
python3 psu-crypt decrypt
```
This will decrypt the text inside the file `cyphertext.txt` and write it into the file `plaintext.txt`

# Files included:
- psu-crypt.py
    - Source code for the project. This is what is being run.
- key.txt
    - Write the secret key inside this file. The program only reads from this file. Key must begin with 0x and be a 80-bit key.
- plaintext.txt
    - This is where the program will write/read from for the the plaintext to encrypt/decrypt.
- cyphertext.txt
    - Read/writes the cipher text from the plaintext.