from tkinter import *

root=Tk()
root.geometry('360x600')
root.resizable(False,False)
root.title('calculator')
root.config(background='#227C70')

def calculate():
    try:

        price=float(num1.get())
        print(price)

        discount=float(num2.get())
        result=price-(price*(discount/100))
        label_rasult.config(text=result)
    except ValueError:
        label_rasult.config(text='Entry First')





Label(root,text='Discount Calculator',fg='#FFB100',bg='#227C70',font=('arial',20,'bold','italic')).place(x=55,y=130)

Label(root,text='Original price',bd=0,bg='#227C70',font=('bold',11),fg='#040303').place(x=40,y=200)
Label(root,text='Discount (%)',bd=0,bg='#227C70',font=('bold',11),fg='#040303').place(x=40,y=250)
Label(root,text='Final price',bd=0,bg='#227C70',font=('bold',11),fg='#040303').place(x=40,y=300)

num1=Entry(root,bg='#E84545',bd=0,foreground='white',font=('arial',11,'bold',))
num1.place(x=130,y=200)

num2=Entry(root,bg='#E84545',bd=0,fg='white',font=('arial',11,'bold',))
num2.place(x=130,y=250)

Button(root,text='Calculate',background='yellow',pady=7,bd=0,cursor='hand2',command=calculate).place(x=175,y=340)
label_rasult=Label(root,width=17,height=1,bg='black',foreground='white',font=('arial',11,'bold',))
label_rasult.place(x=130,y=300)







root.mainloop()
