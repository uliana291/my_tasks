import math

def check_if_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    m = 5
    while m <= math.sqrt(num):
        if num % m == 0:
            return False
        m = m + 1
    return True


def next_number(previous):
    next = previous + 1
    while check_if_prime(next) == False:
        next = next + 1
    return next


def main():
    print('Welcome to application of prime numbers. The only aim of it is printing prime numbers')
    answer = 'Y'
    prime = 1
    while answer == 'Y':
        prime = next_number(prime)
        print(str(prime))
        answer = input('Next? (Y/N)')


if __name__ == "__main__":
    main()
