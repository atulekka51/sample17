def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Set of nodes to be evaluated
    closed_set = set()  # Set of nodes already evaluated
    
    g = {}  # Dictionary to store the cost from start_node to a node
    parents = {}  # Dictionary to store the parent of each node for path reconstruction
    
    g[start_node] = 0
    parents[start_node] = start_node
    
    while len(open_set) > 0:
        n = None
        
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        
        open_set.remove(n)
        closed_set.add(n)
        
        neighbors = get_neighbors(n)
        if neighbors:
            for (m, weight) in neighbors:
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

    print("Path does not exist!")
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist.get(n, float('inf'))  # Return a large value if the node is not found in heuristic

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Test the function
aStarAlgo('A', 'G')

                
        