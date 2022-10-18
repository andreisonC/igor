from email import header
import os, requests, getpass
from wsgiref import headers


print('------------------------\nFACEBOOK LOGIN \n------------------------')
id = raw_input('Email: ')
pw = getpass.getpass(prompt='Senha: ')
print('Cheking Login')
url = "https://facebook.com"
headers = {
    'User-Agent'
}