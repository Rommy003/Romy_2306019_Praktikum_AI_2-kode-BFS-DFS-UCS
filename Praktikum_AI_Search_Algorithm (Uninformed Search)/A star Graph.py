from queue import PriorityQueue

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))  # (Priority, Node)
    explored = set()
    path = {}

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Goal node found!")
            route = reconstruct_path(path, start, goal)
            print("Route optimal:", route)
            return True

        explored.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                total_cost = cost + heuristic[neighbor]
                frontier.put((total_cost, neighbor))
                path[neighbor] = current_node

    print("Goal node not found!")
    return False

# Heuristic values
heuristic = {
    'A': 9, 'B': 4, 'C': 2, 'D': 5, 'E': 3, 'S': 7, 'G': 0
}

# Graph adjacency list with costs (using the second definition)
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'B': 1, 'D': 5},
    'B': {'D': 2}, # Added to make 'D' reachable from 'S'
    'D': {'G': 3} # Added to make 'G' reachable from 'S'
}

# Define start and goal nodes
start_node = 'S'
goal_node = 'G'


# Run A* Graph Search
a_star_graph_search(graph, start_node, goal_node, heuristic)
