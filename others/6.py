class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 *( self.width + self.length)
rectangles=[Rectangle(4,25),Rectangle(2,4),Rectangle(4,5),Rectangle(1,3),Rectangle(4,3)]

maximum = 0
for r in rectangles:
    if(r.area() > maximum):
        maximum = r.area()
        print(f"Largest Area: {r.area()}")


