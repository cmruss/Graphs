"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return IndexError("Vertex does not exist in Graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack() # depth first because FILO order
        s.push(starting_vertex) # add the starting point
        visited = set() # keep track of what we've traversed

        while s.size() > 0: # while we're still pushing to the stack
            v = s.pop() # take the last vertex added
            if v not in visited: # if we've already traversed it, let it go
                print(v)
                visited.add(v) # add the vertex to visited
                for next_v in self.get_neighbors(v): # call get neighbors to loop through
                    s.push(next_v) # and add connected vertices to the stack
   
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        visited = set()

        def helper(vertex): # nested reecursive function takes a vertex
            s.push(vertex) # adds it to the stack 
            v = s.pop() # pulls the last vertex added from the stack
            if v not in visited: # checks if we've traversed it already
                print(v)
                visited.add(v) # if not, add it to the set in parents scope
                for next_v in self.get_neighbors(v): # loop through the connected vertices
                    helper(next_v) # and call the functon on them 

        helper(starting_vertex) # call the recursive function on the first vertex
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # print(path)
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # print(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
            # Mark it as visited...
            visited.add(v)
            # Then add A PATH TO its neighbors to the back of the queue
            for next_v in self.get_neighbors(v):
                # print(f"next vertex: {next_v}")
                # _COPY_ THE PATH
                next_path = list(path)
                # APPEND THE NEIGHOR TO THE BACK
                next_path.append(next_v)
                q.enqueue(next_path)
                
                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        
        while s.size() > 0:
            path = s.pop()
            # print(path)
            v = path[-1]
            
            if v not in visited:
                # print(v)
                if v == destination_vertex:
                    return path
            visited.add(v)

            for next_v in self.get_neighbors(v):
                next_path = list(path)
                next_path.append(next_v)
                s.push(next_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        the_path = []

        def helper(vertex):
            path = s.pop()
            v = path[-1]
            # print(f"v:{v}")
            if v not in visited:
                # base case, we find it
                if v == destination_vertex:
                    # print(f"path {path}")
                    the_path.extend(path)
                visited.add(v)
                for next_v in self.get_neighbors(v):
                    next_path = list(path)
                    next_path.append(next_v)
                    # print(f"next path: {next_path}")
                    s.push(next_path)
                    helper(next_v)

        helper(starting_vertex)
        # if we don't find it
        if the_path == []:
            return None        
        return the_path

    def beejs_dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):

        if visited is Nonoe:
            visited = set()

        if path is None:
            path = []
        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                new_path = self.beejs_dfs_recursive(child_vertex, destination_vertex, visited, path)

            if new_path:
                return new_path

        return None
        
    def beejs_earliest_ancestor(self, ancestors, starting_vertex):
        for pair in ancestors:
            self.add_vertex(pair[0])
            self.add_vertex(pair[1])
            self.add_edge(pair[1], pair[0])

        q = Queue()
        q.enqueue([starting_vertex])
        max_path_len = 1
        earliest_ancestor = -1

        while q.size > 0:
            path = q.dequeue()
            v = path[-1]
            if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
                earliest_ancestor = v
                max_path_len = len(path)

            for neighbor in self.vertices[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
        return earliest_ancestor
                

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))