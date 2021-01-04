import os
import shutil
from functools import partial
from tkinter import *


def show_level_window():
    global level_name_error_label, level_creation_screen, level_name_entry, correct_answer_entry, level_name_label, info_label_gap, info_label, create_button
    level_creation_screen = Tk()
    level_creation_screen.title("Level creation")
    level_creation_screen.geometry("600x500")

    info_label = Label(level_creation_screen, text="Please enter details below", bg="#FFD700")
    info_label.pack()
    info_label_gap = Label(level_creation_screen, text='')
    info_label_gap.pack()
    level_name_label = Label(level_creation_screen, text="Level Name : ")
    level_name_label.pack()
    level_name_entry = Entry(level_creation_screen)
    level_name_entry.pack()
    level_name_error_label = Label(level_creation_screen, text='')
    level_name_error_label.pack()
    create_button = Button(level_creation_screen, text="Create", width=10, height=1, bg="#4169E1",
                           command=partial(create_new_level, level_name_error_label))
    create_button.pack()
    level_creation_screen.mainloop()


def create_new_level(level_name_error_label):
    level_name_entry.pack_forget()
    level_name_error_label.pack_forget()
    level_name_label.pack_forget()
    info_label.pack_forget()
    info_label_gap.pack_forget()
    create_button.pack_forget()
    file_names = os.listdir("C://Users/user/PycharmProjects/pythonProject2/Levels")
    for file_name in file_names:
        if file_name == level_name_entry.get() + '.txt':
            level_name_error_label.configure(text='level already exists, please rename your level')
            return

    enter_level_questions(level_name_entry.get())


def enter_level_questions(level_name):
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
        answer_entries.append(answer_entry.get())
    correct_answer_label = Label(level_creation_screen, text="Correct answer:")
    correct_answer_label.pack()
    correct_answer_entry = Entry(level_creation_screen)
    correct_answer_entry.pack()
    new_question_button = Button(text='+', command=partial(save_new_question,
                                                           level_name,
                                                           question_entry.get(),
                                                           answer_entries,
                                                           correct_answer_entry.get()))
    new_question_button.pack()


def save_new_question(level_name, question, answers, correct_answer):
    file = open('{}.txt'.format(level_name), "w")
    file.write(question + "\n")
    for i in range(0, len(answers)):
        file.write(answers[i] + "\n")
    file.write(correct_answer + "\n")
    file.close()

    question_entry.delete(0, END)
    answer_entry.delete(0, END)
    correct_answer_entry.delete(0, END)
    shutil.move("C://Users/user/PycharmProjects/pythonProject2/ProjectX/{}".format('{}.txt'.format(level_name)),
                "C://Users/user/PycharmProjects/pythonProject2/Levels")
    Label(level_creation_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


show_level_window()
