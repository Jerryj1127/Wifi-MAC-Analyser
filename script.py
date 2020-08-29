from subprocess import Popen, PIPE, run
import os
import re
from time import sleep
#from tkinter import messagebox

temp_mac = []

FNULL = open(os.devnull, 'w')
for i in range(5):
    run(['ping', '-c 2' ,'192.168.8.10{}'.format(i)], stdout=FNULL) 
print("Sarted monitering on wifi")

def message(msg):
  import tkinter as tk 
  import tkinter.font as font
  r = tk.Tk() 
  r.title('Wi-Fi Alert') 
  label = tk.Label( text = msg, height = 10)
  button = tk.Button(r, text='Okay', width=100, fg='#FF0000', bg='#000000', command=r.destroy) 
  label['font'] = font.Font(size=30)
  button['font'] = font.Font(size=17)
  label.pack()
  button.pack() 
  r.mainloop() 


while True:
  pid = Popen(["arp", "-n"], stdout=PIPE)
  s = pid.communicate()[0]

  mac = re.findall(r"(?:[A-Fa-f0-9]{2}[:-]){5}(?:[A-Fa-f0-9]{2})", str(s))
  
  if len(temp_mac) < len(mac):
    new_devices = list(set(mac)-set(temp_mac))
    message('{} new device added \n {}'.format(len(new_devices), ", ".join(new_devices)))

  temp_mac = mac

  sleep(10)
