'''pyramid sum'''
input_1=int(input())
result=input_1*1
num=2
for i in range(input_1-1,0,-1):
    result+=2*i*num
    num+=1
    print(result)
