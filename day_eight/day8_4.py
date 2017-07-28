import re

with open("insurance.txt", "r") as text:
	# address = re.search(r"Address:\s[0-9]+\s[A-Z]\s[a-zA-Z0-9]+\s[a-zA-Z]+\nCity:(\s[a-zA-Z]+)+\nPin:\s[0-9]+", text.read())
	address = re.search(r"Address:.+\nCity:(\s[a-zA-Z]+)+\nPin:\s[0-9]+", text.read())
	if address:	
		print(address.group(0))
text.close()