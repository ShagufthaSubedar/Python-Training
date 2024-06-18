def reverse_number(num, reversed_num=0):
    if num == 0:
        return reversed_num
    else:
        return reverse_number(num // 10, reversed_num * 10 + num % 10)
    
num = 12345
print(reverse_number(num))