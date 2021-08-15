# Easy 1
def showNum():
    print('Fizz Buzz number from 1 to 100')
    allnum = []
    for i in range(100):
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            allnum.append("FizzBuzz")
        elif (i+1)%3 == 0:
            allnum.append("Fizz")
        elif (i+1)%5 == 0:
            allnum.append("Buzz")
        else: 
            allnum.append(i+1)

    for i in range(100):
        if (i+1)%20 == 0:
            print(allnum[i])
        else:
            print(allnum[i], end= " ")


# Easy 2
def leapyear():
    print('Determine a leap year')
    while True:
        try:
            year = int(input('Please input year: '))
            if year%400 == 0 or (year%100 != 0 and year%4 == 0):
                print(f'{year} -> true')
            else:
                print(f'{year} -> false')
        except:
            print('End the program!\nInput is not an integer.')
            break


# Easy 3.1
def star1():
    print('Enter an integer input n')
    while True:
        try:
            n = int(input('n='))
            for i in range(n):
                print('*'*(i+1))
        except:
            print('End the program!\nInput is not an integer.')
            break


# Easy 3.2
def star2():
    print('Enter an integer input n')
    while True:
        try: 
            n = int(input('n='))
            for i in range(n):
                print(' '*(n-i-1) , end='')
                print('*'*(i+1))
        except:
            print('End the program!\nInput is not an integer.')
            break


# Easy 3.3
def star3():
    print('Enter an integer input n')
    while True:
        try:
            n = int(input('n='))
            for i in range(n):
                print(' '*(n-i-1) , end='')
                print('*', end='')
                print(' '*(2*i-1) , end='')
                if i == 0:
                    print('')
                else:
                    print('*')
        except:
            print('End the program!\nInput is not an integer.')
            break


# Easy 3.4
def star4():
    print('Enter an integer input n')
    while True:
        try:
            n = int(input('n='))
            j = n
            for i in range(n):
                j -= 2
                s = 1
                if i == n//2:
                    s = (n+1)%2
                    k = i - s
                    j += 2
                elif i < n//2:
                    k = i
                elif i > n//2:
                    k -= 1
                print(' '*k, end='')
                print('*', end='')
                print(' '*abs(j), end='')
                print('*'*s)
        except:
            print('End the program!\nInput is not an integer.')
            break


# Easy 3.5
def star5():
    print('Enter an integer input n')
    while True:
        try:
            n = int(input('n='))
            j = n//2-1
            for i in range(n):
                if n%2 == 0:
                    if i == n//2:
                        print('*'*(n-1))
                    else:
                        print(' '*abs(j), end='')
                        print('*'*(n-2*(abs(j))-1))
                        j -= 1
                else:
                    print(' '*abs(n//2-i), end='')
                    print('*'*(n-2*(abs(n//2-i))))
        except:
            print('End the program!\nInput is not an integer.')
            break


# Easy 3.6
def alpha():
    print('Enter an integer input n')
    while True:
        try:
            alp = [chr(c) for c in range(65,70)]
            n = int(input('n='))
            l = 2*n-1
            for i in range(l):
                if i == 0:
                    print(alp[0]*(n-i-1), alp[1]*(n-i-1), sep='+')
                elif i == l-1:
                    print(alp[2]*(i-n+1), alp[3]*(i-n+1), sep='+')
                elif i <= n-1:
                    print(alp[0]*(n-i-1), alp[4]*(2*i-1), alp[1]*(n-i-1), sep='+')
                    j = 2*i-1
                elif i > n-1:
                    j -= 2
                    print(alp[2]*(i-n+1), alp[4]*(j), alp[3]*(i-n+1), sep='+')
        except:
            print('End the program!\nInput is not an integer.')
            break

# Easy 4
def specific():
    print("Difference between 'else' and 'finally'.")
    print("'else' is executed when error occurs in try and that error can't match any 'except' type,",\
            "\nbut 'finally' is always executed at the end after 'try', 'except', or 'else' is executed.")


# Medium 1
def primeNum():
    print('Find all prime numbers up to an integer n')
    while True:
        try:
            n = int(input('n='))
            print(n, '->', end=' ')
            prime = []
            for i in range(2, n+1):
                for j in prime:
                    if (i % j) == 0:
                        break  
                else:
                    prime.append(i)
                    print(i,end=' ')
            print('')
        except:
            print('End the program!\nInput is not an integer.')
            break

if __name__ == '__main__':
    print('This is funtion module. Please run the test.py')
