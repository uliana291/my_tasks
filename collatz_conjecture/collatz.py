
def collatz_steps(n, steps):
    if n == 1:
        return steps
    else:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        steps += 1
        return collatz_steps(n, steps)


def main():
    print("This is a program for collatz conjecture counter. It counts how many steps does it take to reach 1.")
    num = input("Enter a number")
    steps = collatz_steps(int(num), 0)
    print("It took " + str(steps) + " steps")

if __name__ == "__main__":
    main()