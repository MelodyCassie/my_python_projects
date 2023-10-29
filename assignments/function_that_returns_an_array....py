def prime_factors_product(num):
    factors = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.append(divisor)
            num /= divisor
        else:
            divisor += 1
    product = 1
    for factor in factors:
        product *= factor
    return factors, product

number = 60
prime_factors, product = prime_factors_product(number)
print("Prime Factors of", number, ":", prime_factors)
print("Product of Prime Factors:", product)
