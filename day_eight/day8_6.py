import re

with open("insurance.txt", "r") as text1:
	position_x = re.findall(r":\s\nX\n", text1.read())
	if len(position_x) == 2:	
		signed = True
	else:
		signed = False
	print("Signed", signed)
text1.close()