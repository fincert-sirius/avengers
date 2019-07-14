from ipwhois import IPWhois
import socket


domains = [
    'yandex.ru', 'google.com', 'adobe.com', 'mail.ru', 'archlinux.org', '123piska2.ga',
    'olo2332df.sd', 'hermajor.ru', 'sochisirius.ru', 'parksirius.ru', 'chlen321.kz'
]

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return 'error'

for domain in domains:
    print(domain, ':', get_ip(domain))
