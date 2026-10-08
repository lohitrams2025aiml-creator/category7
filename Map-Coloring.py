def color_map(graph, colors, result, region):
    if region == len(graph):
        return True
    for color in colors:
        safe = True
        for neighbor in graph[region]:
            if result[neighbor] == color:
                safe = False
                break
        if safe:
            result[region] = color
            if color_map(graph, colors, result, region + 1):
                return True
            result[region] = None
    return False
graph = [
    [1, 2],       
    [0, 2, 3],    
    [0, 1, 3],    
    [1, 2]        
]
colors = ["Red", "Green", "Blue"]
result = [None] * 4
if color_map(graph, colors, result, 0):
    for i in range(4):
        print(chr(65 + i), "->", result[i])
else:
    print("No solution")
