import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
my_w = ttk.Window(themename="lumen")
my_w.geometry("400x200")  # width and height

style = ttk.Style()
style.configure('TButton', background='green', foreground='white', 
        font=('Helvetica', 20))
style.configure('TLabel', background='blue', foreground='white',
     font=('Helvetica', 24))
style.configure('custom1.TLabel', background='gray', foreground='green')

cd = ColorChooserDialog()

def my_show():
    cd.show()
    colors=cd.result
    l1.configure(text=colors.hex) # display hex code 
    l2.configure(text=colors.rgb) # RGB values 
    style.configure('TButton', background=colors.hex, foreground='white', 
        font=('Helvetica', 20,'underline'))
    style.configure('TLabel', background=colors.hex, foreground='white')
    style.configure('custom1.TLabel', background='lightyellow',
		foreground=colors.hex)
b1=ttk.Button(my_w,text='Select Colour',bootstyle='warning', 
        style='custom.TButton',command=lambda:my_show())
b1.grid(row=0,column=0,padx=10,pady=20)
l1=ttk.Label(my_w,text='Hex here',style='custom1.TLabel')
l1.grid(row=1,column=0,padx=10)
l2=ttk.Label(my_w,text='RGB here',style='TLabel')
l2.grid(row=1,column=1,padx=10)
my_w.mainloop()
