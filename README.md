# RSA Public Key Cryptosystem
This documentation is for the RSA encryption in Dr. Sarah Mocas' cryptography class (grad level). 

This program was authored by Robert Pelayo (rpelayo@pdx.edu)

# Running the program:
To run the program, python3 must be installed.
### Enter:
```bash
python3 rsa.py
```

Select 1 for key generation, 2 for encryption of the file ptext.txt, or 3 for decyption of the file ctext.txt.


# Files included:
- rsa.py
    - Source code for the project. This is what is being run.
- prikey.txt
    - The private key for encryption/decryption file. Format is {P G E}.
- pubkey.txt
    - The public key for encryption/decryption. Format is {P G E}.
- ctext.txt
    - Cipher text generated from the program.
- dtext.txt
    - Decrypted output from the ciphertext.
- ptext.txt
    - The plaintext to be decypted.