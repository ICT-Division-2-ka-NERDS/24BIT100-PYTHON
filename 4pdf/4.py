def q4():
    def is_prime():
        num = int(input("Enter a number: "))
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    
    def is_perfect():
        num = int(input("Enter a number: "))
        divisor_sum = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                divisor_sum += i
        return num == divisor_sum


    def is_armstrong():
        num = int(input("Enter a number: "))
        digits = str(num)
        return num == sum(int(d)**len(digits) for d in digits)

    def is_palindrome():
        num = int(input("Enter a number: "))
        s = str(num)
        return s == s[::-1]

    def is_automorphic():
        num = int(input("Enter a number: "))
        return str(num**2).endswith(str(num))

    print("Prime:", is_prime())
    print("Perfect:", is_perfect())
    print("Armstrong:", is_armstrong())
    print("Palindrome:", is_palindrome())
    print("Automorphic:", is_automorphic())
q4()