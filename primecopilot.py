#Github Copilot version get in seconds.
#The prompt was "#a python program that finds if a number is prime or not using Wilson's theorem".


import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
def is_prime(n):
    if n == 1:
        return False
    return (factorial(n-1) + 1) % n == 0

def main():
    n = int(input('Enter a number: '))
    if is_prime(n):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')

    
if __name__ == "__main__":
    main()
    
