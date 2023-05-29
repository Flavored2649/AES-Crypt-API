import requests

# Define the URL for the encryption endpoint
url = 'https://aes-crypt.com/api/encrypt'

# Define your message and key
message = 'Hello, World!'
key = '4fbd8e11e545fdfc7e16d417bb464a9208674a6a6e830b0ed8f8f5855fb8e805'

# Define the parameters for the request
params = {'message': message, 'key': key}

# Send a GET request to the encryption endpoint
response = requests.get(url, params=params)

# Get the encrypted message from the response
encrypted_message = response.json()['result']

print('Encrypted message:', encrypted_message)
