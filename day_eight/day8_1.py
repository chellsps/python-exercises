import re

# If you need to open a file in  another folder then it should be written as 
# with open("../../python/insurance.txt", "r") as text: 
# where ..refers to the number of levels of directory

with open("insurance.txt", "r") as text:
	print(text.read())
text.close()
