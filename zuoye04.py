#funtion
"""
#第一题
def getPentagonalNumber():
    n = 0
    for i in range(1,101):
        b = (n*(3*n-1))/2
        n += 1
        print(b,end=(' '))
        if n%10 == 0:
            print('')


getPentagonalNumber()
"""

"""
#第二题：
def sumDigits(n):
    sum = 0
    m = str(n)
    for i in range(len(m)):
        num = n//10**i%10
        sum += num 
        print(sum)
def start():
    n = int(input("输入一个整数:"))
    sumDigits(n)
    
start()
"""

"""
#第三题
def displaySortedNumbers(num1,num2,num3):
    num = [num1,num2,num3]
    num.sort()
    print(num)
    

def start():
    num1,num2,num3 = map(float,input('Enter three number:').split(','))
    displaySortedNumbers(num1,num2,num3)

start()
"""

"""
#第四题
def futureInvestmenValue(investmentAmount,AnnualInterestRate):
    monthlyInterestRate = float(AnnualInterestRate)/12/100
    print("Years","\t","Future Value")
    for years in range(1,31):
        futureValue = investmentAmount * ((1 + monthlyInterestRate)**(12*years))
        print(years,"\t","%.2f"%futureValue)

def start():
    investmentAmount = eval(input("The amount invested："))
    AnnualInterestRate = eval(input("Annual interest rate："))
    futureInvestmenValue(investmentAmount,AnnualInterestRate)
start()
"""

"""
#第五题
def printChars(ch1,ch2):
    count = 0
    for i in range(ch1,ch2):
        count += 1
        print(chr(i),end = ' ')
        if count % 10 == 0:
            print('')
def srart():
    ch1 = 65
    ch2 = 91
    printChars(ch1,ch2)
srart()
"""

"""
#第六题
def numberOfDaysInAYear():
    for year in range(2010,2021):
        if year%400 == 0 and year%4 == 0 or year%100!=0:
            print(year,'有366天')
        else:
            print(year,"有365天")

numberOfDaysInAYear()
"""  

"""
#第七题
def distance(x1,y1,x2,y2):
    c = ((x2-x1)**2-(y2-y1)**2)**0.5
    print(c)
def start():
    x1,y1,x2,y2 = map(float,input('Enter four number:').split(','))
    distance(x1,y1,x2,y2)  
start()
"""

"""
#第八题
def sushu():
    i = 2
    c = []
    d = []
    while i <=31:
        j = 2
        while j <= i:
            if i % j ==0:
                if i == j:
                    c.append(i)
                break
            j += 1
        i += 1
    print(c) 
    for p in c:
        d.append(2**p-1) 
    print(d) 
sushu()
"""

#第九题

"""
#第十题
import random
def zhishaizi(s1,s2):
    if s1+s1 == 2 and s1+s2 == 3 and s1+s2==12:
        print('你输了')
    elif s1+s2 == 7 and s1+s2 == 11:
        print('你赢了')
    else:
        print('请重新投掷')
    

def start():
    s1 = random.randint(1,6)
    s2 = random.randint(1,6)
    zhishaizi(s1,s2)

start()

"""





"""
#class
#第一题
class Rectangle(object):

def __init__ (self,width = 1,height = 2):
    self.width = width
    self.height = height

def getArea(self):
    return self.width*self.height

def grtPerimeter(self):
    return (self.width+self.height)*2

if __name__ == "__main__":
    rectangle = Rectangle(4,40)
    print('宽是：',rectangle.width)
    print('高是：',rectangle.height)
    print('面积是：',rectangle.getArea())
    print('周长是：',rectangle.getPerimeter())
    
    tom = Rectangle(3.5,35.7)
    print('宽是：',tom.width)
    print('高是：',tom.height)
    print('面积是：',tom.getArea())
    print('周长是：',tom.getPerimeter())

x = Rectangle()
    
"""


   


