# def remove_quotes(string):
# 	if len(string)>0:
# 		if string[0] == '"':
# 			string  = string[1:len(string)]
# 			return string
# 		elif string[len(string)-1] == '"':
# 			string = string[0:len(string)-1]
# 			return string
# 		else:
# 			return string
# 	else:
# 		print("Outlier:", string)
# 		return string
```# EXERCISE 2
def count_words(fileName, n):
    with open(fileName) as file:
        fileString = file.read()
        fileString = fileString.translate(string.punctuation)
        # fileString = fileString.replace(",","")
        # fileString = fileString.replace(".","")
        # fileString = fileString.replace('"',"")
        wordList = fileString.split(" ")
        wordCountDict = {}
        for item in wordList:
            word = item.lower()
            word =  word.replace('"', '')
            word = re.sub(r'[\.\?\"\"\:\;\,\(\)\+]', "", word)
            word = remove_quotes(word)
            if word == "":
                pass
            else:
                if word in wordCountDict.keys():
                    wordCountDict[word] += 1
                else:
                    wordCountDict[word] = 1
        
        sortedTuples = sorted(wordCountDict.items(), key=operator.itemgetter(1), reverse=True)[:n]                
        for tupl in sortedTuples:
            print(tupl[0], tupl[1])


def remove_quotes(string):
    if len(string) > 0:
        if string[0] == '"':
            string = string[1:len(string)]
            return string
        elif string[len(string)-1] == '"':
            string = string[0:len(string)-1]
            return string
        else:
            return string
    else:
        pass

count_words("article.txt", 10)
```