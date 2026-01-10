def arthmatic_op(num,n):
    sum=0
    sub=0
    result=1
    if n==1:
        for i in nums:
            sum+=i
        return sum
    elif n==2:
        for i in nums:
            sub-=i
        return sub
    elif n==3:
        for i in nums:
            result*=i
        return result
    elif n==4:
        for i in nums:
            result/=i
        return result

def arthmatic(x,y,n):
    if n==1:
        return x+y
    elif n==2:
        return x-y
    elif n==3:
        return x*y
    elif n==4:
        return x/y
    else :
        return "invalid number"

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

























