import requests

#获取自己的公网ip
ip = requests.get("https://checkip.amazonaws.com").text.strip()
print(ip)