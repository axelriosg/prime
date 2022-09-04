#'(n-1)!^2 mod n' equals 1 if n is prime and 0 if it is not.

def main():

    import math
    n = int(input("Escribe un número: "))
    i = (n-1)
    result1 = math.prod(range(i, 0, -1))
    x = ((result1)**2)%n
    if x == 1:
        print("Es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    main()
