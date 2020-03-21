import tkinter
from tkinter import *
import pygame

pygame.init()


win=Tk()
win.title("PIANO")
win.geometry("1352x700")
win.configure(background="white")

def A1():
      text.show()
def A2():
      text.show()
def A3():
      text.show()
def A4():
      text.show()
def A5():
      text.show()
def A6():
      text.show()
def A7():
      text.show()

def B1():
      text.show()
def B2():
      text.show()
def B3():
      text.show()
def B4():
      text.show()
def B5():
      text.show()
def B6():
      text.show()
def B7():
      text.show()
def B8():
      text.show()
def B9():
      text.show()
def B10():
      text.show()     



      



LABEL=Label(text="Piano Musical Key",fg="black",font=("arial",50,"bold")).grid(row=0,column=0,columnspan=11)



button1=Button(text="A1",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A1).grid(row=1,column=2)
button2=Button(text="A2",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A2).grid(row=1,column=3)
button3=Button(text="A3",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A3).grid(row=1,column=4)
button4=Button(text="A4",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A4).grid(row=1,column=5)
button5=Button(text="A5",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A5).grid(row=1,column=6)
button6=Button(text="A6",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A6).grid(row=1,column=7)
button7=Button(text="A7",width=6,height=6,bg="black",fg="white",font=("arial",25,"bold"),padx=8,pady=8,command=A7).grid(row=1,column=8)

button8=Button(text="B1",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B1).grid(row=2,column=1)
button9=Button(text="B2",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B2).grid(row=2,column=2)
button10=Button(text="B3",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B3).grid(row=2,column=3)
button11=Button(text="B4",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B4).grid(row=2,column=4)
button12=Button(text="B5",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B5).grid(row=2,column=5)
button13=Button(text="B6",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B6).grid(row=2,column=6)
button14=Button(text="B7",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B7).grid(row=2,column=7)
button15=Button(text="B8",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B8).grid(row=2,column=8)
button16=Button(text="B9",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B9).grid(row=2,column=9)
button17=Button(text="B10",width=6,height=6,fg="black",font=("arial",25,"bold"),bg="white",padx=8,pady=8,command=B10).grid(row=2,column=10)


win.mainloop()

