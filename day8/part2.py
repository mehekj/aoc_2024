def valid(row, col, w, h):
    return row >= 0 and row < h and col >= 0 and col < w


def main():
    antennas = {}
    antinodes = []
    with open("./input.txt", "r") as f:
        for row, line in enumerate(f.readlines()):
            antinodes.append([])
            for col, char in enumerate(line.strip()):
                if char != '.':
                    antinodes[row].append(1)
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((row, col))
                else:
                    antinodes[row].append(0)

    h = len(antinodes)
    w = len(antinodes[0])
    for char, positions in antennas.items():
        for i, pos1 in enumerate(positions):
            for _, pos2 in enumerate(positions[i + 1:]):

                div, temp = dir = (pos2[0] - pos1[0], pos2[1] - pos1[1])
                while temp:
                    div, temp = temp, div % temp
                dir = (dir[0] // div, dir[1] // div)

                next = (pos2[0] + dir[0], pos2[1] + dir[1])
                while valid(next[0], next[1], w, h):
                    antinodes[next[0]][next[1]] = 1
                    next = (next[0] + dir[0], next[1] + dir[1])

                next = (pos2[0] - dir[0], pos2[1] - dir[1])
                while valid(next[0], next[1], w, h):
                    antinodes[next[0]][next[1]] = 1
                    next = (next[0] - dir[0], next[1] - dir[1])

    print(sum([sum(row) for row in antinodes]))


main()
