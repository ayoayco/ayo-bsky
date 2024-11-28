from atproto import Client
import configparser

config = configparser.RawConfigParser()
config.read('config.txt')

user = config['ayo-bsky']['user'].strip('"')
password = config['ayo-bsky']['password'].strip('"')

client = Client()
client.login(user, password)

post = client.send_post('test?')

