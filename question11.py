'''You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. 
Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.
– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.
Example:
Input 1:
aA1_67
Input 2:
a987 abC012
Output 1:
1
Output 2:
0'''

def checkpassword(str):
    if str is None or len(str) == 0:
        return -1
    n = len(str)
    if n < 4:
        return 0
    has_digit = False
    has_upper = False
    for char in str:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char == ' ' or char == '/':
            return 0
    if has_digit and has_upper:
        return 1
    return 0

print(checkpassword("aA1_67"))
    