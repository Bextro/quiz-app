from tkinter import *
import os
from Random.level1_screen import level1
from Random.level2_screen import level2


def main_login_screen():
    global main_login_screen, login_button, register_button, log_reg_bet_label, login_up_label, reg_down_label
    main_login_screen = Tk()
    main_login_screen.geometry('600x500')
    main_login_screen.title('Login screen')
    login_up_label = Label(text="")
    login_up_label.pack()
    login_button = Button(text="|LOGIN|", height="2", width="30", command=login)
    login_button.pack()
    log_reg_bet_label = Label(text="")
    log_reg_bet_label.pack()
    register_button = Button(text="|REGISTER|", height="2", width="30", command=register)
    register_button.pack()
    reg_down_label = Label(text="")
    reg_down_label.pack()

    main_login_screen.mainloop()


def level_screen():
    # global level_screen
    # level_screen = Tk()
    # level_screen.geometry('600x500')
    # level_screen.title('Loggedin screen')
    Label(text="Welcome {} !!!".format(username1), font=("calibri", 28)).pack()
    # scrollbar = Scrollbar(main_login_screen)
    # scrollbar.pack(side=RIGHT, fill=Y)
    back_button = Button(text="|BACK|", height="1", width="15")  # ,command=back_to_main_screen)
    back_button.pack(anchor="w", side="top")
    level_1_button = Button(text="|LEVEL 1|", height="2", width="30", command=lvl1)
    level_1_button.pack()
    Label(text="").pack()
    level_2_button = Button(text="|LEVEL 2|", height="2", width="30", command=lvl2)
    level_2_button.pack()
    Label(text="").pack()


def lvl1():
    main_login_screen.destroy()
    level1()


def lvl2():
    main_login_screen.destroy()
    level2()


# def back_to_main_screen():
# level_screen.destroy()
# main_login_screen()


def register():
    global register_screen
    register_screen = Toplevel(main_login_screen)
    register_screen.title("Register")
    register_screen.geometry("600x500")

    global username
    global password
    global firstname
    global lastname
    global id
    global contactno
    global city
    global state
    global username_entry
    global password_entry
    global firstname_entry
    global lastname_entry
    global id_entry
    global contactno_entry
    global city_entry
    global state_entry

    username = StringVar()
    password = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    id = StringVar()
    contactno = StringVar()
    city = StringVar()
    state = StringVar()

    Label(register_screen, text="Please enter details below", bg="yellow").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username : ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password : ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    firstname_lable = Label(register_screen, text="FirstName : ")
    firstname_lable.pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()

    lastname_lable = Label(register_screen, text="LastName : ")
    lastname_lable.pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()

    id_lable = Label(register_screen, text="ID : ")
    id_lable.pack()
    id_entry = Entry(register_screen, textvariable=id)
    id_entry.pack()

    contactno_lable = Label(register_screen, text="ContactNo : ")
    contactno_lable.pack()
    contactno_entry = Entry(register_screen, textvariable=contactno)
    contactno_entry.pack()

    city_lable = Label(register_screen, text="City : ")
    city_lable.pack()
    city_entry = Entry(register_screen, textvariable=city)
    city_entry.pack()

    state_lable = Label(register_screen, text="State : ")
    state_lable.pack()
    state_entry = Entry(register_screen, textvariable=state)
    state_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="pink", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_login_screen)
    login_screen.title("Login")
    login_screen.geometry("600x500")
    Label(login_screen,
          text="If you have the login enter the login if u dont have the login press register button").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username : ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password : ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    id_info = id.get()
    contactno_info = contactno.get()
    city_info = city.get()
    state_info = state.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(firstname_info + "\n")
    file.write(lastname_info + "\n")
    file.write(id_info + "\n")
    file.write(contactno_info + "\n")
    file.write(city_info + "\n")
    file.write(state_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    register_screen.after(3000, comander)

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_sucess():
    login_screen.destroy()
    register_button.pack_forget()
    login_button.pack_forget()
    login_up_label.pack_forget()
    log_reg_bet_label.pack_forget()
    reg_down_label.pack_forget()
    # main_login_screen.destroy()
    level_screen()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def comander():
    register_screen.destroy
