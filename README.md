# DISCLAIMER
This program is for **EDUCATIONAL PURPOSES ONLY**. I will not be held responsible for any damages or loss of data that may occur from the improper or malicious use of this software.

This tool performs irreversible encryption using a symmetric key. If you lose or forget your encryption key, all encrypted data will be permanently inaccessible and unrecoverable.

# File Encryptor

This is a simple program I made in Python that allows you to encrypt or decrypt your files using AES-128 symmetrical encryption. This is one of the most secure types of encryption and it can be specially useful is some scenarios, like ensuring no one can see your documents on a shared device, etc... For reference, a bruteforce attack using the most powerful computer ever created would still take over 2 trillion years to decrypt a file secured with AES-128 encryption.

# Encryption Key

In order for this program to work you will need to give it a 32 bit key, which must be exactly 32 characters long. This same key will be used to both encrypt and decrypt your files. **IMPORTANT:** Make sure to store your key in a safe place. If it gets lost all the encrypted files will be permanently inaccessible and there is no way to recover them.

This website will automatically generate for you a valid 32 bit key: https://www.random.org/passwords/?num=1&len=32&format=html&rnd=new

# How to use

Using this program is very straightforward. Do the following steps:

1. Download Python 3.6 or higher (I suggest always using the latest version)
2. Download the program
3. Open this program with your code editor and write your 32 bit key in the variable RAW_KEY
4. Save the changes and run the program
