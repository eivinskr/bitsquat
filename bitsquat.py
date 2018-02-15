from __future__ import print_function
import re
from scapy.all import *
import domains

def transpose(character):
	b = ord(character)
	return map(lambda x: chr(b ^ (2 ** x)), xrange(8))


domain_name = "mydomain.foo"
valid_domains = []
invalid_domains = 0
registered_domains = []

for position, letter in enumerate(domain_name):
	transposed_values = transpose(letter)
	for value in transposed_values:
		new_list = list(domain_name)
		if new_list[position] == value.lower():
			invalid_domains += 1
			continue
		new_list[position] = value
		result = "".join(new_list)
		try:
			result.decode('ascii')
			if bool(re.match("^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$", result)) and result.rsplit('.', 1)[1].upper() in domains.valid_top_domains:
				answer = ""
				try:
					answer = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=result)),verbose=0)
					valid_domains.append(result)
				except AttributeError:
					invalid_domains += 1
					continue
				except:
					print("Unexpected error:", sys.exc_info()[0])
				if answer[DNS].summary()[8:] != "":
					registered_domains.append(result)
				else: 
					print(result)
			else:
				invalid_domains += 1
		except UnicodeDecodeError:	# it was not a ascii-encoded unicode string
			invalid_domains += 1


print (str(len(valid_domains)) + " valid domains that are not yet registered.")
print (str(invalid_domains) + " invalid domains.")
print (str(len(registered_domains)) + " registered domains:")

map(print, registered_domains)


