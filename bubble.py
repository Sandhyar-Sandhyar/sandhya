def bubble (a):
    n=len(a)
    for i in range(n):
        for j in range (n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1],a[j]

a=[]
n=int(input("enter the size: "))
for s in range(n):
    n1=int(input("enter number: "))
    a.append(n1)
print("given array is",a)
bubble(a)
print(a)
