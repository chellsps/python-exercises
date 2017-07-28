# word_file = open('words.txt')
# print(word_file)
# print(word_file.readline())
# print(word_file.readline())
# print(word_file.readline())
# Exercise 1.
# for word in word_file:
#   print(word)
# Exercise 2.
# for word in word_file:
#   if len(word) > 20:
#       print("len > 20", word)
# def has_no_e(word):
#     for char in word:
#         if char in 'Ee':
#             return False
#     return True 
# count = 0
# for word in word_file:
#     # word = line.strip()
#     if has_no_e(word):
#         count += 1
#         print(word)
# percent = (count / 113809.0) * 100
# print ("{:.5}% of the words don't have an 'e'.".format(str(percent)))
#write a file
file = open('output.txt', 'w')
line = "this is my first txt file"
# x=77
# file.write(str(x))
alist = [22,33,44,55]
for x in alist:
    a = '\n' + str(x)
    file.write(a)
# file.write(line)
file.close()