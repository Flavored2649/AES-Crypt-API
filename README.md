# AES Crypt API Documentation

This documentation describes the AES Crypt API and how to interact with it using HTTP requests. The API provides two main endpoints, one for encrypting a message and another for decrypting it.

## Endpoints

### Encryption

To encrypt a message, send a GET request to the `/api/encrypt` endpoint. You need to provide two query parameters:

- `message`: The plaintext message you want to encrypt.
- `key`: The 64-character, hex-encoded encryption key.

An example Python script for encryption can be found here: [Encryption Example](encrypt.py)

### Decryption

To decrypt a message, send a POST request to the `/api/decrypt` endpoint. You need to provide two query parameters:

- `message`: The encrypted message you want to decrypt.
- `key`: The 64-character, hex-encoded encryption key.

An example Python script for decryption can be found here: [Decryption Example](decryption.py)
