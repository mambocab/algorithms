from itertools import product
from rumble import rumble


@rumble.contender
def recursive(n, collection):
    if not collection:
        return None

    mid = len(collection) // 2

    if n < collection[mid]:
        return recursive(n, collection[:mid])
    elif collection[mid] == n:
        return mid
    elif collection[mid] < n:
        return recursive(n, collection[mid+1:])

@rumble.contender
def iterative(n, collection):
    candidates = collection[:]

    while candidates:
        mid = len(candidates) // 2
        if n < candidates[mid]:
            candidates = candidates[:mid]
        elif candidates[mid] == n:
            return mid
        elif candidates[mid] < n:
            candidates = candidates[mid+1:]
    return None


if __name__ == '__main__':
    for t, n in product([tuple, list], [100, 1000, 10000]):
        xs = t(range(n))
        rumble.arguments(50, xs, _name=('len(' + t.__name__ + ') == ' + str(n)))
    rumble.run()
