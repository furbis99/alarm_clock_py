from tkinter import *
from time import strftime
import time
import datetime


class AlarmClock:

    def __init__(self):
        self.root = Tk()
        self.root.title('Alarm Clock')
        self.root.geometry("265x270")
        self.root.resizable(width=False,height=False)
        
        self.hrs = StringVar()
        self.mins = StringVar()
        self.sec = StringVar()

        self.label_clock = Label(self.root,font =('arial',16,'bold'),foreground='black',text="Example")
        self.label_clock.grid(row=1,columnspan=4)

        Label(self.root, font = ('arial', 11, 'bold'),text="Hour").grid(row=3,column=1)
        hrbtn=Entry(self.root,textvariable=self.hrs,width=5,font =('arial', 18, 'bold')).grid(row=4,column=1)

        Label(self.root, font = ('arial', 11, 'bold'),text="Minute").grid(row=3,column=2)
        minbtn=Entry(self.root,textvariable=self.mins,width=5, font = ('arial', 18, 'bold')).grid(row=4,column=2)
        
        Label(self.root, font = ('arial', 11, 'bold'),text="Second").grid(row=3,column=3)
        secbtn=Entry(self.root,textvariable=self.sec,width=5,font = ('arial', 18, 'bold')).grid(row=4,column=3)

        setbtn=Button(self.root,text="Set Timer!",command=self.set_alarm,bg="#D4AC0D",fg="Black",font = ('arial', 19, 'bold')).grid(row=20,columnspan=4)

        self.set_time()
        mainloop()
        


    def set_time(self):
        string = strftime('%H : %M : %S %p')
        self.label_clock.config(text=string)
        self.label_clock.after(1000,self.set_time)
    
    def set_alarm():
        pass

    


if __name__ == '__main__':
    AlarmClock()