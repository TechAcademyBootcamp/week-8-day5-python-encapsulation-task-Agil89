import math
class Shape():
    def __init__(self,color,filled):
        self.__color = color
        self.__filled = filled
    def toString(self):
        return f"A Shape with colors of {self.__color} and {self.__filled}"
shape1 = Shape('red',True)
class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius
    @property
    def getArea(self):
        return 3.14*(self.__radius**2)
    @property
    def getPerimeter(self):
        return (3.14 * self.__radius)/2
    def toString(self,obj):
        return f"A Circle with radius={self.__radius}, which is a subclass of {obj.toString()}"
class Rectangle(Shape):
    def __init__(self,width,length):
        self.__width=width
        self.__length=length
    @property
    def getWidth(self):
        return self.__width
    @property
    def getLength(self):
        return self.__length
    @property
    def getArea(self):
        return self.__width*self.__length
    @property
    def getPerimeter(self):
        return (self.__width+self.__length)*2
    def toString(self,obj):
        return  f"A Rectangle with width={self.__width} and length={self.__length}, which is a subclass of {obj.toString()}"
circle1 = Circle(5)
rect1 = Rectangle(5,10)

class Square(Rectangle):
      def getAreaOfSquare(self):
          return f'its a subclass with {self.getLength} and {self.getWidth}'

print(circle1.toString(shape1))
print(rect1.toString(shape1))
square1 = Square(2,3)
print(square1.getAreaOfSquare())