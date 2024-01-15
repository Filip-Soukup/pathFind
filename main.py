import random

class Point:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Connection:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        self.size = 1

    def __str__(self):
        return f"{self.pointA} -- {self.pointB}"


class Branch:
    def __init__(self, history: list):
        self.history = history

    def nextGen(self):
        point = self.history[len(self.history)-1]
        next_dest = [x.pointA if x.pointB == point else x.pointB for x in connections if point in [x.pointA, x.pointB]]
        for x in next_dest:
            if x == end:
                complete.append(self)
            else:
                branches.append(Branch(self.history + [x]))
        branches.remove(self)

    def get_length(self):
        size = 0
        for x in range(len(self.history) - 1):
            point_a = self.history[x]
            point_b = self.history[x + 1]

            # Find the connection between point_a and point_b
            connection = next((y for y in connections if (y.pointA == point_a and y.pointB == point_b) or (
                        y.pointA == point_b and y.pointB == point_a)), None)

            if connection:
                size += connection.size

        return size

    def __str__(self):
        return f'Size: {self.get_length()} / '+' -> '.join(self.history)


points = [Point(chr(x)) for x in range(65, 90)]

connections = []
for x in range(len(points)):
    a = random.choice(points)
    b = random.choice(points)
    c = Connection(a, b)
    d = Connection(b, a)
    if a != b and c not in connections and d not in connections:
        connections.append(c)

# pathfind
start = Point("A")
end = Point("B")

branches = [Branch([start])]

complete = []

while len(branches) > 0:
    branches[0].nextGen()

finalPaths = sorted(complete, key=lambda obj1: sum(obj2.size for obj2 in obj1.obj2_list)) <-- NOT CORRECT

print(connections)

