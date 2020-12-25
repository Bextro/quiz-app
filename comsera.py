import os
from functools import partial
from tkinter import *


def show_level_window():
    global level_name_error_label, level_creation_screen, level_name_entry, correct_answer_entry
    level_creation_screen = Tk()
    level_creation_screen.title("Level creation")
    level_creation_screen.geometry("600x500")

    Label(level_creation_screen, text="Please enter details below", bg="#FFD700").pack()
    Label(level_creation_screen, text="").pack()
    level_name_label = Label(text="Level Name : ")
    level_name_label.pack()
    level_name_entry = Entry()
    level_name_entry.pack()
    level_name_error_label = Label('')
    level_name_error_label.pack()
    Button(level_creation_screen, text="Create", width=10, height=1, bg="#4169E1",
           command=partial(create_new_level, level_name_error_label)).pack()
    level_creation_screen.mainloop()


def create_new_level(level_name_error_label):
    level_name_entry.delete(0, END)
    level_name_entry.delete(0, END)

    file_names = os.listdir("C://Users/user/PycharmProjects/pythonProject2/Levels")
    print(file_names)
    for file_name in file_names:
        if file_name == level_name_entry.get() + '.txt':
            print(level_name_error_label)
            level_name_error_label.configure(text='level already exists, please rename your level')
            return

    enter_level_questions(level_name_entry.get())


def enter_level_questions(qua_name):
    global question_entry, answer_entry, correct_answer_entry
    question_label = Label(text='Enter the question:')
    question_label.pack()
    question_entry = Entry()
    question_entry.pack()
    answer_entries = []
    for i in range(0, 4):
        answer_label = Label(level_creation_screen, text="Answer {}: ".format(i))
        answer_label.pack()
        answer_entry = Entry(level_creation_screen)
        answer_entry.pack()
        answer_entries.append(answer_entry)
    correct_answer_label = Label(level_creation_screen, text="Correct answer:")
    correct_answer_label.pack()
    correct_answer_entry = Entry(level_creation_screen)
    correct_answer_entry.pack()
    new_question_button = Button(text='+', command=partial(save_new_question,
                                                           question_entry.get(),
                                                           answer_entries,
                                                           correct_answer_entry.get()))
    new_question_button.pack()

def save_new_question(question, answers, correct_answer):
    file = open(level_name, "w")
    file.write(question + "\n")
    file.write(answers + "\n")
    file.write(correct_answer + "\n")
    # file.write(lastname_info + "\n")
    # file.write(id_info + "\n")
    # file.write(contactno_info + "\n")
    # file.write(city_info + "\n")
    # file.write(state_info)
    file.close()

    question_entry.delete(0, END)
    answer_entry.delete(0, END)
    correct_answer_entry.delete(0, END)

    Label(level_creation_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()



def level_verify():
    global level_name
    level_name = level_name_entry.get()
    level_name_entry.delete(0, END)

    list_of_files = os.listdir()
    if level_name in list_of_files:
        pass
    else:
        pass


show_level_window()