n=int(input("Enter length:"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c
