import random
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
assignment = {
    'A': random.choice(colors),
    'B': random.choice(colors),
    'C': random.choice(colors),
    'D': random.choice(colors)
}
def conflicts(assignment):
    count = 0
    for node in graph:
        for neighbor in graph[node]:
            if assignment[node] == assignment[neighbor]:
                count += 1
    return count // 2
while conflicts(assignment) != 0:
    node = random.choice(list(graph.keys()))
    best_color = assignment[node]
    best_conflicts = conflicts(assignment)
    for color in colors:
        assignment[node] = color
        current = conflicts(assignment)
        if current < best_conflicts:
            best_conflicts = current
            best_color = color
    assignment[node] = best_color
print("Solution:")
for node in assignment:
    print(node, "->", assignment[node])
print("Conflicts:", conflicts(assignment))
