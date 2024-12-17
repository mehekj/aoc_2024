def valid(row, col, grid):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def dfs(grid, row, col, n, ends):
    if not valid(row, col, grid):
        return

    if grid[row][col] != n:
        return

    if n == 9:
        ends.append((row, col))
        return

    dfs(grid, row + 1, col, n + 1, ends)
    dfs(grid, row - 1, col, n + 1, ends)
    dfs(grid, row, col + 1, n + 1, ends)
    dfs(grid, row, col - 1, n + 1, ends)


def main():
    grid = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            grid.append([int(i) for i in line.strip()])

    total = 0
    for row, digits in enumerate(grid):
        for col, digit in enumerate(digits):
            if digit == 0:
                ends = []
                dfs(grid, row, col, 0, ends)
                total += len(list(set(ends)))

    print(total)


main()
