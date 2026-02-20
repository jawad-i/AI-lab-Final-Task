from collections import deque
import copy

N = 3

# Move offsets: Left, Right, Up, Down
row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]


class p8_board:
    def __init__(self, board, x, y, depth, parent=None):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.parent = parent


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def is_goal(board):
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    return goal == board


def bfs_solve(start_board, x, y):
    queue = deque()
    start_tuple = tuple(map(tuple, start_board))
    visited = {start_tuple}

    queue.append(p8_board(start_board, x, y, 0))

    while queue:
        current = queue.popleft()

        if is_goal(current.board):
            print("✅ Solution found!\n")
            print_solution(current)
            return

        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]

            if is_valid(new_x, new_y):
                new_board = copy.deepcopy(current.board)

                # Swap blank with neighbor
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))

                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(
                        p8_board(new_board, new_x, new_y,
                                 current.depth + 1, current)
                    )

    print("❌ No solution found")


def print_solution(node):
    path = []
    current = node

    while current is not None:
        path.append(current)
        current = current.parent

    path.reverse()

    print(f"Solution found in {len(path) - 1} moves:\n")

    for i, step in enumerate(path):
        print(f"--- Step {i} ---")
        for r in step.board:
            print(r)
        print()


# --- Run Example ---
if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 5],
             [7, 8, 6]]

    # Find position of 0
    x, y = -1, -1
    for r in range(3):
        for c in range(3):
            if start[r][c] == 0:
                x, y = r, c
                break

    print("Solving with BFS...\n")
    bfs_solve(start, x, y)