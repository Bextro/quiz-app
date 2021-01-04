from tkinter import *

from ProjectX.login_screen import create_main_login_screen, center_window


def coco():
    main_screen.destroy()
    create_main_login_screen()

main_screen = Tk()
center_window(main_screen)
main_screen.geometry("300x250")
main_screen.title("Quiz app")
main_label = Label(text="Want to start ?", bg="green", width="300", height="2", font=("Calibri", 13))
main_label.pack()

login_screen_button = Button(text="Start", height="2", width="30", command=coco)
login_screen_button.pack()

main_screen.mainloop()
