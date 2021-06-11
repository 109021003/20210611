from tkinter import *


flag = True
    
def _setText(num):
    global flag
    if num == 0:
        if flag:
            btn0.config(text="o")
        else:
            btn0.config(text="x")
        btn0.config(state = DISABLED)
    elif num == 1:
        if flag:
            btn1.config(text="o")
        else:
            btn1.config(text="x")
        btn1.config(state = DISABLED)
    elif num == 2:
        if flag:
            btn2.config(text="o")
        else:
            btn2.config(text="x")
        btn2.config(state = DISABLED)
    elif num == 3:
        if flag:
            btn3.config(text="o")
        else:
            btn3.config(text="x")
        btn3.config(state = DISABLED)
    elif num == 4:
        if flag:
            btn4.config(text="o")
        else:
            btn4.config(text="x")
        btn4.config(state = DISABLED)
    elif num == 5:
        if flag:
            btn5.config(text="o")
        else:
            btn5.config(text="x")
        btn5.config(state = DISABLED)
    elif num == 6:
        if flag:
            btn6.config(text="o")
        else:
            btn6.config(text="x")
        btn6.config(state = DISABLED)
    elif num == 7:
        if flag:
            btn7.config(text="o")
        else:
            btn7.config(text="x") 
        btn7.config(state = DISABLED)
    elif num == 8:
        if flag:
            btn8.config(text="o")
        else:
            btn8.config(text="x")
        btn8.config(state = DISABLED)
    flag = not flag 

    if btn0.cget('text') == btn1.cget('text') and btn0.cget('text') == btn2.cget('text'):
        if btn0.cget('text') == "o":
            print("player 1 win!!")
        elif btn0.cget("text") == "x":
            print("player 2 win!!")
    if btn0.cget('text') == btn3.cget('text') and btn0.cget('text') == btn6.cget('text'):
        if btn0.cget('text') == "o":
            print("player 1 win!!")
        elif btn0.cget("text") == "x":
            print("player 2 win!!")
    if btn0.cget('text') == btn4.cget('text') and btn0.cget('text') == btn8.cget('text'):
        if btn0.cget('text') == "o":
            print("player 1 win!!")
        elif btn0.cget("text") == "x":
            print("player 2 win!!")
    if btn1.cget('text') == btn4.cget('text') and btn1.cget('text') == btn7.cget('text'):
        if btn1.cget('text') == "o":
            print("player 1 win!!")
        elif btn1.cget("text") == "x":
            print("player 2 win!!")
    if btn2.cget('text') == btn5.cget('text') and btn2.cget('text') == btn8.cget('text'):
        if btn2.cget('text') == "o":
            print("player 1 win!!")
        elif btn2.cget("text") == "x":
            print("player 2 win!!")
    if btn2.cget('text') == btn4.cget('text') and btn2.cget('text') == btn6.cget('text'):
        if btn2.cget('text') == "o":
            print("player 1 win!!")
        elif btn2.cget("text") == "x":
            print("player 2 win!!")
    if btn3.cget('text') == btn4.cget('text') and btn3.cget('text') == btn5.cget('text'):
        if btn3.cget('text') == "o":
            print("player 1 win!!")
        elif btn3.cget("text") == "x":
            print("player 2 win!!")
    if btn6.cget('text') == btn7.cget('text') and btn6.cget('text') == btn8.cget('text'):
        if btn6.cget('text') == "o":
            print("player 1 win!!")
        elif btn6.cget("text") == "x":
            print("player 2 win!!")






window = Tk()
window.title = "test"
window.geometry("400x400+200+100")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)


btn0 = Button(window, text="", command = lambda: _setText(0))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 = Button(window, text="",command = lambda: _setText(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(window, text="", command = lambda: _setText(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(window, text="", command = lambda: _setText(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(window, text="", command = lambda: _setText(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(window, text="", command = lambda: _setText(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(window, text="", command = lambda: _setText(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(window, text="", command = lambda: _setText(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(window, text="", command = lambda: _setText(8))
btn8.grid(row=2, column=2, sticky=NSEW)

window.mainloop()