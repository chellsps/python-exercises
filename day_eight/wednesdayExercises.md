Exercise 1:
Please write a program which count and print the numbers of each character, from file letters.txt, in a string input by console.

Example:
If the following string is given as input from file letters.txt to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.


Exercise 2:

Write a program that takes a filename and a parameter `n` and prints the `n` most common words in the file, and the count of their occurrences, in descending order.

For example:

        word_stats("article.txt", 5)

        "the", 39
        "device", 21
        "start", 14
        "pidgeon", 9
        "box", 3

Import the included `article.txt` file and use that to test your program. What are the top 10 words and their frequency?

#### Regex 

Exercise 3:# go to http://pythex.org/
find match for: 906483755
find match for: 12/35/2007
find match for: 123 Fake St. New York, NY.
find match for: only pairs of 2 numbers in: 4793997252330974750072625122298


*Use Insurance.txt for ex 4-10

Exercise 4:
open and read insurance.txt


Exercise 5:
locate and print Policy Number


Exercise 6:
locate and print Claim Number


Exercise 7:
locate and print Address


Exercise 8:
locate and print Date and Time of Accident


Exercise 9:
Verify (return True/False) Document is signed with 'X' in two places on document

Exercise 10:
Verify (return True/False) 'Email' field has valid email address (has proper symbols and syntax)



### Looking Further

Long Exercise 1:
Create test-file2.txt and populate it with Insruance form updated with YOUR personal information.

hint: use 'write' mode with open()



Long Exercise 2:

A very prestigious art gallery has contacted you regarding a job. Get to work! 

Management wants to figure out how many people visit each room in the gallery, and for how long: this is to help improve the quality of the overall gallery in the future.

Your goal is to write a program that takes a formatted text file that describes the overall gallery's foot-traffic on a minute-to-minute basis. From this data you must compute the average time spent in each room, and how many visitors there were in each room.

###The Input

Each line in the text file represents either a visitor entering or leaving a room. It starts with an integer, representing a visitor's unique identifier. Next on this line is another integer, representing the room's number. Next is a single character, either 'I' (for "In") for this visitor entering the room, or 'O' (for "out") for the visitor leaving the room. Finally, at the end of this line, there is a time-stamp integer: it is an integer representing the minute the event occurred during the day. All of these elements are space-delimited.

You may assume that all input is logically well-formed: for each person entering a room, he or she will always leave it at some point in the future. A visitor will only be in one room at a time.

Note that the order of events in the log are not sorted in any way; it shouldn't matter, as you can solve this problem without sorting given data.

Sample Input:

        0 0 I 540
        1 0 I 540
        0 0 O 560
        1 0 O 560

###The Output

For each room that had log data associated with it, print the room number, then print the average length of time visitors have stayed as an integer, and then finally print the total number of visitors in the room. All of this should be on the same line and be space delimited; you may optionally include labels on this text, like in our sample output 1.

Sample Output:

        Room 0, 20 minute average visit, 2 visitor(s) total

###Loading the Text File

You'll find a text file `traffic.txt` in this repo. Import this text file and parse it to get the results.

When you are done solving the problem, write your output to another text file and save it in the repo.








