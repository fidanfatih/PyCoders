"""
## Bonus Question 2
[HACKERRANK: CAPITALIZE](https://www.hackerrank.com/challenges/capitalize/problem)
"""
def solve(s):
    return ''.join([s[i].upper() if i==0 or s[i-1]==' ' else s[i] for i in range(len(s))])
    
print(solve(input()))