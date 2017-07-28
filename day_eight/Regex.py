import re

with open("insurance.txt", "r") as text:
	policy = re.search(r"Policy\sNumber\:\s*[0-9]{5}", text.read())
	policyNumber = policy.group(0)
	print(policyNumber)
text.close()

# Substitutions
file = re.sub("Sterling Archer", "Uma Pappiah", file)
file = re.sub(r"Address\:\s*(.*)", "80 E 3rd St Apt 5", file)
file = re.sub(r"City\:\s*(.*)", "City: New York", file)
file = re.sub(r"", "80 E 3rd St Apt 5", file)
file = 




# with open("newFile.txt", "a+") as newfile:
# This helps not only append the text but also create a file
with open("newFile.txt", "a+") as newfile:
	newfile.write(file)
	# newfile.close()
