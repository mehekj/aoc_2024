def valid(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def dfs(grid, word, row, col, dir):
    if word == "":
        return 1

    if valid(grid, row, col) and grid[row][col] == word[0]:
        return dfs(grid, word[1:], row + dir[0], col + dir[1], dir)

    else:
        return 0


def word_search(grid, word):
    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            total += dfs(grid, word, row, col, (0, 1)) \
                + dfs(grid, word, row, col, (0, -1)) \
                + dfs(grid, word, row, col, (1, 0)) \
                + dfs(grid, word, row, col, (-1, 0)) \
                + dfs(grid, word, row, col, (-1, -1)) \
                + dfs(grid, word, row, col, (-1, 1)) \
                + dfs(grid, word, row, col, (1, -1)) \
                + dfs(grid, word, row, col, (1, 1))

    return total


def main():
    grid = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            grid.append(line.strip())

    print(word_search(grid, "XMAS"))


main()
