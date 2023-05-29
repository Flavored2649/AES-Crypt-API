# AES Crypt API Documentation

This API provides powerful and efficient AES encryption and decryption functionality. It is implemented using Python and Flask.

## API Endpoints

There are two main API endpoints:

1. `/api/encrypt`: For encrypting a message.
2. `/api/decrypt`: For decrypting a message.

## Encryption

To encrypt a message, make a GET request to the `/api/encrypt` endpoint, and provide the plaintext message and the key as query parameters.

Example request using curl:

```bash
curl "https://aes-crypt.com/api/encrypt?message=Hello%20World&key=4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805"

## Decryption

To decrypt a message, make a POST request to the `/api/decrypt` endpoint, and provide the encrypted message and the key as JSON payload.

Example request using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"message":"ETGL1sW1fFk8zoxnf03WMw== xv/Z G18vhB/1B4WPePjh1bSvRQ==", "key":"4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805"}' https://aes-crypt.com/api/decrypt
