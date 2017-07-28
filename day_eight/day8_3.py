import re

with open("insurance.txt", "r") as text:
	claim = re.search(r"Claim Number:\s[A-Z]{2}-\d+", text.read())
	if claim:	
		print(claim.group(0))
text.close()