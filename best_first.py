import heapq

# Goal state
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal_state.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# Generate neighbors
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    x, y = divmod(index, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx * 3 + ny
            new_state = list(state)

            # Swap blank
            new_state[index], new_state[new_index] = \
                new_state[new_index], new_state[index]

            neighbors.append(tuple(new_state))

    return neighbors


# Best-First Search
def best_first_search(start_state):
    priority_queue = []
    visited = set()

    heapq.heappush(priority_queue,
                   (manhattan_distance(start_state), start_state))

    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)

        if current_state == goal_state:
            print("✅ Goal State Reached!")
            return True

        if current_state in visited:
            continue

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (manhattan_distance(neighbor), neighbor))

    print("❌ No solution found")
    return False


# Initial state
initial_state = (1, 2, 3,
                 4, 0, 5,
                 6, 7, 8)

best_first_search(initial_state)