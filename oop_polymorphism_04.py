 # + operator overloading.

class ComplexNumber:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	# adding two objects 
	def __add__(self, other):
		return self.real + other.real, self.imag + other.imag

cal1 = complex(2, 3)
cal2 = complex(4, 5)
cal3 = cal1 + cal2
print(cal3)
print(cal3.real, "+i", cal3.imag)
