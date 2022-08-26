#Print the Fibonacci series using the recursive method.


def fib_ser(n):
    #base case if n is less or equal to 1
    if n <= 1:
        return n

    return fib_ser(n-1) + fib_ser(n-2)


n_terms = 10

for i in range(n_terms):
    print(fib_ser(i))


#Fibonacci series without recursive method
nterms = 20

def rec_method(nterms):
    n1,n2 = 0,1
    count = 0

    if nterms < = 0:
        print("Please enter positive integer")

    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
