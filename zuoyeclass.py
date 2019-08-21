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
import multiprocessing
import json 
import os
import requests
def dy():
    with open('C:\\Users\\asus\\Desktop\\top_500.txt',mode='r') as f:
        res = f.readlines()[0].strip('\n').split('}')
        # count = 0
        list_1 = []
        for json_ in res[:-1]:
            _json = json_ + '}'
            _json = json.loads(_json)
            song_play_url = _json['song_play_url']
            song_name = _json['song_name']
            print (song_name)
            if song_play_url is not None:
                list_1.append(song_play_url)
                # count +=1
                # print(song_play_url)
                # print(count)
                for i in list_1[0:24]:
                    path = i
                    response = requests.get(path)
                    mp3_ = response.content
                    with open('C:\\Users\\asus\\Desktop\\music\\' +song_name+'.mp3',mode='wb') as f:
                        f.write(mp3_)
def dx():
    with open('C:\\Users\\asus\\Desktop\\top_500.txt',mode='r') as f:
        res = f.readlines()[0].strip('\n').split('}')
        # count = 0
        list_1 = []
        for json_ in res[:-1]:
            _json = json_ + '}'
            _json = json.loads(_json)
            song_play_url = _json['song_play_url']
            song_name = _json['song_name']
            #print (song_name)
            if song_play_url is not None:
                list_1.append(song_play_url)
                # count +=1
                # print(song_play_url)
                # print(count)
                for i in list_1[24:47]:
                    path = i
                    response = requests.get(path)
                    mp3_ = response.content
                    with open('C:\\Users\\asus\\Desktop\\music\\' +song_name+'.mp3',mode='wb') as f:
                        f.write(mp3_)
        
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=dy)   
    p2 = multiprocessing.Process(target=dx)
    p1.start()#启动线程
    p2.start()
    p1.join() #阻塞线程
    p2.join()
    print('ok')
'''