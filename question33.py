
'''1) Signature for LCM
Given two numbers a and b. Find the GCD and LCM of and d.
Input:
• Two positive integers a and b (1 <=a, b <=1000)
Output:
For GCD function, an integer representing the GCD of a 'and b
For LCM function, an integer representing the LCM of a and b
Sample Input:
12 18
Output:
6
36'''

def gcd(a,b):
    while (b>0):
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b/gcd(a,b)
a=int(input())
b=int(input())
result_gcd=gcd(a,b)
result_lcm=lcm(a,b)
print(result_gcd)
print(result_lcm)

