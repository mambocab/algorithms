from random import uniform

from rumble import rumble

epsilon = .000001
init_guess = 10

def close(a, b):
    return (a - epsilon) < b < (b + epsilon)

@rumble.contender
def newton(n):
    guess = init_guess
    guess_2 = guess ** 2

    while not close(guess_2, n):
        guess = guess - ((guess_2 - n) / (2 * guess))
        guess_2 = guess ** 2

    return guess


@rumble.contender
def binary(n):
    bottom, top = 0, n
    guess = uniform(bottom, top)
    guess_2 = guess ** 2

    while not close(guess_2, n):
        if guess_2 < n:
            bottom = guess
        else:
            top = guess
        guess_2 = guess ** 2

    return guess


if __name__ == '__main__':
    for n in [400, 20000]:
        rumble.arguments(n)
    rumble.run()
