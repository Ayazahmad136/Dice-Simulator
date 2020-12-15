from tkinter import *
import random
root=Tk()
root.title('Dice Simulator')
root.geometry('800x500')

l1= Label(root , font='lucida 300')
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)} {random.choice(number)}')
    l1.pack()

b1=Button(root,text='Lets roll..', font='lucide 24',padx=5, pady=5 ,command =roll)
b1.pack()
root.mainloop()
