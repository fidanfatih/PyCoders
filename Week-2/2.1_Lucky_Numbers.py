"""
1.Write a programme to generate the lucky numbers from the range(n). 
These are generated starting with the sequence s=[1,2,...,n]. 
At the first pass, we remove every second element from the sequence, resulting in s2. 
At the second pass, we remove every third element from the sequence s2, resulting in s3, 
and we proceed in this way until no elements can be removed. 
The resulting sequence are the numbers lucky enough to have survived elimination.
The following example describes the entire process for n=22:

Original sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
Remove 2nd elements: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
Remove 3rd elements: [1, 3, 7, 9, 13, 15, 19, 21]
Remove 4th elements: [1, 3, 7, 13, 15, 19] 
Remove 5th elements: [1, 3, 7, 13, 19]
We cannot remove every other 6th element as there is no 6th element.
Input>>> 22 
Output>>> Lucky numbers are [1, 3, 7, 13, 19]
"""

n=int(input('Enter the upper limit of Lucky Number Series: '))
x,step=list(range(1,n+1)),2

while(step<=len(x)):
    x=[x[i] for i in range(0,len(x)) if (i==0) or ((i+1)%step)>0]
    step+=1
print(f"Lucky numbers are {x}")