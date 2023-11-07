# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:54:13 2023

@author: anyta
"""
from tkinter import *

root = Tk();
root.title("Proyecto 145");
root.geometry("400x400");

etiqueta = Label(root)
etiqueta1 = Label(root)
def Proyecto():
    resultado = 12*6
    etiqueta["text"] = "12 x 6"
    etiqueta1["text"] = resultado
    
btn = Button(root, text = "obtener", command = Proyecto)

etiqueta.pack()
btn.pack()
etiqueta1.pack()

root.mainloop()