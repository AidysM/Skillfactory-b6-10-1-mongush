class Rectangle:
    def __init__(self, x=5, y=10, width=50, height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_str(self):
        return print(f"Rectangle ({self.x}, {self.y}, {self.width}, {self.height})")
