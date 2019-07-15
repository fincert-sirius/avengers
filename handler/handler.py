import time
import socket
from ipwhois import IPWhois

class _Handler():
	def handle(self, domain):
		# MAAAGIICCCC
		time.sleep(15)
		verdict = 0
		comment = 'Some notes'
		category = 'lokhotron'
		return [verdict, category, comment]

	def get_whois(self, domain):
		ip = self.get_ip(domain)
		obj = IPWhois(ip, allow_permutations=True)
		info = obj.lookup_whois()
		return info

	def get_ip(self, domain):
		try:
			ip = socket.gethostbyname(domain)
			return ip
		except:
			return 'error'
