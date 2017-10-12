import numpy as np

"""
A dynamic programming solution for the World Series problem.
Two players/teams play as many games as needed until one of them wins
n games. So 2n - 1 games at most are played.
"""


def world_series(n, i, j):
    """
    The function takes as input a given state (i, j): i games have been won
    so far by the first player and j games have been won by the other player.

    The function returns the probability that the first player wins the
    competition (reaches n games) given the current state (i, j).

    :param n: int | number of games to win to be declared champion
    :param i: int | number of games won so far by the first player
    :param j: int | number of games won so far by the second player
    :return: float | probability that the first player wins the competition
    """

    # Sanity check
    if i >= n or j >= n:
        raise ValueError("i and j must be strictly smaller than n")

    # Create matrix of size n^2
    # M[i][j] represents the probability to be in the state (i, j), i.e. that
    # i + j games have been played i of which were won by the first player
    # and the other j the second player
    M = [[1]*(n - j + 1) for _ in range(n - i + 1)]

    # Fill first column of M
    for i_ in range(1, n - i + 1):
        M[i_][0] = M[i_ - 1][0] * 0.5

    # Fill first row of M
    for j_ in range(1, n - j + 1):
        M[0][j_] = M[0][j_ - 1] * 0.5

    # Fill other values of M by filling row by row
    for i_ in range(1, n - i + 1):
        for j_ in range(1, n - j + 1):
            M[i_][j_] = 0.5 * (M[i_][j_ - 1] + M[i_ - 1][j_])

    # Correct last value
    M[n - i][n - j] = 0

    # Cast M to numpy array: easier to slice
    M = np.array(M)

    # Returns the proba that first player wins
    return np.sum(M[n - i, 1: -1])

if __name__ == "__main__":
    print(world_series(4, 3, 1))
    #print(world_series(5, 4, 2))
    print(world_series(8, 4, 6))