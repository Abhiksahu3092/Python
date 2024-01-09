#ternary operator in python
a,b=10,30
if a<b:
    min=a
else:
    min=b
    
print(min)

if a==b:
    print("a and b are equal")
else:
    if a>b:
        print("a is greater")
    else :
        print("b is greater")