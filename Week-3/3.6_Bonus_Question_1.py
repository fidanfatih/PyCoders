'''
## Bonus Question 1
[HACKERRANK: FIND DIGITS](https://www.hackerrank.com/challenges/find-digits/problem)

'''
def findDigits(n):
    items=''
    for i in str(n):
        if int(i)>0 and n%int(i)==0: items+=i
    return len(items)


t = int(input())
nums=[int(input()) for _ in range(t)]   
for n in nums: print(findDigits(n))