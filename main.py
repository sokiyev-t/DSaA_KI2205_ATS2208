import  math
def my_max(a, b):
    if a>b:
        return a
    else:
        return b

def my_round(a):
    b=a-int(a)
    if b>=0.5:
        return int(a)+1
    else:
        return int(a)
l=35
b=my_round(76.2)
print("Ceil result: ",b)
b=my_max(l,12)
print(b)
# k=1000
# n=0
# for i in range(2,math.ceil( math.sqrt(k))+1):
#     if k%i==0:
#         n=n+1
#         print(i ,'-delitel ',k)
#         break
# if n>0:
#     print("Chslov sostavnoe")
# else:
#     print("Chislo prostoe")
# for i in range(1,101):
#     if i%2==0:
#         print(i, "-even number")
#     else:
#         print(i,"-odd number")
