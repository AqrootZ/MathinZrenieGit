# main.py

from threading import Thread
from time import sleep



#from MathZrenieProect.OpenCVOtladka.OpenCVOtladka import OpenCVOtladka
#from MathZrenieProect.TkinterGUI.TkinterGUI import TkinterGUI

sostoanie_TkinterGUI = {'output': False,
                        'ramka_osX': 0,
                        'ramka_osY': 0,
                        'pramiygolnik_PoX': 20,
                        'pramiygolnik_PoY': 20}
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
    from time import sleep

    global sostoanie_TkinterGUI
    

    #событие на кнопу
    def button_click_def(event):
        print("Нажата кнопка output")
        sostoanie_TkinterGUI.update( {'output': True } )
        window.destroy()

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



    #создаем окно
    window = tk.Tk()
    window.title("Добро пожаловать в приложение PythonRu")
    window.geometry('250x600')
   
    #создаем кнопку
    button_output = tk.Button(
        text="output",
        width=15,
        height=1,
        #bg="blue",
        #fg="yellow",
        )
    button_output.place(x = 125, y = 565)#расположение кнопки   
    button_output.bind("<Button-1>", button_click_def)#объявляем событие

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




if __name__ == '__main__':
    main()
