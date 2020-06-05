class Vehicle():
    __numofWheels =4
    __color="black"
    __engine=2.4
    __positionX=1
    __positionY=1
    __speed=50
    __isOn=False

    def __init__(self,color,engine,numofWheels):
        self.__color=color
        self.__engine=engine
        self.__numofWheels=numofWheels


    def accelerate(self):
        self.__speed = self.__speed + 1
        return self.__speed

    def moveForward(self,x,y):
        self.__positionX = self.__positionX + x
        self.__positionY = self.__positionY + y
        return f"{self.__positionX} {self.__positionY}"
    def moveBackwards(self,x,y):
        self.__positionX = self.__positionX - x
        self.__positionY = self.__positionY - y
        return f"{self.__positionX} {self.__positionY}"

    def ignition(self):
        if self.__isOn == False:
            self.__isOn = True
        elif self.__isOn == True:
            self.__isOn = False
    @property
    def numofWheels(self):
        return self.__numofWheels
    @numofWheels.setter
    def numofWheels(self,num):
        self.__numofWheels = num
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
        return self.__color
    @property
    def speed(self):
        return self.__speed
    # @speed.setter
    # def speed(self,x):
    #     self.__speed += x
    #     return self.__speed
    def __str__(self):
        print(str(f"""tekerlerin sayi:{self.__numofWheels}
                  masinin rengi:{self.__color}
                  matorun hecmi: {self.__engine}
                  x pozisyon: {self.__positionX}
                  y pozisyon:  {self.__positionY}
                  speed : {self.__speed}
                    """))


class Motorcycle(Vehicle):
    brand = 'harley'
    numOfSeats = 1

    def __init__(self,color, engine,wheels, brand, seats):
        self.__color = color
        self.__engine = engine
        self.__wheels = wheels
        self.__brand = brand
        self.__seats = seats
    @property
    def brand(self):
        return self.__brand
    @property
    def numOfSeats(self):
        return self.__numOfSeats
    @brand.setter
    def brand(self,brand):
        self.__brand = brand
    @numOfSeats.setter
    def numofSeats(self,numofSeats):
        self.__numOfSeats = numofSeats
    def accelerate(self):
        newSpeed = self.speed
        newSpeed +=10
        return newSpeed
    def decelerate(self):
        newSpeed = self.speed
        newSpeed = newSpeed - 10
        return newSpeed


my_motor = Motorcycle('red', 1.2,2, 'h-d', '1')

print(my_motor.accelerate())
print(my_motor.accelerate())
print(my_motor.accelerate())

bmw = Vehicle('white',3.0,4)
print(bmw.moveForward(5,5))
print(bmw.moveBackwards(6,6))
bmw.color = 'black'
print(bmw.color)