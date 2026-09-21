# Grid - 8-puzzle

print("Hello! I am your smart-search helper")
print("Give me a Puzzle and I will find the shortest answer with A*!")

# ===============================
# A* Search Algo 
# ==============================

def astar(start, goal, get_neighbours, guess):
    # the to list. Each node is [f, g, place, path_so_far]
    frontier = [[guess(start), 0, start, [start]]]
    visited = []        # places we already explored
    explored_count = 0      #How many times we explored.

    while len(frontier) > 0:
        best = 0

        for i in range(len(frontier)):
            if frontier[i][0] < frontier[best][0]:
                best = i

        note = frontier.pop(best)
        f, g, place, path = note
        if place in visited:
            continue

        visited.append(place)
        explored_count += 1

        # 3 ) did we reach the goal ? 
        if place == goal:
            return path, explored_count

        # 4) add each neighbour
        for nxt in get_neighbours(place):
            if nxt not in visited:
                new_g = g + 1
                new_f = new_g + guess(nxt)

                frontier.append([new_f, new_g, nxt, path + [nxt]])

    return None, explored_count

print("A* is ready.")

# =======================================
# PART A - ROBOT On Grid

grid = [
    "............",
    "....####....",
    "S..........G",
    "....###.....",
    "............",
]

# Find S and G in the grid

def find(letter):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == letter:
                return(r,c)

start = find("S")
goal = find("G")

rows, cols = len(grid), len(grid[0])

print("Start S is at ", start)
print("Goal G is at ", goal)
print()

for line in grid:
    print(" " + " ".join(line))

# =================
# GRID NEIGHBOURS
# =================

def grid_neighbour(box):
    r, c = box
    out = []

    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] != "#":
                out.append((nr, nc))
    return out

print(
    "From the start",
    start,
    "the robot can step to:",
    grid_neighbour(start)
)

# ======================
# Grid Heuristics
# ======================

# Guess 1 : No Hint
def grid_zero(box):
    return 0


# Guess 2 : 
def grid_manhattan(box):
    r, c = box

    return abs(r - goal[0]) + abs(c - goal[1])

print(
    "Manhattan guess from the start:",
    grid_manhattan(start)
)

# ==================================
# SOLVE GRID USING BOTH HEURISTICS
# ===================================
path_zero, explored_zero = astar(start, goal, grid_neighbour, grid_zero)
path_manh, explored_manh = astar(start, goal, grid_neighbour, grid_manhattan)


print("Guess              Path length            Boxes explored")
print("-" * 46)

print("Zero (no hint)", len(path_zero) - 1, "steps       ", explored_zero)

print("Manhattan       ", len(path_manh)-1, "steps    ", explored_manh)

def show_grid_path(path):
    path_set = set(path)

    for r in range(rows):
        line = ""

        for c in range(cols):
            if (r,c) == start: 
                line += " S "
            elif (r, c) == goal:
                line += " G "
            elif (r, c) in path_set:
                line += " * "

            else:
                line += " " + grid[r][c] + " "
        print(line)

print("The robot's path:")
print()

show_grid_path(path_manh)

goal_state = "123456780"
start_state = "123450678"


# Display the puzzle
def show_puzzle(state):

    for r in range(3):

        row = state[r * 3 : r * 3 + 3]

        row = row.replace("0", "_")

        print("   " + "  ".join(row))


print("Start:")
show_puzzle(start_state)

print()

print("Goal:")
show_puzzle(goal_state)


# =========================================================
# 8-PUZZLE NEIGHBOURS
# =========================================================

def puzzle_neighbours(state):

    out = []

    # Find the empty space
    zero = state.index("0")

    # Convert index into row and column
    r, c = zero // 3, zero % 3

    # Up, Down, Left, Right
    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]:

        nr, nc = r + dr, c + dc

        # Stay inside the 3x3 puzzle
        if 0 <= nr < 3 and 0 <= nc < 3:

            new_zero = nr * 3 + nc

            tiles = list(state)

            # Swap empty space with neighbouring tile
            tiles[zero], tiles[new_zero] = (
                tiles[new_zero],
                tiles[zero]
            )

            out.append("".join(tiles))

    return out


print(
    "From the start, we can reach these arrangements:"
)

for s in puzzle_neighbours(start_state):
    print("  ", s)


# =========================================================
# 8-PUZZLE HEURISTICS
# =========================================================

# Guess 1: No hint
def puzzle_zero(state):
    return 0


# Guess 2: Wrong tiles
def puzzle_wrong_tiles(state):

    count = 0

    for i in range(9):

        if state[i] != "0" and state[i] != goal_state[i]:
            count = count + 1

    return count


print(
    "Wrong tiles in the start:",
    puzzle_wrong_tiles(start_state)
)


# =========================================================
# SOLVE 8-PUZZLE USING BOTH HEURISTICS
# =========================================================

ans_zero, count_zero = astar(
    start_state,
    goal_state,
    puzzle_neighbours,
    puzzle_zero
)

ans_smart, count_smart = astar(
    start_state,
    goal_state,
    puzzle_neighbours,
    puzzle_wrong_tiles
)


print(
    "Guess            Moves to solve    Arrangements explored"
)

print("-" * 56)

print(
    "Zero (no hint)  ",
    len(ans_zero) - 1,
    "moves          ",
    count_zero
)

print(
    "Wrong-tiles     ",
    len(ans_smart) - 1,
    "moves          ",
    count_smart
)

print()

print(
    "Same number of moves. "
    "But the smart guess explores FAR fewer arrangements! ⭐"
)


# =========================================================
# SHOW PUZZLE SOLUTION STEP BY STEP
# =========================================================

print("Solving the puzzle, one slide at a time:")
print()

for step, state in enumerate(ans_smart):

    print("Move", step, ":")

    show_puzzle(state)

    print()