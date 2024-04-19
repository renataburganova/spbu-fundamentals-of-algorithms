from time import perf_counter
from collections import deque


class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def solve(maze: Maze) -> None:
    path = ""  # solution as a string made of "L", "R", "U", "D"
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    start = (0, maze.start_j)

    queue = deque([(start, "")])
    visited = set([start])

    while queue:
        (row, col), path = queue.popleft()
        if maze.list_view[row][col] == 'X':
            print(f"Found: {path}")
            maze.print(path)
            return
        for direction, (dx, dy) in directions.items():
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < len(maze.list_view) and
                    0 <= new_col < len(maze.list_view[0]) and
                    maze.list_view[new_row][new_col] != '#' and
                    (new_row, new_col) not in visited):
                queue.append(((new_row, new_col), path + direction))
                visited.add((new_row, new_col))

    print(f"Found: {path}")
    maze.print(path)


def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j


if __name__ == "__main__":
    maze = Maze.from_file("C:/IT/algorithms/spbu-fundamentals-of-algorithms/practicum_3/homework/basic/maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")
