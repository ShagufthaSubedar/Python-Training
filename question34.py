'''Pangram is a sentence containing every letter in the English alphabet. Given a string, 
find all characters that are missing from the string, Le., the characters that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output:abdhijnpquvxyz'''

def missing_chars(input_string):
    all_chars=set('abcdefghijklmnopqrstuvwxyz')]
    input_chars=set(input_string.lower())
    missing_letters=all_chars-input_chars
    missing_letters_sort=sorted(missing_letters)
    result=''.join(missing_letters_sort)
    return result

input_string=input()
print(missing_chars(input_string))