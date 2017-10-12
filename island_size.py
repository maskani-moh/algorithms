# Exercise 695 of Leetcode
def maxAreaOfIsland(grid):
    seen = set()

    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        return (1 + area(r + 1, c) + area(r - 1, c) +
                area(r, c - 1) + area(r, c + 1))

    return max(area(r, c)
               for r in range(len(grid))
               for c in range(len(grid[0])))


def maxAreaOfIsland2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Size of the matrix grid
    m, n = len(grid), len(grid[0])

    # Def custom class
    class Node:
        def __init__(self, i, j):
            self.value = grid[i][j]
            self.visited = False
            # Corners of the grid
            if i == 0 and j == 0:
                self.neighbors = [Node(0, 1), Node(1, 0)]
            elif i == m - 1 and j == n - 1:
                self.neighbors = [Node(m - 1, n - 2), Node(m - 2, n - 1)]
            elif i == 0:
                self.neighbors = [Node(0, j - 1), Node(0, j + 1),
                                  Node(1, j + 1)]
            elif j == 0:
                self.neighbors = [Node(i - 1, 0), Node(i, 1),
                                  Node(i + 1, 0)]
            elif i == m - 1:
                self.neighbors = [Node(m - 2, j), Node(m - 1, j + 1)]
            elif j == n - 1:
                self.neighbors = [Node(i, n - 2), Node(i - 1, n - 1),
                                  Node(i + 1, n - 1)]
            else:
                self.neighbors = [Node(i - 1, j), Node(i, j - 1),
                                  Node(i, j + 1), Node(i + 1, j + 1)]

    connected_compo = []

    def exploreNode(node):
        tmp = []
        if node.visited:
            return tmp
        node.visited = True
        if node.value == 0:
            return tmp
        tmp.append(node)
        for PosNeighbor in [n for n in node.neighbors if n.value == 1]:
            tmp.extend(exploreNode(PosNeighbor))
        return tmp

    for i in range(0, m):
        for j in range(0, n):
            node = Node(i, j)
            if node.visited:
                continue
            connected_compo.append(exploreNode(node))
            print(connected_compo)

    return max([len(c) for c in connected_compo])

if __name__ == "__main__":
    grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
    print(maxAreaOfIsland(grid))