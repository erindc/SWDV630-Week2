class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def computeArea(self):
        return self.length * self.width


def main():
    rectangle = Rectangle(13, 12)
    print('The area is ', rectangle.computeArea())
    
main()