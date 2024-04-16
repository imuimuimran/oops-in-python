# Method overloading
class Add:
    def sum(self, a, b):
        # self.a = a
        # self.b = b
        print(a+b)
        
    def sum(self, a, b, c):
        # self.a = a
        # self.b = b
        # self.c = c
        print(a+b+c)
        
sum1 = Add()

sum1.sum(2,3,4)