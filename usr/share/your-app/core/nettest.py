import socket
import subprocess
import requests

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return "Интернет работает \n"
    except:
        return "Интернет не работает \n"

def check_ping(host = "8.8.8.8"):
    try:
        output = subprocess.getoutput(f"ping -c 3 {host}")
        return f"Ping {host}: \n {output}\n"
    except:
        return f"Ping {host} неудачен"
    
def check_dns(domain = "google.com"):
    try:
        ip = socket.gethostbyname(domain)
        return f"DNS: {domain} -> {ip} \n"
    except:
        return f"Ошибка разрешения для {domain} \n"
        
def net_test():
    result = []
    result.append(check_internet())
    result.append(check_ping())
    result.append(check_dns())
    return "\n".join(result)