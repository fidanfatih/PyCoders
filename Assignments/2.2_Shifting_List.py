'''
2.
Write a program that takes two inputs; 
one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) 
when n is positive (negative). 
Use wrap-around: if an element is shifted beyond the end of the list, 
then continue to shift starting at the beginning of the list.

Example:

Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3] 
Inputs>>> [1, 2, 3, 4, 5], -2 
Output>>> [3, 4, 5, 1, 2]
'''
x=[int(i) for i in input('Enter the number list with a space between the elements: ').split()]
shift=int(input('Enter the shifting count(s): '))
shift=shift%len(x)
x=x[-shift:]+x[:-shift]
print('Output:',x)