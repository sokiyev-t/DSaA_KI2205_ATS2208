
def faktorial(n):
    p=1
    for i in range(1,n+1) :
        p=p*i
        # p*=i
    return p

def faktorial2(n):
    if n<2:
        return 1
    else:
        return n*faktorial2(n-1)

def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-2)+fib(n-1)


def countdown(n):
    print(n)
    if n<=0:
        return
    countdown(n-1)

countdown(5)




n=6
res=fib(n)
print(f"Result fibonachi: {res}")

# res=faktorial2(n)
# print(f"Result2: {res}")
