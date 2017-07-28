import re

with open("insurance.txt", "r") as text:
	policy = re.search(r"Policy Number:\s*[0-9]{5}", text.read())
	if policy:
		print(policy.group(0))
text.close()