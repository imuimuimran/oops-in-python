class Rectangle:
    def __init__(self, width, height):
        print(f"A rectangls is created with width: {width} and height: {height}")
        self.width = width
        self.height = height
        
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# object 1
wid = int(input("Enter the width of he rectangle: "))
hei = int(input("Enter the height of he rectangle: "))
rectangle1 = Rectangle(wid, hei)
print("The height and width of rectangle are: ", rectangle1.width,"and", rectangle1.height)
print("The total area of the rectangle is: ", rectangle1.area())
print("The total perimeter of the rectangle is: ", rectangle1.perimeter())

# object 2
wid2 = int(input("Enter the width of he rectangle2: "))
hei2 = int(input("Enter the height of he rectangle2: "))
rectangle2 = Rectangle(wid2, hei2)
print("The height and width of rectangle are: ", rectangle2.width,"and", rectangle2.height)
print("The total area of the rectangle is: ", rectangle2.area())
print("The total perimeter of the rectangle is: ", rectangle2.perimeter())