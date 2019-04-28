import time
import threading
from statistics import mean
from PIL import Image
from threading import Thread

from numba import cuda



image = Image.open("temp1024.jpg")  # Открываем изображение.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.
@cuda.jit
def Intensity():
     ls = []
     for i in range(width):
        for j in range(height):
            a = pix[i,j][0]
            b = pix[i,j][1]
            c = pix[i,j][2]
            S = (a+b+c)/3
            ls.append(S)
def imgSize():
    imResize = image.resize((width*2,height*2), Image.ANTIALIAS)
    imResize.save('new.jpeg')
    # проверка для увеличенного изображения
    # width2 = imResize.size[0] #Определяем ширину.
    # height2 = imResize.size[1] #Определяем высоту.
    # pix2 = imResize.load() #Выгружаем значения пикселей.
    # ls = []
    # for i in range(width2):
    #     for j in range(height2):
    #         a2 = pix2[i,j][0]
    #         b2 = pix2[i,j][1]
    #         c2 = pix2[i,j][2]
    #         S2 = (a2+b2+c2)/3
    #         ls.append(S2)
    # return mean(S2)

if __name__ == '__main__':
    local_start_time = time.time()
    for i in range(2):  #разбитие на потоки
        my_thread = threading.Thread(target=Intensity)
        my_thread2 = threading.Thread(target=imgSize)
        my_thread.start()
        my_thread2.start()
        # my_thread.join()
        # my_thread2.join()
        # print(threading.currentThread())
    t = time.time() - local_start_time
    print("Время работы потоков: {t:0.6f}".format(t=time.time() - local_start_time))
