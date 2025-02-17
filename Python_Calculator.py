import tkinter as tk
class Calculator:
    def __init__(self,master):
        self.master=master
        master.title(" Python Calculator")

        #Create the Entry Field
        self.entry = tk.Entry(master, width=40, justify='right',font=('Arial', 16))
        self.entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

        #Create the Buttons
        self.create_button("7",1,0)
        self.create_button("8",1,1)
        self.create_button("9",1,2)
        self.create_button("4",2,0)
        self.create_button("5",2,1)
        self.create_button("6",2,2)
        self.create_button("1",3,0)
        self.create_button("2",3,1)
        self.create_button("3",3,2)
        self.create_button("0",4,1)
        self.create_button("=",4,2)

        self.create_button("+",1,3)
        self.create_button("-",2,3)
        self.create_button("*",3,3)
        self.create_button("/",4,3)

        self.create_button("C",4,0)
        

    def create_button(self,text,row,column):
        button = tk.Button(self.master,text=text,width=10,height=2,font=("Arial",16), command=lambda: self.button_click(text))    
        button.grid(row=row,column=column,padx=5,pady=5)

    def button_click(self,text):
        if text == "=":
            try:
                result = str(eval(self.entry.get()))   
                self.entry.delete(0,tk.END)
                self.entry.insert(0,result)
            except:
                self.entry.delete(0,tk.END)    
                self.entry.insert(0,"Error")
        elif text == "C":
            self.entry.delete(0, tk.END)      
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()                   