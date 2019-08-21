
#下载音乐
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