from tkinter import *
#from tkinter import messagebox
import random,string
import pyperclip

root= Tk()
C = Canvas(root,height=200, width=350)
filename = PhotoImage(file="C:\\Users\\lenovo\\Documents\\Images\\back.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry("400x450")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

# heading
#heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Python & Tkinter Project', font='arial 15 bold').pack(side=BOTTOM)

###select password length

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack(pady=25)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=18).pack(pady=0)

#####define function

pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


###button

Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=20)

Entry(root, textvariable=pass_str).pack(pady=10)


########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text="Didn't like it? Retry!", command=Generator).pack(pady=2)

# loop to run program
C.pack()
root.mainloop()



