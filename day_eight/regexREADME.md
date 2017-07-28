# Regular Expressions

### Python 're' module

#### Links to Documentation/Sources
```
https://docs.python.org/3.3/library/re.html?highlight=regex#re.regex.findall

http://pythex.org/

http://www.diveintopython3.net/regular-expressions.html

```
- To use regular expressions, import module 're'
```
import re
```
examples:
- ```re.findall()```
- ```re.split()```
- ```re.search()```
- ```re.match()```

### Special Characters:

- '.'' matches any character, except for a new line
- '^' Match the beginning of a string; in MULTILINE mode matches start of new line 
- '$' Match the end of a string, or just before new line i.e ```ab$``` matches ```'ab'``` only at end of line
- '*' Match 0 or more (all)
- '+' Match 1 or more i.e. ```ab+``` the occurance of ```'ab'```,```'abb'```,```'abbbbb'```, etc in line
- '?' Match 0 or 1 i.e.  ```ab?``` will match either ```'a'``` or ```'ab'``` ('b' is optional because '?'' modifies 'b')
- '*?','+?','??' The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE ```<.*>``` is matched against ```<H1>title</H1>```, it will match the entire string, and not just ```<H1>```. Adding '?' after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched
- {n} matches exactly number n time of occurance i.e ```ab{5}``` will match ONLY if ```'ab'``` appeares 6 times 
- {m,n} Match m to n number of times (can be any range of digits) ie ```ab{1,3}``` matches 1 to 3 occurances of ```'ab'```
- '[]' range or variance i.e. [A-Z], [a-zA-Z0-9]
- '|' either/or


### Identifiers:

- ```\d``` any number
- ```\D``` anything but a number
- ```\s``` space
- ```\S``` anything but a space
- ```\w``` any character
- ```\W``` anything but a character
- ```\b``` the white space around words
- ```\.``` a period
- ```\1``` repeating char


### White Space Characters

- ```\n``` new line
- ```\s``` space
- ```\t``` tab
- ```\e``` escape
- ```\f``` form feed
- ```\r``` return


### Additional Info

- ```., +, *, ?, [], $, ^, (), {}, |, \``` all have to be escaped.

### Reading .txt file

```
https://docs.python.org/3/library/functions.html#open
```

- ```var = open("textfile","mode")```
- ```var.close()```  
*important to close after finished to preserve memory

#### Open Modes

- ‘r’ – Read mode which is used when the file is only being read 
- ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
- ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
- ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 

### Working Examples

```
with open("test-file.txt", "r") as text
	print(text.read())
text.close()

with open("test-file2.txt", "w") as text
	text.write('Adding text to new file.\n')
text.close()

with open("test-file3.txt", "a") as text
	text.write('Adding text to end of test-file3 content only if t=file already exists.\n')
text.close()
```

### Putting it all together:

```
with open("test-file.txt", "r") as text
	policy = re.search('Policy Number:\s(*)', text)
text.close()
print(policy)
```