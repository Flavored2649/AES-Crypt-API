import requests

# Define the URL for the decryption endpoint
url = 'https://aes-crypt.com/api/decrypt'

# Define your encrypted message and key from previous encryption
encrypted_message = 'Encrypted message from the previous example'
key = '4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805'

# Define the parameters for the request
params = {'message': encrypted_message, 'key': key}

# Send a POST request to the decryption endpoint
response = requests.post(url, params=params)

# Get the decrypted message from the response
decrypted_message = response.json()['result']

print('Decrypted message:', decrypted_message)
