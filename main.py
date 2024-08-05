# main.py

from threading import Thread
from time import sleep

import configparser#файла конфигурации





#from MathZrenieProect.OpenCVOtladka.OpenCVOtladka import OpenCVOtladka
#from MathZrenieProect.TkinterGUI.TkinterGUI import TkinterGUI

sostoanie_TkinterGUI = {'output': False,
                        'ramka_osX': 0,
                        'ramka_osY': 0,
                        'pramiygolnik_PoX': 20,
                        'pramiygolnik_PoY': 20,
                        'ObnovitConfig': False}
'''СЛОВАРЬ
gender_dict = {0: 'муж',
               1: 'жен'}
------------------------------------------------------------------
Метод update() пригодится, если нужно обновить несколько пар сразу
dictionary.update({'бежал': 'бежать в прошедшем времени',
                   'туфли': 'туфля во множественном числе'})
------------------------------------------------------------------
Метод get() возвращает значение по указанному ключу
story_count = {'сто': 100,
               'девяносто': 90}
------------------------------------------------------------------
Метод items() возвращает пары «ключ — значение»
>>> dictionary.items()
[('персона', 'человек'),
('бежать', 'двигаться со скоростью')]
'''
#------------------------------------------------------------------------
def TkinterGUI():
    import tkinter as tk
    from tkinter import ttk
    from time import sleep

    global sostoanie_TkinterGUI
    global config


    a=1#номер прямоугольника
    #событие на кнопу
    def button_click_def(event):
        print("Нажата кнопка output")
        sostoanie_TkinterGUI.update( {'output': True } )
        window.destroy()
    #событие на кнопу записи координат прямоугольника
    def button_SaveKoordPriamoygoln(event):
        print("Нажата кнопка сохранения координат")
        a= 1 + len(config.options('KoordinatPriamoygolnik'))
        #массив координат прямоугольника
        array=[sostoanie_TkinterGUI['ramka_osX'],
               sostoanie_TkinterGUI['ramka_osY'],
               sostoanie_TkinterGUI['pramiygolnik_PoX'],
               sostoanie_TkinterGUI['pramiygolnik_PoY'],]
        aSTR=str(a)#преобразуем в строку так как конфиг принимает только строки
        arraySTR=str(array)#преобразуем в строку так как конфиг принимает только строки
        config.set('KoordinatPriamoygolnik', aSTR, arraySTR)#записываем данные в конфиг
        #записываем в файл конфиг
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
        #ставим флаг что надо перечитать конфиг
        sostoanie_TkinterGUI.update( {'ObnovitConfig': True } )




    #события на ползунок
    def scale_osX_value(osX_value):
        lbl_1.config(text= osX_value )
        sostoanie_TkinterGUI.update( {'ramka_osX': osX_value } )
    def scale_osY_value(osY_value):
        lbl_2.config(text= osY_value )
        sostoanie_TkinterGUI.update( {'ramka_osY': osY_value } )

    #события на ползунок по размеру рамки
    def scale_pramiygolnikPoX_value(pramiygolnikPoX_value):
        sostoanie_TkinterGUI.update( {'pramiygolnik_PoX': pramiygolnikPoX_value } )
    def scale_pramiygolnikPoY_value(pramiygolnikPoX_value):
        sostoanie_TkinterGUI.update( {'pramiygolnik_PoY': pramiygolnikPoX_value } )

    #события на нажатие всплывающий список, обновляем всплывающий список
    def combobox1_ObnovlenieSpiska(event):
        config.read('config.ini')
        li = [' ']
        li.extend( config.options('KoordinatPriamoygolnik') )#к пустому списку добавляем опции из файла конфигурации
        combobox1.configure(values = li  )
    #события на выбор из списка
    def combobox1_ViborElementaSpiska(event):        
        #combobox.get()#Выбранный элемент можно получить с помощью метода get()
        lbl_1.config(text= combobox1.get() )



    #создаем окно
    window = tk.Tk()
    window.title("Добро пожаловать в приложение PythonRu")
    window.geometry('250x600')
   
    #создаем кнопку выход
    button_output = tk.Button(
        text="output",
        width=15,
        height=1,
        #bg="blue",
        #fg="yellow",
        )
    button_output.place(x = 125, y = 565)#расположение кнопки   
    button_output.bind("<Button-1>", button_click_def)#объявляем событие

    #создаем кнопку сохранить координаты прямоугольника
    button_output = tk.Button(
        text="СохрКоордПрямоуг",
        width=15,
        height=1,
        #bg="blue",
        #fg="yellow",
        )
    button_output.place(x = 1, y = 250)#расположение кнопки   
    button_output.bind("<Button-1>", button_SaveKoordPriamoygoln)#объявляем событие

    #ползунок по расположению на Х
    scale_osX = tk.Scale(window,
                      #variable = v,
                      from_ = 1, to = 620,
                      length=170, width=15,
                      orient = "horizontal",
                      command=scale_osX_value)
    scale_osX.place(x = 45, y = 145)#расположение
    #ползунок по расположению на Y
    scale_osY = tk.Scale(window,
                      #variable = v,
                      from_ = 1, to = 480,
                      length=150, width=15,
                      orient = "vertical",
                      command=scale_osY_value)
    scale_osY.place(x = 0, y = 10)#расположение

    #ползунок по расположению на Х
    scale_pramiygolnikPoX = tk.Scale(window,
                      #variable = v,
                      from_ = 20, to = 150,
                      length=100, width=15,
                      orient = "horizontal",
                      command=scale_pramiygolnikPoX_value)
    scale_pramiygolnikPoX.place(x = 120, y = 0)#расположение
    #ползунок по расположению на Y    
    scale_pramiygolnikPoY = tk.Scale(window,
                      #variable = v,
                      from_ = 20, to = 150,
                      length=100, width=15,
                      orient = "vertical",
                      command=scale_pramiygolnikPoY_value)
    scale_pramiygolnikPoY.place(x = 200, y = 40)#расположение

    # Combobox выпадающий список, пользователь может выбрать один элемент
    combobox1 = ttk.Combobox( values = [' '])
    combobox1.current(0)#Для установки по индексу из привязанного набора значений
    combobox1.pack(anchor='nw', padx=6, pady=285)#расположение
    combobox1.bind("<ButtonPress-1>", combobox1_ObnovlenieSpiska)#событие на нажатие на фиджет
    combobox1.bind("<<ComboboxSelected>>", combobox1_ViborElementaSpiska)#обработки выбора элементов в Combobox


    
    lbl_1 = tk.Label(window, text = 0)#простой текст
    lbl_1.place(x = 30, y = 230)#расположение 
    lbl_2 = tk.Label(window, text = 0)#простой текст
    lbl_2.place(x = 60, y = 230)#расположение 
    
    window.mainloop()
     
#------------------------------------------------------------------------
def OpenCVOtladka():
    from time import sleep
    
    import cv2
    import numpy as np

    img_rgb = cv2.imread(r'1_Thit_2.jpeg',1)
    #cap = cv2.VideoCapture("Mario.jpg",cv2.CAP_IMAGES)
    
    
    if __name__ == '__main__':
        def nothing(*arg):
            pass
        
    cv2.namedWindow( "result" ) # создаем главное окно
    
    #global a
    #sleep(5)
    while True:
        #img = img_rgb
        img = img_rgb.copy()#надо делать copy для удаления старых треугольников
        #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        #flag, img = cap.read()
        
        cv2.rectangle(img, (int(sostoanie_TkinterGUI.get( 'ramka_osX', 0 )),
                               int(sostoanie_TkinterGUI.get( 'ramka_osY', 0 ))),
                               (int(sostoanie_TkinterGUI.get( 'ramka_osX', 0 )) + int(sostoanie_TkinterGUI.get( 'pramiygolnik_PoX', 20 )) ,
                                int(sostoanie_TkinterGUI.get( 'ramka_osY', 0 )) + int(sostoanie_TkinterGUI.get( 'pramiygolnik_PoY', 20 )) ),
                                (255,0,255), 2)
        #
        
        #
        #for KoordinatPriamoygolnik in len(config.options('KoordinatPriamoygolnik')): #возвращает список опций, доступных в указанной секции section
        for KoordinatPriamoygolnikNo in config.options('KoordinatPriamoygolnik'): # если добавили прямоугольник то
            if sostoanie_TkinterGUI.get( 'ObnovitConfig' ):
                # Чтение файла конфигурации
                config.read('config.ini')

            array=[]#создаем массив
 
            a = config.get('KoordinatPriamoygolnik', KoordinatPriamoygolnikNo).replace('\'', '')# .replace удаление всех символов, в данном случае '
            #вытаскиваем из конфига значения и преобразовываем его в массив
            s0 = a.find(',', 0)#ищем в строке запятую
            array.append(int(a[ 1 : s0 ]))#по найденому индексу срезаем нужное значение
            
            s1 = a.find(',', s0+1)
            array.append(int(a[ s0+1 : s1 ]))

            s2 = a.find(',', s1+1)
            array.append(int(a[ s1+1 : s2 ]))

            s3 = a.find(',', s2+1)
            array.append(int(a[ s2+1 : s3 ]))
            #print(array)

            cv2.rectangle(img, (array[0], array[1]), (array[0]+array[2], array[1]+array[3]), (0,0,255), 2)





        cv2.imshow("result", img) 

        ch = cv2.waitKey(5)
        if ch == 27 or sostoanie_TkinterGUI.get( 'output' ):
            break
            
    #cap.release()
    cv2.destroyAllWindows()
        
    #print(sostoanie_TkinterGUI)





 
def main():
    #global a 
    #global b
    
    th1 = Thread(target=OpenCVOtladka)
    th2 = Thread(target=TkinterGUI)
    th1.start()
    th2.start()

    for i in range(5):        
    # Работает
    #print(OpenCVOtladka())
    #print(TkinterGUI())
        sleep(0.5)



#---------работаем с файлом конфигурации------
config = configparser.ConfigParser()
# Чтение файла конфигурации
config.read('config.ini')
# Создание конфигурации
try:
    config.add_section('KoordinatPriamoygolnik')
except:
    print('Конфигурация уже есть')
# Сохранение конфигурации в файл
with open('config.ini', 'w') as config_file:
    config.write(config_file)
#-----конец работаем с файлом конфигурации----

        
print(config.sections())

if __name__ == '__main__':
    main()
