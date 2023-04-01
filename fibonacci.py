"""
10.fibonacci series
"""

def fibonacc(number):
    if number <=1:
        return number
    else:
        return fibonacc(number-1)+fibonacc(number-2)
        
        
number = int(input())
for i in range(0,number):
    print("fibonacci:",fibonacc(i))
