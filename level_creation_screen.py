from tkinter import *
import os

def level_creation():
    global correct_answer_lable, level_creation_screen, question, answer1, answer2, answer3, answer4, correct_answer, level_name, \
        level_name_entry, question_entry, answer1_entry, answer2_entry, answer3_entry, answer4_entry, correct_answer_entry
    level_creation_screen = Tk()
    level_creation_screen.title("Create new level")
    level_creation_screen.geometry("600x500")

    level_name = StringVar()
    question = StringVar()
    answer1 = StringVar()
    answer2 = StringVar()
    answer3 = StringVar()
    answer4 = StringVar()
    correct_answer = StringVar()

    Label(level_creation_screen, text="Please enter details below", bg="#FFD700").pack()
    Label(level_creation_screen, text="").pack()
    level_name_lable = Label(level_creation_screen, text="Level Name : ")
    level_name_lable.pack()
    level_name_entry = Entry(level_creation_screen, textvariable=level_name)
    level_name_entry.pack()

    question_lable = Label(level_creation_screen, text="Question : ")
    question_lable.pack()
    question_entry = Entry(level_creation_screen, textvariable=question)
    question_entry.pack()

    answer1_lable = Label(level_creation_screen, text="Answer 2 (0): ")
    answer1_lable.pack()
    answer1_entry = Entry(level_creation_screen, textvariable=answer1)
    answer1_entry.pack()

    answer2_lable = Label(level_creation_screen, text="Answer 2 (1): ")
    answer2_lable.pack()
    answer2_entry = Entry(level_creation_screen, textvariable=answer2)
    answer2_entry.pack()

    answer3_lable = Label(level_creation_screen, text="Answer 3 (2): ")
    answer3_lable.pack()
    answer3_entry = Entry(level_creation_screen, textvariable=answer3)
    answer3_entry.pack()

    answer4_lable = Label(level_creation_screen, text="Answer 4 (3) : ")
    answer4_lable.pack()
    answer4_entry = Entry(level_creation_screen, textvariable=answer4)
    answer4_entry.pack()

    correct_answer_lable = Label(level_creation_screen, text="Correct Answer : ")
    correct_answer_lable.pack()
    correct_answer_entry = Entry(level_creation_screen, textvariable=correct_answer)
    correct_answer_entry.pack()

    Label(level_creation_screen, text="").pack()
    Button(level_creation_screen, text="+", width=10, height=1, bg="#4169E1", command=create_level_questions).pack()
    level_creation_screen.mainloop()


def create_level_questions():
    level_name_info = level_name.get()
    question_info = question.get()
    answer1_info = answer1.get()
    answer2_info = answer2.get()
    answer3_info = answer3.get()
    answer4_info = answer4.get()
    correct_answer_info = correct_answer.get()

    file = open('{}.txt'.format(level_name_info), "w")
    file.write(question_info + "\n")
    file.write(answer1_info + "\n")
    file.write(answer2_info + "\n")
    file.write(answer3_info + "\n")
    file.write(answer4_info + "\n")
    file.write(correct_answer_info)

    file.close()

    level_name_entry.delete(0, END)
    question_entry.delete(0, END)
    answer1_entry.delete(0, END)
    answer2_entry.delete(0, END)
    answer3_entry.delete(0, END)
    answer4_entry.delete(0, END)
    correct_answer_entry.delete(0, END)

    Label(level_creation_screen, text="SAVED", fg="green", font=("calibri", 11)).pack()
    level_creation_screen.after(3000, destroy_level_creation_screen)


def destroy_level_creation_screen():
    level_creation_screen.destroy()

def level_verify():
    global level_name_entry
    level_name = level_name_entry.get()
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
