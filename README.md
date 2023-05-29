# AES-Crypt API

This API allows you to encrypt and decrypt messages with AES encryption.

## Endpoints

There are two main endpoints:

1. `/api/encrypt`: This endpoint accepts a `GET` or `POST` request with the parameters `message` (the message you want to encrypt) and `key` (a 32 bytes, hex encoded key). The endpoint returns an encrypted version of your message.

2. `/api/decrypt`: This endpoint accepts a `POST` request with the parameters `message` (the encrypted message you want to decrypt) and `key` (the key that was used for encryption). The endpoint returns a decrypted version of your message.

## Usage

### Encryption

To encrypt a message, send a `GET` or `POST` request to the `/api/encrypt` endpoint with your message and key as parameters.

### Decryption

To decrypt a message, send a `POST` request to the `/api/decrypt` endpoint with your encrypted message and key as parameters.
