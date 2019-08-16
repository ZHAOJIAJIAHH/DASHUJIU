"""
#编写程序，提示用户输入a、b和c的值，然后显示判别式的结果
def canshu(a,b,c):
    r1 = (-b + (b*b - 4*a*c)**0.5)/2*a
    r2 = (-b - (b*b - 4*a*c)**0.5)/2*a
    pianbieshi = b*b - 4*a*c
    if pianbieshi > 0:
        print('The roots are',r1 ,'and',r2 )
    elif pianbieshi == 0:
        print('The roos is',r1)
    else:
        print('The equation has no real roots')

def Start():
    a,b,c = eval(input('Enter a,b,c:' ))
    canshu(a,b,c)

Start()
"""

"""
#编写一个程序产生两个100以下的整数，提示用户的输入整数和，并判断
import random
def zhengshu(a,b):
    c = int(input('请输入整数：'))
    if c == a + b:
        print('True')
    else:
        print('False')

def Start():
    a = random.randint(0,100)
    b = random.randint(0,100)
    zhengshu(a,b)

Start()
"""

"""
#请编写一个程序提示用户今天是一周内的那个数字以及今天之后到未来某天的天数并显示是星期几
def xingqi(a):
    if a == 0:
        print("星期日")
    elif a == 1:
        print('星期一')
    elif a == 2:
        print('星期二')
    elif a == 3:
        print('星期三')
    elif a == 4:
        print('星期四')
    elif a== 5:
        print('星期五')  
    elif a == 6:
        print('星期六')
        
def panduan(a,b):
    c = a + b
    if c >= 7:
        d = c % 7
        xingqi(d)
    else:
        xingqi(c)
         
def Start():
    a = int(input('请输入数字：'))
    b = int(input('请输入整数：'))
    xingqi(a)
    panduan(a,b)

Start()
"""

"""
#编写一个程序输入三个整数并排序
def zhengshu(a,b,c):
    d = [a,b,c]
    d.sort()
    print(d)
def Start():
    a,b,c = eval(input('Enter a,b,c:'))
    zhengshu(a,b,c)
Start()
"""

"""
#编写一个程序比较大米的两张包装的价格 显示价格更好的包装
def  bijiao(weight,price,weight1,price1):
    a = weight/price
    b = weight1/price1
    if a > b:
        print('Package 1 has the better price.')
    else:
        print('Package 2 has the better price.')

def Start():
    weight,price = eval(input('Enter weight and price for package:'))
    weight1,price1 = eval(input('Enter weight and price for package:'))
    bijiao(weight,price,weight1,price1)

Start()
"""


"""
#编写一个程序抛硬币猜测正反
import random
def caice(b):
    a = random.choice('正,反')
    if a == b:
        print('恭喜您，回答正确')
    else:
        print('很遗憾，回答错误')

def Start():
    b = str(input('请输入正面还是反面：'))
    caice(b)
Start()
"""

"""
#编写一个程序——猜拳游戏
import random
def caiquan(com,play):
    if com == play:
        print('平局')
    else:
        if com == 0 and play == 1:
            print('电脑赢了')
        elif com == 1 and play == 2:
            print('电脑赢了')
        elif com == 2 and play == 0:
            print('电脑赢了')   
        else:
            print('你赢了')     
def Start():
    com = random.randint(0,2)
    play = int(input('0:石头,1:剪刀,2:布'))
    caiquan(com,play)

Start()
"""

"""
#编写程序提示用户输入一个三位数 判断他是否是回文数
def huiwenshu(a): 
    a = str(a)
    c = a[::-1]
    if a == c:
        print('是回文数')
    else:
        print('不是')
def Start():
    a = int(input('请输入一个三位数'))
    huiwenshu(a)
Start()
"""

"""
#编写一个程序读取三条边并计算周长
def zhouchang(c,k,g):
    if c + k > g and k + g > c:
        d = c + k + g
        print('The perimeter is',d)
def Start():
    c,k,g = eval(input('Enter c,k,g:'))
    zhouchang(c,k,g)
Start()
"""
    