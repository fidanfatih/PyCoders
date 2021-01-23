'''
## 4-unique_list
Write a function that filters all the unique(unrepeated) elements of a given list.

Example:
```
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output       : [1, 2, 3, 4, 5]
```
'''
def unique_list(n):
    print(list(set(n)))

unique_list([1,2,3,3,3,3,4,5,5])