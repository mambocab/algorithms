from collections import deque

def wiki(xs):
    current_max_len = 0
    m = [0 for x in xs]
    preds = [0 for x in xs]

    longest = 0

    for i, x in enumerate(xs):
        lo, hi = 1, current_max_len
        mid = (lo + hi) // 2
        if xs[m[mid]] < x:
            lo = mid + 1
        else:
            hi = mid - 1

        longest, preds[i], m[lo] = (lo if lo > longest else longest,
                                    m[lo - 1],
                                    i)

    rv = deque([xs[m[longest]]])
    for x in reversed(xs):
        if rv[0] > x:
            rv.appendleft(x)

    return rv

if __name__ == '__main__':
    output = wiki([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,
                    13, 3, 11, 4, 5, 6, 7, 15, 8, 9])
    expected = [0, 2, 3, 4, 5, 6, 7, 8, 9]
    print(output)
    assert len(output) == len(expected)
