class Rectangle:
    def __init__(self, length,width):
        self.length = int(length)
        self.width = int(width)

    def __iter__(self):

        yield {'length': self.length}
        yield {'width': self.width}


rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)