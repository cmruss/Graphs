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

"""
DAY 2
"""
def f(n):
    """
    not a super useful function
    easily loops infinitely
    """
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

cache = {}

def get_neighbors(word):
    neighbors = []

    string_word = list(word) # ["w", "o", "r", "d"]

    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[-1] = letter
            w = "".join(temp_word)

            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

"""
DAY 3
"""

islands = [[0,1,0,1,0],
            [1,1,0,1,1],
            [0,0,1,0,0],
            [1,0,1,0,0],
            [1,1,0,0,0]]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def island_counter(matrix):
    """
    Count the number of 1s in the matrix 
    that are adjacent as a single island 
    """
    # create a visited data structure
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    count = 0
    # walk through all nodes, elemments in the input matrix
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            # If it's not visited:
            if not visited[x][y]:
                # if it's a 1:
                if matrix[x][y] == 1:
                    # do a traversal and mark as visited
                    visited = dft(x, y, matrix, visited)
                    # increment island counter
                    count += 1
                else: # it's a 0
                    visited[x][y] = True
    return count

def  dft(x,y, matrix, visited):
    s = Stack()
    s.push((x,y))
    while s.size() > 0:
        v = s.pop()
        x,y = v
        if not visited[x][y]:
            visited[x][y] = True
            for neighbor in get_neighbors(x,y, matrix):
                s.push(neighbor)
    return visited

def get_neighbors(x,y, matrix):
    neighbors = []
    # look north
    if x > 0 and matrix[x-1][y] == 1:
        neighbors.append((x-1, y))
    # look south
    if x < len(matrix) -1 and matrix[x+1][y] == 1:
        neighbors.append((x+1, y))
    # look west
    if y > 0 and matrix[x][y-1] == 1:
        neighbors.append((x, y-1))
    # look east
    if y < len(matrix[0]) - 1 and matrix[x][y+1] == 1:
        neighbors.append((x,y+1))
    return neighbors

print(island_counter(islands))

"""
Generating random data
----------------------
       0 1 2 3 
    0  - 0 0 0
    1  - - 2 3
    2  - - - 6
    3  - - - -
"""
# if you have a deck of cards, 
# how to choose 10 at random?

def populate_graph(self, num_users, avg_friendships):
    # reset graph
    self.last_id = 0
    self.users = {} # nodes
    self.friendships = {} # edges
    # generate the users
    for i in range(0, num_users):
        self.add_user(f"User {i}")
    # generate all friendship combinations
    # but not duplicate combinations
    possible_friendships = []
    for user_id in self.users:
        for friend_id in range(user_id + 1, self.last_id + 1):
            possible_friendships.append((user_id, friend_id))
    # shuffle them
    random.shuffle(possible_friendships)
    # choose the first n out of the list
    if i in range(num_users * avg_friendships // 2):
        # set up those friendships
        friendship = possible_friendships[i]
        self.add_friendship(friendship[0], friendship[1])
        