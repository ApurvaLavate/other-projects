#finding a shortest path
def find_shortest_path(graph, start, end):
    paths = [[start]]  

    while paths:
        path = paths.pop(0)  
        node = path[-1]      

        if node == end:
            return path  

        for neighbor in graph.get(node, []):
            if neighbor not in path:  
                new_path = path + [neighbor]
                paths.append(new_path)

    return None  
