from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
from utils import *


class TeacherPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        center_window(self.root, 1000, 618)
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.home_page()
        menubar = Menu(self.root)
        menubar.add_command(label='Home', command=self.home_page)
        menubar.add_command(label='Chosen courses', command=self.courses_page)
        menubar.add_command(label='Scores', command=self.scores_page)
        self.root['menu'] = menubar  # 设置菜单栏

    def home_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        # ID, Name, Sex, Entrance Age, Entrance Year, Class, Grade [7]
        info_head = ['ID', 'Name', 'Sex', 'Entrance Age', 'Entrance Year', 'Class', 'Grade']
        student_info = ['000001', 'Tom Jack', 'Male', '18', '2008', 'Class 1', 'Grade']
        # student_info[6] = currentYear - Entrance Year

        Label(self.page, text='Hello, Student {}!'.format(student_info[1]), font=("Arial", 16)).grid(row=1, stick=W,
                                                                                                     pady=10)
        for i in range(7):
            Label(self.page, text=info_head[i] + ': ', font=("Arial", 12)).grid(row=i + 2, stick=W, pady=10)
            Label(self.page, text=student_info[i], font=("Arial", 12)).grid(row=i + 2, column=1, stick=W, pady=10)

        self.page.pack()

    def courses_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Course Name', 'Teacher Name', 'Credit', 'Course Grade', 'Canceled Year')
        table = Treeview(self.page, height=14, show="headings", columns=columns)
        for i in range(5):
            table.column(columns[i], width=150, anchor='center')
            table.heading(columns[i], text=columns[i])

        table.grid(row=1, sticky=W + E)
        # course_data()
        self.page.pack()

    def scores_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Course Name', 'Teacher Name', 'Credit', 'Course Grade', 'Chosen Year', 'Score')
        table = Treeview(self.page, height=14, show="headings", columns=columns)
        for i in range(6):
            table.column(columns[i], width=150, anchor='center')
            table.heading(columns[i], text=columns[i])

        table.grid(row=1, sticky=W + E)
        # scores_data()

        Label(self.page, text='Average Score: ', font=("Arial", 12)).grid(row=2, stick=E, pady=10)
        Label(self.page, text='{}'.format('ave'), font=("Arial", 12)).grid(row=2, column=1, stick=W, pady=10)
        self.page.pack()


if __name__ == "__main__":
    root = Tk()
    root.title('Management Information System')
    TeacherPage(root)
    root.mainloop()
