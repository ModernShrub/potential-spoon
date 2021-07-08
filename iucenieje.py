from tkinter import *
import random

root=Tk()
root.title("sdiy")
root.geometry("500x600")

label = Label(root)
label1 = Label(root)
input1 = Entry(root)

array_3d = [[[1, 2, 3, 4, 5, 87, 7], ["Gee", "Me", "Home", "Key", "Passkey"], ["D", "G", "F", "T", "E", "U"], ["!", "@", "&", "%", "$", "*", "?", "#"]]]

print(array_3d[0][2][3])

def passkeygen():
    
    iwc = input1.get()
    label1['text'] = "Passkey : " + str(iwc)
    
    randno1 = random.randint(0, 6)
    randno2 = random.randint(0, 4)
    randno3 = random.randint(0, 5)
    randno4 = random.randint(0, 7)
    
    keyno1 = str(array_3d[0][0][randno1])
    keyno2 = str(array_3d[0][1][randno2])
    keyno3 = str(array_3d[0][2][randno3])
    keyno4 = str(array_3d[0][3][randno4])    
    label['text'] = " New Passkey : " + keyno1 + keyno2 + keyno3 + keyno4
    
btn = Button(root, text="Genarate Password", command=passkeygen)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
input1.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()
    
    
    