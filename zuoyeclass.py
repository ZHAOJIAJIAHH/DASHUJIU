'''
#第一题：
class Rectangle(object):
    def __init__(self,width = 1,height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return (self.width+self.height)*2

    def main(self):
        rectangle = Rectangle(4,40)
        print('宽是>>',rectangle.width)
        print('高是>>',rectangle.height)
        print('面积是>>',rectangle.getArea())
        print('周长是>>',rectangle.getPerimeter())
        print('---------------------------------')
        tom = Rectangle(3.5,35.7)
        print('宽是>>',tom.width)
        print('高是>>',tom.height)
        print('面积是>>',tom.getArea())
        print('周长是>>',tom.getPerimeter())

if __name__ == "__main__":
    x = Rectangle()
    x.main()
'''
'''
#第二题
class Account(object):
    def __init__(self, id_=0, balance=100.0, annualInterestRate=0.0):
        self._id = id_
        self._balance = balance
        self._annualInterestRate = annualInterestRate

@property
def id(self):
    return self._id

@property
def balance(self):
    return self._balance

@property
def annualInterestRate(self):
    return self._annualInterestRate

@id.setter
def id(self, new_id):
    self._id = new_id

@balance.setter
def balance(self, new_balance):
    self._balance = new_balance

@annualInterestRate.setter
def annuallInterestRate(self, new_annualInterestRate):
    self._annuallInterestRate = new_annualInterestRate

def getMonthlyInterestRate(self):
    return self._annualInterestRate/12/100

def getMonthlyInterest(self):
    rate = self.getMonthlyInterestRate()
    res = self._balance * rate
    return res

def withdraw(self, money):
    if self._balance >= money:
        self._balance -= money
        print("您已成功取出：%.2f" % money)
        print("您的余额为：%.2f" % self._balance)
    else:
    print("您的余额不足")
    print("您的余额为：%.2f" % self._balance)
def deposit(self, money):
    self._balance += money
    print("您已成功存入：%.2f" % money)
    print("您的余额为：%.2f" % self._balance)


if __name__ == "__main__":
    a = Account(id_=1122, balance=20000, annualInterestRate=4.5)
    a.withdraw(2500)
    a.deposit(3000)
    print("月利率为：",a.getMonthlyInterestRate())
    print("月利息为：",a.getMonthlyInterest())

'''


"""
#第三题
class Fan(object):

    def __init__(self,speed="SLOW",on=False,radius=5,color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    @property
    def  speed(self):
        return self.__speed
    @speed.setter
    def speed(self,new_speed):
        self.__speed = new_speed 

    @property
    def on(self):
        return self.__on
    @on.setter
    def on(self,new_on):
        self.__on = new_on 

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,new_radius):
        self.radius = new_radius

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,new_color):
        self.__color = new_color

if __name__ =="__main__":
    fan1 = Fan("fast",True,10,"yellow")
    print("速度：",fan1.speed)
    print("半径：",fan1.radius)
    print("颜色：",fan1.color)
    print("已打开：",fan1.on)
    print('======================')
    fan1 = Fan("zhongsu",True,5,"blue")
    print("速度：",fan1.speed)
    print("半径：",fan1.radius)
    print("颜色：",fan1.color)
    print("已打开：",fan1.on)
"""

import math

class RegularPolygon(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self._n = n
        self._side = side
        self._x = x
        self._y = y

    @property #装饰器
    def n(self):
        return self._n  
    @n.setter #修改器
    def n(self,n1):
        self._n = n1
    
    @property #装饰器
    def side(self):
        return self._side 
    @side.setter #修改器
    def side(self,side1):
        self._side = side1
    
    @property #装饰器
    def x(self):
        return self._x 
    @x.setter #修改器
    def x(self,x1):
        self._x = x1
    
    @property #装饰器
    def y(self):
        return self._y 
    @y.setter #修改器
    def y(self,y1):
        self._y = y1
    def getPerimerter(self):
        return self.n*self.side
    def getArea(self):
        return self.n * self.side ** 2 / (4 * math.tan(math.pi / self.n))
if __name__ == "__main__":
    rp1 = RegularPolygon()
    print("周长为:",'%.2f'%rp1.getPerimerter())
    print("面积为:",'%.2f'%rp1.getArea())
    print("---------------------------------------")
    rp2 = RegularPolygon(6,4)
    print("周长为:",'%.2f'%rp2.getPerimerter())
    print("面积为:",'%.2f'%rp2.getArea())
    print("---------------------------------------")
    rp3 = RegularPolygon(10,4,5.6,7.8)
    print("周长为:",'%.2f'%rp3.getPerimerter())
    print("面积为:",'%.2f'%rp3.getArea())
    