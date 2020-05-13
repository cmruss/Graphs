import sys
sys.path.insert(0, '../graph')
from graph import Graph
from util import Queue, Deque, Stack

# How to solve any graph problem
# 1. Translate the problem into graph terminology

def earliest_ancestor(ancestors, starting_node):
    """Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
    """
    # create a queue 
    q = Queue()
    # add the stating node to the queue
    q.enqueue([starting_node])
    # create a visited set to 
    # keep track of where we've been
    visited = set()
    # until there's no nodes added to the queue
    paths = list()
    while q.size() > 0:
        # grab the first path in the queue
        path = q.dequeue()
        # grab the last node in the path
        node = path[-1]
        print(f"current: {paths}")
        print(f"node from queue: {node}")
        # if we haven't seen it before
        if node not in visited:
            # print(node)
            # add it to the visited set
            visited.add(node)
            # loop through the list of tuples passed in
            for next_node in ancestors:
                print(f"next_node tuple: {next_node}")
                if node == next_node[1]:
                    print(f"match")
                    # copy the path
                    next_path = list(path)
                    # add the next node to the end of the path
                    next_path.append(next_node[0])
                    # add the path to the queue
                    q.enqueue(next_path)
                    # add the path to paths
                    paths.append(next_path)
    # when the size reaches 0
    if node == starting_node:
        # per the spec
        return -1
    # if there are multiple paths
    elif len(paths) > 1:
        # grab the last path
        last_path = paths[-1]
        print(last_path)
        # compare it to the other paths
        for path in paths:
            print(path)
            # if any path is as long as the last and it's final node is less
            if len(path) == len(last_path) and path[-1] < last_path[-1]:
                # make it the node
                node = path[-1]
                print(node)
        return node
    else: # return the furthest ancestor
        # print(node)
        return node

# ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# # 2. Build the graph

# # sets the earliest_ancestor method as an attribute on the Graph class
# setattr(Graph, "earliest_ancestor", earliest_ancestor)

# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     for node in ancestors:
#         # print(node)
#         # add parent to graph
#         graph.add_vertex(node[0])
#         # add child to graph
#         graph.add_vertex(node[1])
#     # had to have seperate loops while adding edges
#     # else half the edges aren't added 
#     for node in ancestors:
#         graph.add_edge(node[1], node[0])
#     print(graph.vertices)

# # 3. Traverse it

# print(graph.earliest_ancestor(ancestors, 1), 10)
# print(graph.earliest_ancestor(ancestors, 2), -1)
# print(graph.earliest_ancestor(ancestors, 3), 10)
# print(graph.earliest_ancestor(ancestors, 4), -1)
# print(graph.earliest_ancestor(ancestors, 5), 4)
# print(graph.earliest_ancestor(ancestors, 6), 10)
# print(graph.earliest_ancestor(ancestors, 7), 4)
# print(graph.earliest_ancestor(ancestors, 8), 4) 
# print(graph.earliest_ancestor(ancestors, 9), 4) 
# print(graph.earliest_ancestor(ancestors, 10), -1)
# print(graph.earliest_ancestor(ancestors, 11), -1)
