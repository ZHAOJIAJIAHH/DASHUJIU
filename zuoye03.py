"""
#编写一个程序来读入不指定个数的整数，统计整数中有多少个正负数，并计算和以及平均值
def zs():
    sum_ = 0
    num = 0
    while num != 3:
        num = int(input('请输入一个整数[输入50停止]：'))
        if num > 0:
            print('是正数')
            sum_ += num
        else:
            sum_ += num
            print('是负数')     

def start():
    zs()
start()
"""


"""
#编写一个程序计算未来十年的学费
def main(money,sum1):
    for i in range(1,14):
        money = money * 0.05 + money
        if i ==10:
            print('十年之后的学费：%.2f'%money)
        if i >= 10: 
            sum1 += money
    print('十年后大学四年的总学费为：%.2f'%sum1)

def start():
    money = 10000
    sum1 = 0
    main(money,sum1)

start()

"""


"""
#编写程序同时被5和6整除
def zhengshu():
    count = 0
    for i in range(100,1000):
        if i%5==0 and i%6==0:
            count += 1
            print(i,end=(' '))
        if count%10 == 0:
            print(' ')
zhengshu()
"""



"""
#编写一个程序找满足条件的数
def panduan():
    i = 100
    while i*i <= 12000:
        i+=1
    print(i)

def pd():
    e = 10
    while e**3 <= 12000:
        e+=1
    print(e)
def start():
    panduan()
    pd()
start()
"""


"""
#编写一个程序求数列求和
def qiuhe():
    sum1 = 0
    for i in range(3,100,2):
        sum1 += (i-2)/i
    print('数列的和为：',sum1) 
qiuhe()
"""

"""
#编写一个程序计算派

def start():
    pai = 0
    i = int(input('输入i的值：'))
    main(pai,i)

def main(pai,i):    
    for j in range(1,i+1):
        pai += 4 * ((-1)**(1+j)/(2*j-1))
    print('π的值为：%f'%pai)

start()
"""


"""
#编写一个程序寻找完全数
def find():
    for i in range(1,10000):
        x = 0
        for j in range(1,i):
            if i % j == 0:
                x += j
        if x == i:
            print('10000以下的完全数有：%d'%x)
find()
"""

"""
#编写程序解决数学组合问题
def zuhe():
    list1 = []
    for i in range(1,8):
        for j in range(1,8):
            if i != j and sorted([i,j]) not in list1:
                list1.append([i,j])
    print('所有可能的组合为：',list1)
    print('组合总个数为：',len(list1))
zuhe()
"""