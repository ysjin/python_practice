
def fibonacci (num):
    fib = [0, 1]
    for i in range(2, num+1):
        fib[i%2] = fib[0] + fib[1]

    if (num%2)==0 :
        return fib[0]
    else:
        return fib[1]


def main():
    print( fibonacci(7) )



if __name__ == "__main__": main()
