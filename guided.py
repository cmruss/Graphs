class LinkedNode:
    def __init(self, value):
        self.value = value
        self.next = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edge = [] # adjacency list

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set() # set of edges

    def add_edge(self, v1, v2):
        """
        Add edge from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """
        Breadth-firts traversal
        """
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)
g.add_edge(99, 3)
g.add_edge(3, 99)
g.add_edge(99, 3490)

# print(g.get_neighbors(99))
# print(g.get_neighbors(3))
g.bft(99)

def f(n):
    if n == 0:
        return 3490
    return f(n-1)

# print(f(10))
# print(f(10000))

def find_ladders(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in self.get_neighbors(v):
                path_copy = list(past)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
import string
with open('words.txt') as f:
    words = f.read().split()

word_set = set()

for w in words:
    word_set.add(w.lower())

letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []

    string_word = list(word) # ["w", "o", "r", "d"]

    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[-1] = letter
            w = "".join(temp_word)

            if w in word_set:
                neighbors.append(w)

    return neighbors