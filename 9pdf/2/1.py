def q1():
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):  # Check only up to √n
            if n % i == 0:
                return False
        return True

    l = []  # List to store prime factors

    def primeFactors(n: int, i=2):
        if n <= 1:  # Base case: when n is fully reduced
            print(l)
            return
        while n % i == 0:
            l.append(i)
            n //= i  # Reduce n
        primeFactors(n, i + 1)  # Move to the next factor

    num = int(input("Enter a number: "))  # Allow user input
    primeFactors(num)

q1()
