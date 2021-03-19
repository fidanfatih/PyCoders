'''
4.
Write a program that takes in two words as input and returns a list containing three elements, in the following order:

Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. 
The strings will always be in lowercase and will not contain any punctuation.

Example:

Input1>>> "sharp" 
Input2>>> "soap" 
Output>>> ['aps', 'hr', 'o']
'''
word_1=[i for i in input("Word 1: ").lower() if i.isalpha()]
word_2=[i for i in input("Word 2: ").lower() if i.isalpha()]


intersection=''.join(sorted(set(word_1).intersection(word_2)))
difference_12 = ''.join(sorted(set(word_1).difference(set(word_2))))
difference_21 = ''.join(sorted(set(word_2).difference(set(word_1))))
print([intersection,difference_12,difference_21])