# -*- coding: utf-8 -*-
import argparse
import sys
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="the message to encrypt or decrypt")
    parser.add_argument("-k", "--key", help="the encryption key (32 bytes, hex encoded)")
    parser.add_argument("-a", "--action", help="the action to perform (encrypt/decrypt)", choices=['encrypt', 'decrypt'])
    args = parser.parse_args()

    if args.key is None or args.action is None or args.message is None:
        print("You must specify a key, a message and an action.")
        sys.exit(1)

    try:
        key = args.key
        message = args.message
        action = args.action

        base_url = 'https://aes-crypt.com/api/'

        if action == 'encrypt':
            url = base_url + 'encrypt'
        elif action == 'decrypt':
            url = base_url + 'decrypt'

        params = {
            'key': key,
            'message': message
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(response.json()['result'])
        else:
            print("An error occurred: ", response.content)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
