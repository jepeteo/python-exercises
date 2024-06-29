def get_prime_factors(number):
    if number < 2:
        return []

    factors = []
    divisor = 2

    while divisor * divisor <= number:
        while (number % divisor) == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    if number > 1:
        factors.append(number)

    return factors

num = int(input("Enter a number: "))
if num < 1:
    print("Please enter a positive integer greater than 0.")
else:
    print(f"Prime factors of {num}: {get_prime_factors(num)}")