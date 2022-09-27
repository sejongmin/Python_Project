import socket
import requests
import re

#컴퓨터 내부 IP알아보는 코드
#in_addr = socket.gethostbyname(socket.gethostname())

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP: ",in_addr.getsockname()[0])

#컴퓨터 외부 IP알아보는 코드
req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("d외부 IP: ", out_addr)
