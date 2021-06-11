from tkinter import *

window = Tk()
window.title("Label demo")
window.geometry("500x400+100+50")
lab = Label(window,
            text = "The THE report announced AU is ranked among the list of high-impactuniversities in the world, No. 11 in Taiwan.",
            anchor = "nw",       # 參數se也可以用大寫,使用大寫時不需要雙引號
            width = 25,
            height = 20,
            wraplength = 120,    # wraplength屬性(自動換行,單位像素點)
            justify = "left",     #  justify 屬性 (文字靠邊 RIGHT)
            background = "#ccffdd",
            foreground = "#0000ff")
lab.pack()
window.mainloop()