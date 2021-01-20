from tkinter import * 

root = Tk()
root.title("joy's calculator")

e =  Entry(root,width= 35, borderwidth=5,bg ="grey",fg ="black")
e.grid(row=0,column = 0, columnspan = 3 ,padx = 10 , pady =10)

#e.insert(0,"enter your name")

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)

    e.insert(0,str(current) +str(number)) 

def button_clear():
    e.delete(0,END)



def button_equal():
    secnum = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,fstnum + int(secnum))

    if math == "subtraction":
        e.insert(0,fstnum - int(secnum))

    if math == "multiplication":
        e.insert(0,fstnum * int(secnum))

    if math == "division":
        e.insert(0,fstnum / int(secnum))

def button_add():
    fnumber = e.get()
    global fstnum
    global math 
    math = "addition"
    fstnum = int(fnumber)
    e.delete(0,END)
 

def button_sub():
    fnumber = e.get()
    global fstnum
    global math 
    math = "subtraction"
    fstnum = int(fnumber)
    e.delete(0,END)

def button_mul():
    fnumber = e.get()
    global fstnum
    global math 
    math = "multiplication"
    fstnum = int(fnumber)
    e.delete(0,END)

def button_div():
    fnumber = e.get()
    global fstnum
    global math 
    math = "division"
    fstnum = int(fnumber)
    e.delete(0,END)


btn1 = Button(root,text= "1",padx =40,pady=20, command= lambda: button_click(1) )
btn2 = Button(root,text= "2",padx =40,pady=20, command= lambda: button_click(2) )
btn3 = Button(root,text= "3",padx =40,pady=20, command= lambda: button_click(3))

btn4 = Button(root,text= "4",padx =40,pady=20, command= lambda: button_click(4))
btn5 = Button(root,text= "5",padx =40,pady=20, command= lambda: button_click(5))
btn6 = Button(root,text= "6",padx =40,pady=20, command= lambda: button_click(6))

btn7 = Button(root,text= "7",padx =40,pady=20, command= lambda: button_click(7))
btn8 = Button(root,text= "8",padx =40,pady=20, command= lambda: button_click(8) )
btn9 = Button(root,text= "9",padx =40,pady=20, command= lambda: button_click(9) )
btn0 = Button(root,text= "0",padx =40,pady=20, command= lambda: button_click(0) )

btn_add = Button(root,text= "+",padx =39,pady=20, command= button_add )
btn_sub = Button(root,text= "-",padx =41,pady=20, command= button_sub )
btn_mul = Button(root,text= "*",padx =40,pady=20, command= button_mul )
btn_div = Button(root,text= "/",padx =41,pady=20, command= button_div )


btn_equal = Button(root,text= "=",padx =91,pady=20, command= button_equal )
btn_clear= Button(root,text= "clear",padx =79,pady=20, command= button_clear)

#putting the buttons on the screen

btn1.grid(row= 3, column=0)
btn2.grid(row= 3, column=1)
btn3.grid(row=3 , column=2)

btn4.grid(row=2 , column=0)
btn5.grid(row=2 , column=1)
btn6.grid(row= 2, column=2)

btn7.grid(row=1 , column=0)
btn8.grid(row= 1, column=1)
btn9.grid(row= 1, column=2)

btn0.grid(row= 4, column=0)
btn_add.grid(row=5,column=0)
btn_equal.grid(row=5,column=1,columnspan= 2)
btn_clear.grid(row=4,column=1,columnspan= 2)

btn_sub.grid(row=6,column=0)
btn_mul.grid(row=6,column=1)
btn_div.grid(row=6,column=2)



root.mainloop()
