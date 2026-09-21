

print("I am your Treasure Hunt Robot.")
print("Welcome! Let's find Treasure.")

map_rooms = {
    "A" : ["B", "C"],
    "B" : ["D"],
    "C" : ["D"],
    "D" : ["G"],
    "G" : []
}

print("Our Map")
print("      A(Start)")
print("     /   \\     ")
print("    B     C   ")
print("     \\   /")
print("       D    ")
print("       \\    ")
print("        G (Treasure)")
print("Doors for each Room : ", map_rooms)

def bfs(start, goal):
    todo = [start]
    visited = []
    order = []

    while todo:
        room = todo.pop(0)

        if room in visited:
            continue
        visited.append(room)
        order.append(room)
        # print(visited)
        if room == goal:
            return order
        for nxt in map_rooms[room]:
            todo.append(nxt)

    return(order)

bfs_order = bfs("A", "G")
print("BFS checked the rooms to find the treasure : ", bfs_order)
print("Number of rooms visited : ", len(bfs_order))

def dfs(start, goal):
    todo = [start]
    visited = []
    order = []

    while todo:
        room = todo.pop()

        if room in visited:
            continue
        visited.append(room)
        order.append(room)

        if room == goal:
            return order
        for nxt in map_rooms[room]:
            todo.append(nxt)

    return(order)

dfs_order = dfs("A", "G")
print("DFS checked the rooms to find the treasure : ", dfs_order)
print("Number of rooms visited : ", len(dfs_order))

door_cost = {
    ("A", "B") : 1, 
    ("B", "D") : 1,
    ("A", "C") : 5, 
    ("C", "D") : 1,
    ("D", "G") : 1
}

def path_cost(path): 
    total = 0
    for i in range(len(path) - 1):
        door = (path[i], path[i+1])
        total += door_cost[door]

    return total

path1 = ["A", "B", "D", "G"]
path2 = ["A", "C", "D", "G"]

cost1 = path_cost(path1)
cost2 = path_cost(path2)

print("\nPath1 (A -> B -> D -> G) : ",cost1)
print("Path1 (A -> C -> D -> G) : ",cost2)

if(cost1 < cost2):
    best_path = path1
    best_cost = cost1
else:
    best_path = path2
    best_cost = cost2

print("Best Path : ", best_path, ", Cost of Path : ", best_cost)

print("\n", "-" *40)
print("RESULT")
print("-" * 40)

# print("BFS Traversal : ", bfs_order)
print("DFS Traversal : ", dfs_order)
print("Cheapest Cost : ", best_path)
print("Cost : ", best_path)

print("-" * 40)

print("\n What we learned : ")
print("- BFS checks the nearest rooms first.")
print("- DFS explores one path deeply first.")
print("- Uniform Cost Search checks the path with the lowest cost first.")


# Activity

print ("\n --------- Activity ------- ")
door_cost[("A", "B")] = 4
door_cost[("A", "C")] = 1
door_cost[("B", "D")] = 3
door_cost[("C", "D")] = 2
door_cost[("D", "G")] = 2

cost1 = path_cost(path1)
cost2 = path_cost(path2)

print("\nPath1 (A -> B -> D -> G) : ",cost1)
print("Path2 (A -> C -> D -> G) : ",cost2)

if(cost1 < cost2):
    best_path = path1
    best_cost = cost1
else:
    best_path = path2
    best_cost = cost2

print("Best Path : ", best_path, ", Cost of Path : ", best_cost)