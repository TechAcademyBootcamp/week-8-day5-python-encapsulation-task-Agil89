class Author():
    def __init__(self,name,email,gender):
        self.__name= name
        self.__email=email
        self.__gender=gender
    @property
    def getName(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email=email
        return self.__email
    @property
    def getGender(self):
        return self.__gender
    def toString(self):
        return f"Author[name={self.__name},email={self.__email},gender={self.__gender}]"

Shair = Author('Mikayil Musfiq','musfiq@gmail.com','m')

class Book():

    def __init__(self,name,author,price,qty):
        self.__name= name
        self.__price= price
        self.author= author
        self.__qty = qty
    @property
    def getName(self):
        return self.__name


    def getAuthor(self):
        return self.author

    @property
    def price(self):
        return self.__price
    @price.setter
    def setPrice(self,price):
        self.__price=price
        return self.__price

    @property
    def qty(self):
        return self.__qty
    @qty.setter
    def setQty(self,qty):
        self.__qty=qty
        return self.__qty

    def toString(self):
        return f"Book name={self.__name},{self.author.toString()}),price={self.__price},qty={self.__qty}"

kitab = Book('Daglar',Shair,50,10)

print(kitab.toString())