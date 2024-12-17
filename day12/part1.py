def valid(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def calc_dims(grid, visited, row, col, dims):
    dims[0] += 1
    dims[1] += 4

    char = grid[row][col]
    visited[row][col] = 1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in dirs:
        r = row + dir[0]
        c = col + dir[1]

        if valid(grid, r, c) and grid[r][c] == char:
            dims[1] -= 1
            if not visited[r][c]:
                calc_dims(grid, visited, r, c, dims)


def main():
    grid = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            grid.append(line.strip())

    visited = [[0] * len(grid[0]) for row in grid]
    dims = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not visited[row][col]:
                dims.append([0, 0])
                calc_dims(grid, visited, row, col, dims[-1])

    total = 0
    for dim in dims:
        total += dim[0] * dim[1]

    print(total)


main()
