"""
## 1-perfect_number
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is `6`, which is the sum of `1`, `2`, and `3`. 

Some other perfect numbers are `28(1+2+4+7+14=28)`, `496` and `8128`.

Write a function that finds perfect numbers between `1` and `1000`.
Check perfect numbers between `1` and `1000` and find the sum of the perfect numbers using reduce and filter functions. <br />
"""
def isperfect(num):
    multipliers = [i+1 for i in range(num//2) if num%(i+1)==0]
    return sum(multipliers)==num

def perfect_nums(up):
    return [j+1 for j in range(up) if isperfect(j+1)]
    
up=1000
p_nums=perfect_nums(up)
print(f"Perfect Numbers between 1 and {up}:\n{p_nums}")
print("\nSum of the perfect numbers:",
      reduce(lambda x,y:x+y, filter(lambda x: x in p_nums, range(up))),sep="\n")