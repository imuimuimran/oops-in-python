class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rectangle1 = Rectangle()
rectangle1.set_dimensions(3, 4)
print("The height and width of rectangle are: ", rectangle1.width,"and", rectangle1.height)
print("The total area of the rectangle is: ", rectangle1.area())
print("The total perimeter of the rectangle is: ", rectangle1.perimeter())