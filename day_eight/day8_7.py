import re

with open("insurance.txt", "r") as text1:
	email = re.findall(r"Email:\s\w+@\w+\..+", text1.read())
	if len(email) >= 1:	
		print("Valid mail id", email)
	else:
		print("Invalid")
text1.close()


