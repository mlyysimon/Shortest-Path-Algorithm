# node and distance values for graph listed here
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
  # graph being the nodes and distances table
  # start being the node to begin pathing
  # target used for displaying a specific end node in output

    unvisited = list(graph) # track which nodes still need to be determined
    distances = {node: 0 if node == start else float('inf') for node in graph} # track distance values found
    paths = {node: [] for node in graph} # track shortest path for each node
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get) # unvisited node with the smallest known distance from start
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]: # if new distance to neighbor is smaller than known distance
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:  # if a path exists and is complete but is not the shortest path, replace with current shorter path
                    paths[node] = paths[current][:]
                else: # if no path exists, create a path with current path
                    paths[node].extend(paths[current])
                paths[node].append(node) # append the current node
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            # shortest path to start node is the start node, self explanatory
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A')
