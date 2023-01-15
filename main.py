import math as m

def check_prime():
    n=int(input('Enter a number-\n'))
    flag = False
    for i in range(2,(int(m.sqrt(n))+1)):
        if n%i==0:
            print(str(n)+' is not a prime number')
            flag=True
            break
    if not flag:
        print(str(n)+'  is a prime number')

check_prime()
