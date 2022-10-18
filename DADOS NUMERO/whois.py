import os
from unittest import result
def get_whois(url):
    command = "whois" + url
    process = os.popen(command)
    results = str(process.read())
    return results
print(get_whois('thenewboston.com'))