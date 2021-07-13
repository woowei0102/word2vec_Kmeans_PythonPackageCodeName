def _fibo(n):
    if(n == 0):
        return 0;
    elif (n == 1):
        return 1;
    return (_fibo(n-1) + _fibo(n-2))

test = int(input("Enter a number: "))
print(_fibo(test))