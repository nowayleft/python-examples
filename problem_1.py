
'''
Problem Statement:
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
  Find the sum of all the multiples of 3 or 5 below 1000.
'''

def func():
    n1, n2 = 3, 5
    m      = 1000
    out    = 0
    for i in range(1, m):
        if not i % n1 or not i % n2:
            out += i
    return out

if __name__ == '__main__':
    print func()


