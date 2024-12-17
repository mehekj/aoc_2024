def valid(row, col, grid):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def dfs(grid, row, col, n):
    if not valid(row, col, grid):
        return 0

    if grid[row][col] != n:
        return 0

    if n == 9:
        return 1

    return dfs(grid, row + 1, col, n + 1) \
        + dfs(grid, row - 1, col, n + 1) \
        + dfs(grid, row, col + 1, n + 1) \
        + dfs(grid, row, col - 1, n + 1)


def main():
    grid = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            grid.append([int(i) for i in line.strip()])

    total = 0
    for row, digits in enumerate(grid):
        for col, digit in enumerate(digits):
            if digit == 0:
                total += dfs(grid, row, col, 0)

    print(total)


main()
