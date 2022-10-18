import subprocess



data = subprocess.check_output(["netsh","wlan","show","profiles"], encoding='cp860')
print(data)
nome_wifi = input('Digite nome do wifi: ')
data2 = subprocess.check_output(["netsh","wlan","show","profiles", nome_wifi, "key", "=", "clear"], encoding='cp860')
print(data2)