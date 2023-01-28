#Calculator Project
from tkinter import*
expression=""

class Calculator:   
    def __init__(self,window):
        self.window=window
        self.window.title("Grocery Calculator")
        self.window.geometry("500x700+0+0")

        


        def backspc():
           
            global expression
            print(expression)
            expression=[*expression]
            n=len(expression)
            print(n)
            if n==0:
                clear()
            else:
                print(expression.pop(n-1))
                stored_value.set(expression)
                expression="".join(expression)
            print(type(expression))

            


        
        def click(item):
            global expression
            expression=expression+str(item)
            stored_value.set(expression)

            
        def clear():
            global expression
            expression=""
            stored_value.set("")
            
        def equal():
            global expression
            stored=str(eval(expression))
            stored_value.set(stored)
            expression=""

        
        stored_value=StringVar()


        frame=Frame(window,bg="grey",height=700,width="500",highlightbackground="black",highlightthickness=5)
        frame.place(x=0,y=0)

        frame1=Frame(frame,bg="white",height=80,width="460",highlightbackground="black",highlightthickness=4)
        frame1.place(x=15,y=40)

        label=Label(frame,text="<<<<<<<CASIO>>>>>>>",bg="grey",font=("ALGERIAN",22,"bold"))
        label.place(x=100,y=0)

        entry=Entry(frame,width=26,font=("Algerian",22),justify=RIGHT,bg="white",bd=0,insertbackground='red',insertofftime=30,textvariable=stored_value)
        entry.place(x=23,y=80)


        #row one button

        button=Button(frame,bg="white",text="7",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("7"),activebackground="grey",activeforeground="green")
        button.place(x=15,y=160)

        button1=Button(frame,bg="white",text="8",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("8"))
        button1.place(x=135,y=160)


        button2=Button(frame,bg="white",text="9",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("9"))
        button2.place(x=260,y=160)


        button3=Button(frame,bg="white",text="%",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("/"))
        button3.place(x=380,y=160)


        #row two button

        button=Button(frame,bg="white",text="4",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("4"))
        button.place(x=15,y=260)

        button1=Button(frame,bg="white",text="5",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("5"))
        button1.place(x=135,y=260)


        button2=Button(frame,bg="white",text="6",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("6"))
        button2.place(x=260,y=260)


        button3=Button(frame,bg="white",text="x",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("*"))
        button3.place(x=380,y=260)

        #row three button

        button=Button(frame,bg="white",text="1",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("1"))
        button.place(x=15,y=360)

        button1=Button(frame,bg="white",text="2",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("2"))
        button1.place(x=135,y=360)


        button2=Button(frame,bg="white",text="3",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("3"))
        button2.place(x=260,y=360)


        button3=Button(frame,bg="white",text="-",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("-"))
        button3.place(x=380,y=360)


        #row four button

        button=Button(frame,bg="white",text="0",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("0"))
        button.place(x=15,y=460)

        button1=Button(frame,bg="white",text=".",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("."))
        button1.place(x=135,y=460)


        button2=Button(frame,bg="white",text="+",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:click("+"))
        button2.place(x=260,y=460)

        button3=Button(frame,bg="white",text="=",bd=4,font=("Cambria",22),relief=GROOVE,width=5,height=1,command=lambda:equal())
        button3.place(x=380,y=460)


        #row four button
        button=Button(frame,bg="green",text="C",bd=4,font=("Cambria",22),relief=GROOVE,width=15,height=1,command=lambda:clear())
        button.place(x=45,y=550)

        button=Button(frame,bg="cyan",text="Bkspc",bd=20,font=("Cambria",10),relief=GROOVE,width=6,height=1,command=lambda:backspc())
        button.place(x=380,y=550)

        



if __name__=="__main__":
    window=Tk()
    obj=Calculator(window)
    window.mainloop()
