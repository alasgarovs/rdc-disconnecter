import threading,subprocess ,os
import tkinter as tk
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
from datetime import datetime


pnc=tk.Tk()
pnc.title('....') 
def pncfunc():
    pgen=100
    pyuks=100
    ekrangen = pnc.winfo_screenwidth()
    ekranyuks = pnc.winfo_screenheight()
    x = pgen-ekrangen
    y = pyuks-ekranyuks
    pnc.geometry("%dx%d+%d+%d"%(pgen, pyuks, x, y)) 
    pnc.resizable(width=False,height=False)
    pnc.overrideredirect(1)
    pnc.withdraw()

pncfunc()

def write_error(info):
    c_user=str(os.getlogin()).upper()
    path_error=c_user+'_M_ERROR.txt'
    f=open(path_error,'w')
    f.write(str(info))
    f.close()

    subprocess.Popen(path_error, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def check_path():    
    path=os.path.join(os.environ[r'HOMEPATH'], r'Documents')+r'\DISCONNECTER'
    if os.path.exists(path)==True:
        pass
    else:
        os.system(r'mkdir '+path)

def write_time(info):
    check_path()
    path=os.path.join(os.environ[r'HOMEPATH'], r'Documents')+r'\DISCONNECTER\DISCONNET TIME.txt'

    info_time=str(datetime.now())
    msg=str(info_time+','+info)
    f=open(path,'w')
    f.write(msg)
    f.close()
    

def disconnect():
    try:
        subprocess.Popen('tsdiscon', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        write_time('disconnect')
    except Exception as err_msg:
        write_error(err_msg)
        
def on_press(key):
    if key == keyboard.Key.ctrl_r: 
        thr=threading.Thread(target=disconnect)
        thr.start()
    else:
        write_time('none') 

def on_click(x, y, dx, dy):
    write_time('none')

def on_scroll(x, y, dx, dy):
    write_time('none')


keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener = MouseListener(on_click=on_click, on_scroll=on_scroll)


keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()

pnc.mainloop() 