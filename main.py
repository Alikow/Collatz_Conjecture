# The Collatz Conjecture
def three_one_problem():
    num = int(input("Type a number: "))
    while True:
        if num % 2 != 0:
            num = ((3 * num) + 1)
            print(int(num))
        if num % 2 == 0:
            num = num / 2
            print(int(num))
        if num == 1:
            break


three_one_problem()
