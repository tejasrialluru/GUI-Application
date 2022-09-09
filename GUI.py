from tkinter import *

window = Tk()
window.geometry("800x400")
window.title("Saffronic Packing Tool")       # adding title of the window
window.resizable(False, False)               # Making the window of fixed size

# Frame containing checkboxes

top_frame = Frame(window, height=400, width=200)                 
top_frame.pack(side=LEFT)
#Checkbox1
Button1 = Checkbutton(top_frame, text="Copy Source Images", font='sofia-pro 12 bold',
                      onvalue=1,
                      offvalue=0,
                        )
Button1.pack()

#checkbox2
Button2 = Checkbutton(top_frame, text="Copy Renders", font='sofia-pro 12 bold',
                      onvalue=1,
                      offvalue=0,
                      )
Button2.pack()

# frame containing the input label and entry

right_frame = Frame(window)
right_frame.pack(side=TOP, pady=20)
lbl1 = Label(right_frame, text="Input Path", fg='white', font='sofia-pro 12 bold', width=13)
lbl1.config(bg="#92D050")
lbl1.pack(side=LEFT, padx=10, pady=15)
input_entry = Entry(right_frame, font='calibre 10 normal', bd=1, width=60)
input_entry.pack(side=LEFT)

#frame containing the destination label and entry

right1_frame = Frame(window)
right1_frame.pack(side=TOP)
lbl2 = Label(right1_frame, text="Destination Path", fg='white', font='sofia-pro 12 bold', width=13)
lbl2.config(bg="#92D050")
lbl2.pack(side=LEFT, padx=10, pady=15)
destination_entry = Entry(right1_frame, font='calibre 10 normal', bd=1, width=60)
destination_entry.pack(side=LEFT)

#frame containing the ssubmit and quit buttons

bottom_frame = Frame(window)
bottom_frame.pack(side=TOP, pady=70)
btn1 = Button(bottom_frame, text='Submit', fg='black', font='sofia-pro 12 bold', width=16)
btn1.config(bg="#A9D08E")
btn1.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(bottom_frame, text='QUIT', fg='black', font='sofia-pro 12 bold', width=16)
btn2.config(bg="#F4B084")
btn2.pack(side=LEFT, padx=5, pady=5)

mainloop()
