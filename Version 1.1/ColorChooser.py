import ttkbootstrap as ttk
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

# Create the main application window
my_w = ttk.Window(themename="flatly")
my_w.title("Color Chooser")
my_w.geometry("400x200")

# Set a custom window icon
my_w.iconbitmap(r"..\Images\colorchooserlogo.ico")  # Replace "path/to/your/icon.ico" with the actual path to your icon file

# Configure the styles for buttons and labels
style = ttk.Style()
style.configure('TButton', background='#007BFF', foreground='white', font=('Helvetica', 20))
style.configure('TLabel', background='#E9ECEF', foreground='#343A40', font=('Helvetica', 24))
style.configure('custom1.TLabel', background='#6C757D', foreground='#007BFF')

# Create a ColorChooserDialog instance
cd = ColorChooserDialog()

# Function to show the color chooser dialog and update labels and styles
def my_show():
    colors = cd.show()
    if colors is not None:
        style.configure('TButton', background=colors.hex, foreground='white', font=('Helvetica', 20, 'underline'))
        style.configure('TLabel', background=colors.hex, foreground='white')
        style.configure('custom1.TLabel', background='#6C757D', foreground=colors.hex)

# Create a frame to center the button
frame = ttk.Frame(my_w)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create a "Select Color" button
b1 = ttk.Button(frame, text='Select Color', bootstyle='primary', style='custom.TButton', command=my_show)
b1.pack()

# Start the main application loop
my_w.mainloop()
