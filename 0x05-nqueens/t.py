#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


sols = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""


def get_inp():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_att(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def grp_exists(grp):
    """Checks if a group exists in the list of solutions.

    Args:
        grp (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global sols
    for sol in sols:
        i = 0
        for sol_pos in sol:
            for grp_pos in grp:
                if sol_pos[0] == grp_pos[0] and sol_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_sol(row, grp):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        grp (list of lists of integers): The group of valid positions.
    """
    global sols
    global n
    if row == n:
        tmp = grp.copy()
        if not grp_exists(tmp):
            sols.append(tmp)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(grp), grp)
            used_pos = map(lambda x: is_att(x[0], x[1]), matches)
            grp.append(pos[a].copy())
            if not any(used_pos):
                build_sol(row + 1, grp)
            grp.pop(len(grp) - 1)


def get_sols():
    """Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    grp = []
    build_sol(a, grp)


n = get_inp()
get_sols()
for sol in sols:
    print(sol)

