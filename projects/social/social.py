import random
import sys
sys.path.insert(0, '../graph')
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # generate all friendship combinations
        possible_friendships = []
        for user_id in self.users:
            # but not duplicate combinations
            for friend_id in range(user_id +1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # shuffle them
        random.shuffle(possible_friendships)
        # Create friendships
        for i in range(0, num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            # print(f"friendship {friendship}")
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
    
        q = Queue() # going to use bredth first here
        # add user_id as a list to the queue
        q.enqueue([user_id]) # this will become the path
        
        while q.size() > 0: # loop the queue
            path = q.dequeue()  
            # print(path)
            cur_id = path[-1] # pull the last element of the path as the current id

            if cur_id not in visited: # check if the id has been added
                visited[cur_id] = path # add it if not

                # loop through the friends of the id from the queue
                for friend_id in self.friendships[cur_id]: 
                    if friend_id not in visited: # if the friends id has not been visited
                        next_path = list(path) # copy the path
                        next_path.append((friend_id)) # add the friends id to the path
                        q.enqueue(next_path) # add the updated path to the queue

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(f"{len(list(connections)) / 1000 * 100}% of users are in this users extended network")
    friends = list()
    for i in connections:
        friends.append(len(connections[i]))
    print(f"The average degree of seperation is {sum(friends) // len(friends)}")