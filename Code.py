from cProfile import label
from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import *
from turtle import left
from cairo import Extend
import pywinusb.hid as hid
import string
import pywinusb.hid as hid
import tkinter as tk
 
#Fct Read
def readD():
    
    def readData(data):
        val = "Data: {0}".format(data), "\n"
        texte1.insert(2.0, val)
        return None
    
    device.set_raw_data_handler(readData)
    return None

#Fct Write
def write():    

    DATA = texte2.get("1.0", "end")
    DATA1 = int(DATA)
    #print(DATA)

    def sample_handler(data):
        "Raw data: {0}".format(data)
        return None
    
    target_usage = hid.get_full_usage_id(0x00, 0x3f)
    device.set_raw_data_handler(sample_handler)
    
    report = device.find_output_reports()

    buffer = [16]*9
    buffer[0] = 0x00
    # data to be transmitted from HID to UART
    buffer[1] = DATA1  # data length;   Range->1 to 63
    buffer[2] = 0x01 # data 1
    buffer[3] = 0x02 # data 2
    buffer[4] = 0x03 # data 3
    buffer[5] = 0x04 # data 4
    buffer[6] = 0x05 # data 5
    buffer[7] = 0x06 # data 6
    buffer[8] = 0x07 # data 7
     
    report[0].set_raw_data(buffer)
    report[0].send()

# Creation de la fenetre
window = Tk()

# Personalisation de la fenêtre
window.title("Ecriture USB_HID (M-Extend)")
window.geometry("750x450")
window.iconbitmap("logo-white.ico")
window.config(background='#D7EEFD')

#Création des frames
frame_1 = Frame(window, bg ='#D7EEFD')
frame_2 = Frame(window, bg ='#D7EEFD')

#ajout de la frame
frame_1.pack(side = TOP)
frame_2.pack(expand=TRUE)

#ajout titre
label_title = Label(frame_1, text="Ecriture/Lecture de la liaison USB HID", font=("Arial", 26), bg='#D7EEFD', fg='black')
label_title.grid(row=0, column=0)

#Config USB
filter = hid.HidDeviceFilter(vendor_id = 0x0483, product_id = 0x5750)
hid_device = filter.get_devices()
device = hid_device[0]
device.open()

#TXT Lecture
texte1 = Text(frame_2, bg='#D7EEFD', fg='black', width=40, height=15)
texte1.grid(row=1, column=0)

#TXT Ecriture
texte2 = Text(frame_2, bg='#D7EEFD', fg='black', width=40, height=15)
texte2.grid(row=1, column=3)


#BTN_Read
BTN_lire = Button(frame_2, text="Lire", font=("Arial", 18), bg='white', fg='black', command=readD)
BTN_lire.grid(row=0, column=0)

#BTN_Write
BTN_Ecrire = Button(frame_2, text="Ecrire", font=("Arial", 18), bg='white', fg='black', command=write)
BTN_Ecrire.grid(row=0, column=3)

# Affichage de la fenetre
window.mainloop()
