# AES Crypt API Examples

This document provides examples of how to use the AES Crypt API. The API consists of two endpoints, one for encryption and one for decryption.

## Encryption

The encryption endpoint is a GET request which takes two parameters:

- `message`: The plaintext message you want to encrypt.
- `key`: The 64-character, hexadecimal-encoded encryption key.

Here's an example of how you might use this endpoint:

``bash
curl "https://aes-crypt.com/api/encrypt?message=Hello%20World&key=4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805"
\```

And the Python example using `requests` library:

\```python
import requests

params = {
    "message": "Hello World",
    "key": "4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805"
}

response = requests.get("https://aes-crypt.com/api/encrypt", params=params)

print(response.json())
\```

## Decryption

The decryption endpoint is a POST request which also takes two parameters:

- `message`: The ciphertext message you want to decrypt.
- `key`: The 64-character, hexadecimal-encoded decryption key.

Here's an example of how you might use this endpoint:

``bash
curl -X POST "https://aes-crypt.com/api/decrypt" -d "message=ETGL1sW1fFk8zoxnf03WMw== xv/Z G18vhB/1B4WPePjh1bSvRQ==&key=4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805"
\```

And the Python example using `requests` library:

\```python
import requests

data = {
    "message": "ETGL1sW1fFk8zoxnf03WMw== xv/Z G18vhB/1B4WPePjh1bSvRQ==",
    "key": "4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805"
}

response = requests.post("https://aes-crypt.com/api/decrypt", data=data)

print(response.json())
\```
