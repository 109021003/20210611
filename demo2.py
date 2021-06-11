from tkinter import *
    
op = 0
v1 = 0
opFlag = False
def _chan(num):
    if int(lab['text']) != 0:
        lab["text"] = lab["text"] + num
    else:
        lab["text"] = num
    
def _op(opValue):
    global op
    global v1
    global opFlag
    opFlaf = True
    v1 = int(lab['text'])
    op = opValue
    
def compute():
    v2 = int(lab['text'])
    global op
    if op == 1:
        lab['text'] = v1 + v2  
    elif op ==2:
        lab['text'] = v1 - v2 
    elif op ==3:  
        lab['text'] = v1 * v2
    elif op ==4:   
        lab['text'] = v1 / v2   

window = Tk()
window.title("new test")
window.geometry("400x500+200+50")
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

lab = Label(window, text="0", justify=RIGHT,anchor=E, font=("Monaco", 26, "bold"), bg="#ccddee")
lab.grid(row=0, column=0, columnspan=4, sticky=EW)

btn7 = Button(window, text="7", font=("Monaco", 30, "bold"), command=lambda:_chan('7'))
btn7.grid(row=1, column=0, sticky=NSEW)
btn8 = Button(window, text="8", font=("Monaco", 30, "bold"),command=lambda:_chan('8'))
btn8.grid(row=1, column=1, sticky=NSEW)
btn9 = Button(window, text="9", font=("Monaco", 30, "bold"), command=lambda:_chan('9'))
btn9.grid(row=1, column=2, sticky=NSEW)

btn4 = Button(window, text="4", font=("Monaco", 30, "bold"), command=lambda:_chan('4'))
btn4.grid(row=2, column=0, sticky=NSEW)
btn5 = Button(window, text="5", font=("Monaco", 30, "bold"), command=lambda:_chan('5'))
btn5.grid(row=2, column=1, sticky=NSEW)
btn6 = Button(window, text="6", font=("Monaco", 30, "bold"), command=lambda:_chan('6'))
btn6.grid(row=2, column=2, sticky=NSEW)

btn1 = Button(window, text="1", font=("Monaco", 30, "bold"), command=lambda:_chan('1'))
btn1.grid(row=3, column=0, sticky=NSEW)
btn2 = Button(window, text="2", font=("Monaco", 30, "bold"), command=lambda:_chan('2'))
btn2.grid(row=3, column=1, sticky=NSEW)
btn3 = Button(window, text="3", font=("Monaco", 30, "bold"), command=lambda:_chan('3'))
btn3.grid(row=3, column=2, sticky=NSEW)

btn0 = Button(window, text="0", font=("Monaco", 30, "bold"), command=lambda:_chan('0'))
btn0.grid(row=4, column=0, sticky=NSEW)
btnpoint = Button(window, text=".", font=("Monaco", 30, "bold"), command=lambda:_chan('.'))
btnpoint.grid(row=4, column=1, sticky=NSEW)
btnclear = Button(window, text="c", font=("Monaco", 30, "bold"), command=lambda:_chan(' '))
btnclear.grid(row=4, column=2, sticky=NSEW)

btnmult = Button(window, text="*", font=("Monaco", 30, "bold"), command=lambda:compute('3'))
btnmult.grid(row=1, column=3, sticky=NSEW)
btnexcept = Button(window, text="/", font=("Monaco", 30, "bold"), command=lambda: compute('4'))
btnexcept.grid(row=2, column=3, sticky=NSEW)
btnplus = Button(window, text="+", font=("Monaco", 30, "bold"), command=lambda: compute('1'))
btnplus.grid(row=3, column=3, sticky=NSEW)
btnless = Button(window, text="-", font=("Monaco", 30, "bold"), command=lambda: compute('2'))
btnless.grid(row=4, column=3, sticky=NSEW)


window.mainloop()