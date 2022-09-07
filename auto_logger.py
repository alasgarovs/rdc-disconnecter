import subprocess,time,os
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import messagebox

pnc=tk.Tk()
pnc.title('....') 
pnc.geometry('200x200')
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
    path_error=c_user+'_A_ERROR.txt'
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

    path=os.path.join(os.environ[r'HOMEPATH'], r'Documents')+r'\DISCONNECTER\DISCONNET TIME.txt'
    if os.path.exists(path)==True:
        pass
    else:
        info_time=str(datetime.now())
        msg=str(info_time+',none')
        f=open(path,'w')
        f.write(msg)
        f.close()

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
    
def showMessage(message, timeout=40000):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost',True)
    try:
        root.after(timeout, root.destroy)
        res=messagebox.showinfo('RDC AUTO DISCONNECT', message, master=root)
        if res == 'ok' :
            write_time('none')
        else :
            disconnect()
        root.destroy()
    except:
        pass


def control():
    while True:
        try:
            check_path()
            path=os.path.join(os.environ[r'HOMEPATH'], r'Documents')+r'\DISCONNECTER\DISCONNET TIME.txt'

            f=open(path,'r')
            content=f.read()
            f.close()
            content=content.split(',')

            if content[1]=='disconnect':
                pass
            else:
                info_time=content[0]
                start_time=datetime.strptime(info_time, r"%Y-%m-%d %H:%M:%S.%f")
                end_time=datetime.now()
                time_diff=end_time-start_time
                seconds=time_diff.seconds

                f=open('DISCONNECTER_LOG.txt','r')
                content=f.read()

                disconnect_second=int(content)
                if seconds>=disconnect_second:
                    msg='Sistemdə aktiv görünmürsünüz,\n40 saniyə sonra sistem bağlanacaq.\n\nLəğv etmək üçün təsdiqləyin !'
                    showMessage(msg)
                else:
                    pass

            time.sleep(10)
        except:
            pass

control()

pnc.mainloop()