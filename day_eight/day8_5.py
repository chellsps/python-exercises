import re

with open("insurance.txt", "r") as text:
	date_time = re.search(r"Date and Time of Accident:\s[a-zA-Z]{3}\s[0-9]+\s[0-9]{2,4},\s[0-9]+:[0-9]+[a-z]{2}\s[A-Z]+", text.read())
	if date_time:	
		print(date_time.group(0))
text.close()