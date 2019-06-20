from tkinter import *
from tkinter.messagebox import *
from utils import *
from StudentPage import StudentPage
from TeacherPage import TeacherPage
from AdminPage import AdminPage


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        center_window(self.root, 500, 309)
        self.username = StringVar()
        self.password = StringVar()
        self.usertype = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='I AM ', font=("Arial", 16)).grid(row=1, stick=W, pady=10)

        user_type = ['student', 'teacher', 'admin']
        v = StringVar()
        v.set('student')
        for i in range(3):
            Radiobutton(self.page, variable=self.usertype, text=user_type[i], value=user_type[i],
                        font=("Arial", 12)).grid(row=2, column=i, pady=10)

        Label(self.page, text='ID: ', font=("Arial", 12)).grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.username, font=("Arial", 12)).grid(row=3, column=1, stick=E)
        Label(self.page, text='Password: ', font=("Arial", 12)).grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*', font=("Arial", 12)).grid(row=4, column=1, stick=E)
        Button(self.page, text='Sign in', command=self.login_check, font=("Arial", 12)).grid(row=5, stick=W, pady=10)
        Button(self.page, text='Exit', command=self.page.quit, font=("Arial", 12)).grid(row=5, column=1, stick=E)

    def login_check(self):
        print(self.usertype.get())
        type = self.usertype.get()
        name = self.username.get()
        secret = self.password.get()
        s = 'select * from user where user.username="'+name+'' \
            '" and user.password="'+secret+'' \
            '" and user.usertype="'+type+'"'

        db_fetch = sql_conn(s)

        if len(db_fetch) != 0:
            self.page.destroy()
            if type == 'student':
                StudentPage(self.root)
            elif type == 'teacher':
                TeacherPage(self.root)
            elif type == 'admin':
                AdminPage(self.root)
        else:
            showinfo(title='Login error', message='ID or password incorrect')


if __name__ == "__main__":
    root = Tk()
    root.title('Management Information System')
    LoginPage(root)
    root.mainloop()
