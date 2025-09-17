import socket
import subprocess

def main():
    try:
        # Nom de domaine
        name = input("Entrez le nom de domaine: ").strip()
        ipv4 = socket.gethostbyname(name)
        print(f"[+] IPv4: {ipv4}")
    except Exception as e:
        print(f"[!] Erreur lors de la résolution du domaine: {e}")
        return

    # Plage d’IP
    iprange = input("Entrez l'adresse IP ou plage (ex: 192.168.1.1-255): ").strip()

    # Plage de ports
    portrange = input("Entrez la plage de ports (ex: 20-1000): ").strip()
    if "-" not in portrange:
        print("[!] Format de plage invalide, exemple attendu: 20-1000")
        return

    # Threads (par défaut 10)
    threads = input("Entrez le nombre de threads [defaut=10]: ").strip()
    if not threads.isdigit():
        threads = "10"

    # Timeout (par défaut 2s)
    timeout = input("Entrez le délai de timeout (sec) [defaut=2]: ").strip()
    if not timeout.isdigit():
        timeout = "2"

    # Commande finale
    cmd = [
        "java", "-Dfile.encoding=UTF-8", "-jar", "qubo.jar",
        "-noping",
        "-ports", portrange,
        "-th", threads,
        "-ti", timeout,
        "-all",
        "-range", iprange
    ]

    print("\n[+] Exécution de la commande :")
    print(" ".join(cmd))

    try:
        subprocess.run(cmd, check=True)
        print("\n[✓] Scan terminé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Erreur lors de l'exécution du scan: {e}")
    except FileNotFoundError:
        print("[!] Erreur: qubo.jar ou Java introuvable.")

if __name__ == "__main__":
    main()
