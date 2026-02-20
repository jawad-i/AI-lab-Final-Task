import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_moves(state):
    moves = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def ao_star(start):
    counter = 0  # tie breaker
    open_list = [(heuristic(start), counter, start, [])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: (x[0], x[1]))
        cost, _, current, path = open_list.pop(0)

        if current == GOAL_STATE:
            return path + [current]

        visited.add(tuple(map(tuple, current)))

        for next_state in generate_moves(current):
            if tuple(map(tuple, next_state)) not in visited:
                g = len(path) + 1
                h = heuristic(next_state)
                counter += 1
                open_list.append((g + h, counter, next_state, path + [current]))

    return None

def print_state(state):
    for row in state:
        print(row)
    print()

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = ao_star(start_state)

if solution:
    print("Solution Path:")
    for step in solution:
        print_state(step)
    print("Total Moves:", len(solution) - 1)
else:
    print("No solution found")