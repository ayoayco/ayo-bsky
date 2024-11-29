from atproto import Client, client_utils
import configparser

def main():
    config = configparser.RawConfigParser()
    config.read('config.txt')

    user = config['ayo-bsky']['user'].strip('"')
    password = config['ayo-bsky']['password'].strip('"')

    client = Client()
    client.login(user, password)

    text = client_utils.TextBuilder().text('Hello World from ').link('Python SDK', 'https://atproto.blue')
    client.send_post(text)

if __name__ == "__main__":
    main()