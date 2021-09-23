# Fibonacci Serisi

def Fibonacci(first, second, max):
    if first + second > max:
        pass
    else:
        print("{} - {}".format(second, first + second))
        Fibonacci(second, first + second, max)

max = int(input("Enter Max: "))
Fibonacci(1, 2, max)