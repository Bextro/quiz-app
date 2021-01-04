from tkinter import *
import os, os.path
from functools import partial


def create_main_login_screen():
    global main_login_screen, login_button, register_button, log_reg_bet_label, login_up_label, reg_down_label
    main_login_screen = Tk()
    center_window(main_login_screen)
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
    register_screen.after(3000, destroy_reg_screen_and_open_log)


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
            login_success()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_success():
    login_screen.destroy()
    register_button.pack_forget()
    login_button.pack_forget()
    login_up_label.pack_forget()
    log_reg_bet_label.pack_forget()
    reg_down_label.pack_forget()
    show_level_screen()


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


def destroy_reg_screen_and_open_log():
    register_screen.destroy()
    login()


def show_level_screen():
    path = "C://Users/user/PycharmProjects/pythonProject2/Levels/"
    levels_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print(levels_count)
    for level in range(1, levels_count + 1):
        button = Button(text='{}'.format(level), command=partial(show_level_questions, level))
        button.pack()


def show_level_questions(level_number):
    filename = 'Level{}.txt'.format(level_number)
    path = "C://Users/user/PycharmProjects/pythonProject2/Levels/"
    file = open(path + filename, 'r')
    line = file.readline()
    main_login_screen.destroy()
    questions_count = 0
    while line != "":
        questions_count += 1
        question = line
        print(question)
        answers = []
        for i in range(4):
            answers.append(file.readline())
        print(answers)
        correct_answer = file.readline()
        print(correct_answer)
        line = file.readline()

        show_level_question(question, answers, int(correct_answer))
    file.close()


def show_level_question(question, answers, correct_answer):
    print('show_level_question')
    new_window = Tk()
    center_window(new_window)
    Label(new_window, text=question).pack()

    buttons = []
    for i in range(0, 4):
        print('created new button')
        button = Button(new_window, text=answers[i],
                        command=partial(check_answer, i,
                                        correct_answer, new_window)).pack()
        buttons.append(button)
    new_window.mainloop()
    return new_window


def check_answer(user_answer, correct_answer, question_window):
    if user_answer == correct_answer:
        label = Label(question_window, text='Your answer is correct').pack()
    else:
        label = Label(question_window, text='Your answer is wrong').pack()
    question_window.destroy()


def center_window(window, width= 600, height=500):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

# 1. 1 saat
# muellimin suallari elave etmek uchun pencere yaradirsan
# her entry novu uchun label olmalidir
# create new level
# 1. sual (entry)
# 2. variantlari doldurur (entryler)
# 3. duzgun suali qeyd edir (entry)
# 4. yadda saxla
# 5. Add button