#!/usr/bin/python3
""" N queens """
import sys

def queens(q, i=0, a=set(), b=set(), c=set()):
    """ Find possible positions using backtracking """
    if i < q:
        for j in range(q):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(q, i+1, a.union({j}), b.union({i+j}), c.union({i-j}))
    else:
        yield tuple(a)

def solve(q):
    """ Solve and print all solutions """
    solutions = list(queens(q))
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        q = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if q < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(q)
