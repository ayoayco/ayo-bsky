from atproto import Client
import configparser

config = configparser.RawConfigParser()
config.read('config.txt')

password = config['ayo-bsky']['password'].strip('"')

client = Client()
client.login('ayco.io', password)

post = client.send_post('test?')

