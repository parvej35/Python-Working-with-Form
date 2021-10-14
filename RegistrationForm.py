from tkinter import *


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open("files/data_file.txt", "a+")
    file.write(username_info + "#" + password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Completed", fg="green", font=("calibri", 14)).pack()


def register():
    global screen1

    screen1 = Toplevel(SCREEN)
    screen1.title("Registration")
    screen1.geometry("500x500")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    # Label(screen1, text="Please Enter ", fg="red").pack()

    Label(screen1, text="Username: ", font=("calibri", 14)).pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Password: ", font=("calibri", 14)).pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()

    Button(screen1, text="Register", width=10, height=1, command=register_user, font=("calibri", 14)).pack()


def login():
    print("Login......")


def main_screen():
    global SCREEN

    SCREEN = Tk()
    SCREEN.geometry("500x500")
    SCREEN.title("Python Registration Form")

    Label(text="Python Registration Form For Learning", fg="black", bg="gray", width="500", height="1", font=("calibri", 14)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login, font=("calibri", 14)).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register, font=("calibri", 14)).pack()

    # heading = Label(text="Python Registration Form For Learning", fg="black", bg="gray", width="500", 
    # height="3").pack() 

    # Label(text="Username: ").place(x=15, y=50)
    # Label(text="Password: ").place(x=15, y=120)

    SCREEN.mainloop()


if __name__ == "__main__":
    main_screen()
