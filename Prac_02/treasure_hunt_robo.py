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

# Activity

print ("\n --------- Activity ------- ")
door_cost[("A", "B")] = 4
door_cost[("A", "C")] = 1
door_cost[("B", "D")] = 3
door_cost[("C", "D")] = 2
door_cost[("D", "G")] = 2

cost1 = path_cost(path1)
cost2 = path_cost(path2)

print("\nNew Path1 (A -> B -> D -> G) : ",cost1)
print("New Path1 (A -> C -> D -> G) : ",cost2)

if(cost1 < cost2):
    best_path = path1
    best_cost = cost1
else:
    best_path = path2
    best_cost = cost2

print("Best Path : ", best_path, ", Cost of Path : ", best_cost)