import heapq
import copy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


def to_tuple(state):
    return tuple(tuple(row) for row in state)


def a_star(start):
    open_list = []
    closed_set = set()
    counter = 0  # Tie-breaker

    heapq.heappush(open_list,
                   (heuristic(start), counter, 0, start, []))

    while open_list:
        f, _, g, current, path = heapq.heappop(open_list)

        if current == GOAL_STATE:
            return path + [current]

        closed_set.add(to_tuple(current))

        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in closed_set:
                counter += 1
                heapq.heappush(
                    open_list,
                    (
                        g + 1 + heuristic(neighbor),
                        counter,
                        g + 1,
                        neighbor,
                        path + [current]
                    )
                )

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

solution = a_star(start_state)

if solution:
    print("✅ Solution Path:\n")
    for step in solution:
        print_state(step)
    print("Total Moves:", len(solution) - 1)
else:
    print("❌ No solution found")