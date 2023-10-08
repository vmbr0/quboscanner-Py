import socket
import os

name = input("Entrer Le nom de domaine: ")

print(f"IPv4: {socket.gethostbyname(name)}")

iprange = input("Entrez l'adresse IP: ")
portrange = input("Entrez la plage de ports (xxx-xxx): ")
threads = input("Rentrer thread: ")
timeout = input("Entrez le délai de timeout: ")
os.system(
    "java -Dfile.encoding=UTF-8 -jar qubo.jar -noping -ports " + portrange + " -th " + threads + " -ti " + timeout + " -all -range " + iprange)

print("Done Checking")