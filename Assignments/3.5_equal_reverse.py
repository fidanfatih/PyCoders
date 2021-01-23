"""
## 5-equal_reverse
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:
```
Input  >>> madam, tacocat, utrecht 
Output >>> True, True, False
```
"""
def equal_reverse(text):
    words = map(lambda x:x.strip(),text.split(','))
    print( [i==i[::-1] for i in words] )

equal_reverse(input())