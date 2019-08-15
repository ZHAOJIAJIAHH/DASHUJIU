"""
#编写一个程序将华氏温度转化为摄氏温度
celsius = int(input('Enter a degree in Celsius：'))
fahrenheit = (9 / 5 ) * celsius + 32
print(celsius,'Celsius is',fahrenheit)
"""

"""
#编写一个程序读取圆柱体的半径和高并计算圆柱体的底面积和体积
import math
radius = float(input('radius: '))
length = float(input('length: '))
area = radius * radius * math.pi
print('The area is',area)
volume = area * length
print('The volume is',volume)
"""

"""
#编写一个程序把英尺数转换为米数并显示结果
feet = float(input('Enter a value for feet: '))
meter = feet * 0.305
print(feet,'feet is',meter,'meters')
"""

"""
#编写一个程序计算将水从初始温度加热到最终温度所需要的能量
kilograms = float(input('Enter the amount of water in kilograms:'))
temperature = float(input('Enter the initial temperature:'))
temperature_1 = float(input("Enter the final temperature:"))
Q = kilograms * (temperature_1 - temperature) * 4184
print('The energy needed is',Q)
"""

"""
#编写一个程序计算下个月的月供的利息
cha_e = float(input('请输入差额：'))
nian_li_lv = float(input('请输入年利率：'))
rate = cha_e * (nian_li_lv / 1200)
print('The interest is',rate)
"""

"""
#编写一个程序计算平均加速度
initialfast = float(input('请输入初始速度：'))
finalfast = float(input('请输入末速度：'))
time = float(input('time:'))
average = ((finalfast - initialfast)/time)
print('The average accleration is',average)
"""

"""
#编写一个程序计算账户总额
money = 100
yue_li_lv = 0.00417
first_month = money * (1 + yue_li_lv)
second_month = (money + first_month) * (1 + yue_li_lv)
third_month = (money + second_month) * (1 + yue_li_lv)
fouth_month = (money + third_month) * (1 + yue_li_lv)
fifth_month = (money + fouth_month) * (1 + yue_li_lv)
sixth_month = (money + fifth_month) * (1 + yue_li_lv)
print('After the sixth month, the account value is',sixth_month)
"""
"""
#编写一个程序计算0到1000之间整数各位数字之和
number = int(input('请输入一个三位数：'))
ge = number%10
shi = number//10%10
bai = number//10//10%10
sum = ge + shi + bai
print('The sum of the digits is:',sum)
"""


"""
import random
emile = '123456@163.com'
password = 123456
count = 0
emile1 = input('账号：')
if '@163.com' not in emile1:
    print('账号不合法，请重新输入')
else:
    for i in range(4):
        emile1 = input('账号：')
        password1 = int(input('密码：'))
        if emile1 == emile and password1 == password:
            print("登陆成功")
            break
        else:
            print('账号或密码错误，请重新输入')
            count += 1
            yzm = random.randint(1000,9999)
            print(yzm)
            num = int(input("输入验证码"))
            if num == yzm :
                print("验证成功")
            else :
                print("请重新输入验证码")
    if count == 4:
        print('已锁定，请持本人身份证到王晓萌处办理')

"""
import hashlib
email = input('请输入邮箱号：')
hash = hashlib.md5()#创建md5对象
hash.update(email.encode('utf-8'))#如果不使用encode()则会报错
res = hash.hexdigest()#进行加密
print(res)



