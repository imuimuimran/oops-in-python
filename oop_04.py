class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
wid = int(input("Enter the width of he rectangle: "))
hei = int(input("Enter the height of he rectangle: "))
rectangle1 = Rectangle()
rectangle1.set_dimensions(wid,hei)
print("The height and width of rectangle are: ", rectangle1.width,"and", rectangle1.height)
print("The total area of the rectangle is: ", rectangle1.area())
print("The total perimeter of the rectangle is: ", rectangle1.perimeter())