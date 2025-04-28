class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

# point1 = Point()
# point1.draw()
#
# point2 = Point()
# point2.x = 10
# point2.move()
# print(point2.x)

point = Point(15,50)
print(point.x)