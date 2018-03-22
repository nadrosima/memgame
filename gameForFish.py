#15/08/2015
import os
import thread,time
import random

import math

try:
    dirs = os.path.dirname(os.__file__).lower()
    if "python2" in dirs:
        from Tkinter import *
    elif "python3" in dirs:
        from tkinter import *
except Exception,e : print e

LARGE_FONT = ("Verdana",20)
color = 0

root = Tk()
frame = Frame(root)
root.title("Game for fish or variants")
root.geometry("200x200")
root.resizable(0, 0)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N + S + E + W)
grid = Frame(frame)
grid.grid(sticky=N + S + E + W, column=0, row=8, columnspan=2)
Grid.rowconfigure(frame, 8, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

class _zo : pass
zo = _zo()
zo.foo = []
zo.pick = None
zo.lq =[]
zo.a = {}
zo.level = 0
zo.lev_list = [4,9,16,25,36,49,64,81]
zo.miss = 0


def get_num(num):
    h = sorted(zo.a.keys())
    p = zo.foo.index(num)
    if num in zo.lq and num == zo.pick :
        zo.a["%0.2d_%d"%(p,num)].config(text=num, state="disabled")

        if len(zo.lq) > 1 :
            zo.lq.remove(num)
            zo.pick = ( random.choice(zo.lq))
            zo.a["my_lab"].config(text= "where is %d ?" % zo.pick)
        elif len(zo.lq) == 1:
            zo.lq = []
            zo.foo = []
            zo.pick = None
            zo.level = zo.level +1
            for s in zo.a.keys() :
                zo.a[s].destroy()
            zo.a = {}
            do_cube(zo.lev_list[zo.level])


    else:
        zo.miss += 1
        zo.a["my_lab"].config(text="Try again for (%d)!(Miss:%s)"%(zo.pick,zo.miss))    





def timot(hu):
    time.sleep(2)
    n = sorted(zo.a.keys())   

    for s in n :
        if not s.startswith("my"):
            y = zo.foo[n.index(s)]
            zo.a[s].config(text=y)
            time.sleep(1)
            zo.a[s].config(text="")
    zo.pick = random.choice(zo.foo)
    for j in n: zo.a[j].config(state="normal")
    zo.a["my_lab"].config(text="where is %d ?" %zo.pick)

def do_cube(many):
    bx = int(math.sqrt(many))
    w = (200+(200*(zo.level*0.15)))
    root.geometry("%dx%d+400+200" %(w,w+(20+(5*zo.level))))


    color = "orange","red","green","blue","yellow","brown","dodgerblue","pink"
    zo.foo  = random.sample(range(100),many)
    zo.lq = [e for e in zo.foo]

    for x in range(bx):
        for y in range(bx):
            ind = (x*bx) + y  
            rand_no = zo.foo[ind]

            butn = Button(frame, bg=color[x], command= lambda rand_no=rand_no:get_num(rand_no), font=LARGE_FONT,state="disabled")
            butn.grid(column=x, row=y, sticky=N + S + E + W)

            zo.a["%0.2d_%d"%(ind,rand_no)] = butn

    for x in range(bx):
        Grid.columnconfigure(frame, x, weight=1)
    for y in range(bx):
        Grid.rowconfigure(frame, y, weight=1)

    zo.a["my_lab"] = Label(root,text="ready !")
    zo.a["my_lab"].grid(column=0, row=bx+1, sticky=N + S + E + W,columnspan = bx)


    thread.start_new_thread(timot,(None,))


do_cube(zo.lev_list[zo.level])


root.mainloop()
