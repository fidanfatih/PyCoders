'''
3.
Write a code snippet that inputs a sentence from the user, 
then uses a dictionary to summarize the number of occurrences of each letter. 
Ignore case, ignore blanks and assume the user doesnot enter any punctuation. 
Display a two-column table of the letters and their counts with the letters in sorted order.

Example:

Input >>> "This is a sample text with several words This is more sample text with some differentwords..." 
Output >>> [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)] 
'''
from collections import Counter
text=input('Enter a text: ')
dict=Counter(text.lower())
print(sorted([(k,v) for k,v in dict.items() if k.isalpha()]))