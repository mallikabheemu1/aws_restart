"""
1.Greatest number
"""
a = int(input())
b = int(input())
c = int(input())

if a >b:
    if(a>c):
        print("a is greatest number:",a)
    else:
        if(c>a and c>b):
            print("c is greatest:",c)
        else:
            print("b is greatest:",b)
