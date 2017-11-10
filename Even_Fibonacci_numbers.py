



"""Questions or Problems:
1. Generate the infinite sequence
2. nth term
3. 
"""

def main_func(N = 4000000): # Int -> Int (MaxN -> sum)
    A = fib_gen(1,2)
    s = 0
    for i in A:
        if isEven(i):
            s += i # Update s
        # Stop Criterion
        if i > N: # Exit Loop
            break
    return s

def fib_gen(F0, F1): # Infinite Fibonacci Sequence 
    # (F0, F1) = (1, 2)
    a, b = F0, F1
    while 1:
        yield a
        a, b = b, a + b

def isEven(x): # Int -> Bool
    return x%2 == 0

def test_run():
    print(main_func())


if __name__ == '__main__':
    test_run()
