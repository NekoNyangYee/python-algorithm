graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

def dfs(graph, start_node, visited = []):
    visited.append(start_node)
    for node in graph[start_node]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

print(dfs(graph, 1))
