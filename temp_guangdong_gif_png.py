# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 19:25:16 2022

@author: Eric Kwong
"""
#pyinstaller --onefile --noconsole temp_guangdong_gif_png.py
#pyinstaller --onefile --noconsole --icon=icon.ico temp_guangdong_gif_png.py

from tkinter import *
import requests
import time
import os
from PIL import Image
import glob
import datetime

class MyWindow:
    global choice_png
    choice_png = True
    global choice_gif
    choice_gif = False
    def __init__(self, win):
        self.lbl1 = Label(win, text='Year: ')
        self.lbl2 = Label(win, text='Month: ')
        self.lbl3 = Label(win, text='Day: ')
        self.lbl4 = Label(win, text='Hours: ')
        self.lbl5 = Label(win, text='to')
        self.lbl6 = Label(win, text='Directory: ')
        self.lbl7 = Label(win, text='e.g. C:\\Users\\nameless\Desktop\\temp_guangdong\\')
        self.lbl8 = Label(win, text='to')
        
        text1 = StringVar()
        text1.set(datetime.datetime.now().year)
        self.t1 = Entry(bd=2, width=40, textvariable = text1) #bd: thickness of the box
        text2 = StringVar()
        text2.set(datetime.datetime.now().month)
        self.t2 = Entry(bd=2, width=40, textvariable = text2)
        text3 = StringVar()
        text3.set(datetime.datetime.now().day)
        self.t3 = Entry(bd=2, width=15, textvariable = text3)
        text4 = StringVar()
        text4.set("00")
        self.t4 = Entry(bd=2, width=15, textvariable = text4)
        text5 = StringVar()
        text5.set(datetime.datetime.now().day)
        self.t5 = Entry(bd=2, width=15, textvariable = text5)
        filepath = os.path.realpath(__file__)
        length = len("\temp_guangdong_gif_png.py")
        filepath = filepath[:len(filepath)-length]
        text6 = StringVar()
        text6.set(filepath)
        self.t6 = Entry(bd=2, width=40, textvariable = text6)
        text7 = StringVar()
        text7.set("23")
        self.t7 = Entry(bd=2, width=15, textvariable = text7)
        text8 = StringVar()
        text8.set("NOT YET...")
        self.t8 = Entry(bd=2, width=40, state = DISABLED, textvariable = text8)
        text9 = StringVar()
        text9.set("SETTING: GETTING PNGs ONLY")
        self.t9 = Entry(bd=2, width=31, state = DISABLED , textvariable = text9)
        
        self.btn1 = Button(win, text='EXECUTE')
        self.btn2 = Button(win, text='CONVERT GIFs')
        self.btn3 = Button(win, text='NO PNGs')
        self.btn4 = Button(win, text='RESET')
        
        self.lbl1.place(x=50, y=20)
        self.t1.place(x=150, y=20)
        self.lbl2.place(x=50, y=60)
        self.t2.place(x=150, y=60)
        self.lbl3.place(x=50, y=100)
        self.t3.place(x=150, y=100)
        self.lbl4.place(x=50, y=140)
        self.t4.place(x=150, y=140)
        self.lbl5.place(x=283, y=100)
        self.t5.place(x=325, y=100)
        self.lbl6.place(x=50, y=180)
        self.t6.place(x=150, y=180)
        self.lbl7.place(x=150, y=200)
        self.t7.place(x=325, y=140)
        self.lbl8.place(x=283, y=140)
        self.t8.place(x=150, y=272)
        self.t9.place(x=215, y=232)
        
        self.b2=Button(win, text='GET GIFs', command=self.gif)
        self.b2.place(x=150, y=230)
        
        self.b3=Button(win, text='NO PNGs', command=self.png)
        self.b3.place(x=50, y=230)
        
        self.b3=Button(win, text='RESET', command=self.reset)
        self.b3.place(x=2, y=230)
        
        self.b1=Button(win, text='EXECUTE', command=self.execute)
        self.b1.place(x=50, y=270)


    def execute(self):
        global choice_png
        global choice_gif
        text8 = StringVar()
        text8.set("EXECUTING...")
        self.t8 = Entry(bd=2, width=40, state = DISABLED , textvariable = text8)
        
        year = str(self.t1.get())
        month = int(self.t2.get())
        day = int(self.t3.get())
        hour = int(self.t4.get())
        num_of_day = int(self.t5.get())
        directory = str(self.t6.get())
        hour_end = int(self.t7.get())
        hour_start = hour
        
        num_of_day = num_of_day - day + 1
        day = day - 1
        hour = hour_end
        if (directory[-1] != "\\"):
            directory = directory + "\\"

        #Below: All fixed
        while (num_of_day != 0):    
            num_of_day = num_of_day - 1
            month = int(month)
            day = int(day) + 1  #Fixed
            cnt = int(hour_end) + 1 #Fixed
            temp = int(hour_end) + 1#Fixed
            gif = ".gif"
            
            if (month < 10):
                month = '0'+str(month)
            else:
                month = str(month)
                
            if (day < 10):
                day = '0'+str(day)
            else:
                day = str(day)
                
            filename = year + month + day
            
            while (cnt != hour_start):
                cnt = cnt - 1
                
                if (cnt < 10):
                    hour = '0'+str(cnt)
                else:
                    hour = str(cnt)   
                    
                data = year + month + day + hour + '00'
            
                url = 'https://soc.gd121.cn/skt/'+str(year)+'/'+str(month)+'/MSP1_AGD_MANOBS_T_L88_AGD_'+str(data)+'_00000-00000.PNG'
                    
                with open(directory + str(data) +'.png','wb') as f:
                    f.write(requests.get(url).content)
                fsize = os.path.getsize(directory +str(data)+'.png')
                text8 = StringVar()
                text8.set("GETTING" + data + '.png')
                self.t8 = Entry(bd=2, width=40,  state = DISABLED,textvariable = text8)
                self.t8.place(x=150, y=272)
                
                if (fsize < 10000):
                    os.remove(directory + str(data) +'.png')
                    temp = cnt
                    text8 = StringVar()
                    text8.set("No Data: " + data)
                    self.t8 = Entry(bd=2, width=40,  state = DISABLED,textvariable = text8)
                    self.t8.place(x=150, y=272)
                else:
                    print(url)
            
            text8 = StringVar()
            text8.set("Done: GETTING ALL .png FILES")
            self.t8 = Entry(bd=2, width=40,  state = DISABLED,textvariable = text8)
            self.t8.place(x=150, y=272)
            
            if (choice_gif == True):
                # Create the frames
                frames = []
                path_png = directory + "\*.png"
                imgs = glob.glob(path_png)
                for i in imgs:
                    new_frame = Image.open(i)
                    frames.append(new_frame)
                 
                # Save into a GIF file that loops forever
                frames[0].save(directory + filename + gif , format='GIF',
                               append_images=frames[1:],
                               save_all=True,
                               duration=250, loop=0)
            
            cnt = temp
            
            if (choice_png == False):
                while (cnt!= hour_start):
                    cnt = cnt - 1
                    
                    if (cnt < 10):
                        hour = '0'+str(cnt)
                    else:
                        hour = str(cnt)   
                        
                    data = year + month + day + hour + '00'
                
                    url = 'https://soc.gd121.cn/skt/' + str(year)+'/'+str(month)+'/MSP1_AGD_MANOBS_T_L88_AGD_'+str(data)+'_00000-00000.PNG'
                    
                    fsize = os.path.getsize(directory + str(data) + '.png')
                    if (fsize > 0):
                        os.remove(directory + str(data) + '.png')
            
            text8 = StringVar()
            text8.set("DONE!")
            self.t8 = Entry(bd=2, width=40,  state = DISABLED,textvariable = text8)
            self.t8.place(x=150, y=272)

    def gif(self):
        global choice_png
        global choice_gif
        choice_gif = True
        if ((choice_gif == True)&(choice_png == False)):
            text9 = StringVar()
            text9.set("SETTING: GETTING GIFs ONLY")
            self.t9 = Entry(bd=2, width=31, state = DISABLED, textvariable = text9)
        if (choice_gif == True)&(choice_png == True):
            text9 = StringVar()
            text9.set("SETTING: GETTING GIFs & PNGs")
            self.t9 = Entry(bd=2, width=31, state = DISABLED, textvariable = text9)
        self.t9.place(x=215, y=232)    
    def png(self):
        global choice_png
        global choice_gif
        choice_png = False
        if ((choice_gif == False)&(choice_png == False)):
            text9 = StringVar()
            text9.set("SETTING: PLEASE PRESS RESET")
            self.t9 = Entry(bd=2, width=31, state = DISABLED, textvariable = text9)
        if (choice_gif == True)&(choice_png == False):
            text9 = StringVar()
            text9.set("SETTING: GETTING GIFs ONLY")
            self.t9 = Entry(bd=2, width=31, state = DISABLED, textvariable = text9)
        self.t9.place(x=215, y=232)
        
    def reset(self):
        global choice_png
        choice_png = True
        global choice_gif
        choice_gif = False
        text9 = StringVar()
        text9.set("SETTING: GETTING PNGs ONLY")
        self.t9 = Entry(bd=2, width=31, state = DISABLED, textvariable = text9)
        self.t9.place(x=215, y=232)

window=Tk()
mywin=MyWindow(window)
window.title('Guang Dong: Temperature GIF/PNG')
window.geometry("500x300+400+200")   #size & window location
window.mainloop()