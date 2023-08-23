def sieve_eratosthenes(n):
    def sieve(numbers, primes):
        if not numbers:
            return primes
        head, *tail = numbers
        primes.append(head)
        numbers = [x for x in tail if x % head != 0]
        return sieve(numbers, primes)

    # Generate a list of numbers from 2 to n
    numbers = list(range(2, n + 1))
    prime_numbers = sieve(numbers, [])

    return prime_numbers

# Test the function with an example
n = int(input("Enter the number that you want to use for limit the list > "))
prime_list = sieve_eratosthenes(n)
print(f"Prime numbers less than or equal to {n}: {prime_list}")
