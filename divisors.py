def divisors(n):  # count divisors
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:

            counter = counter + 1
            print(counter)

        else:
            continue
    return counter


print(divisors(4))
