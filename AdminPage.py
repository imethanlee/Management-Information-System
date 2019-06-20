from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
from utils import *


class AdminPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        center_window(self.root, 1000, 618)
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.home_page()
        menubar = Menu(self.root)
        menubar.add_command(label='Home', command=self.home_page)
        menubar.add_command(label='Students Info', command=self.students_page)
        menubar.add_command(label='Teachers Info', command=self.teachers_page)
        menubar.add_command(label='Choosing courses', command=self.choosing_page)
        menubar.add_command(label='Courses Info', command=self.courses_page)

        menubar.add_command(label='Query Students', command=self.query_student_page)
        menubar.add_command(label='Query Courses', command=self.query_course_page)
        menubar.add_command(label='Query Teachers', command=self.query_teacher_page)
        menubar.add_command(label='Query Score', command=self.query_score_page)
        self.root['menu'] = menubar  # 设置菜单栏

    def home_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='Hello, Admin ! ', font=("Arial", 24)).grid(row=1, stick=W, pady=10)
        for i in range(7):
            Label(self.page).grid(row=i + 2, stick=W)
        Watch(self.page).grid(row=9)
        self.page.pack()

    def students_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Student ID', 'Name', 'Password', 'Sex', 'Entrance Age', 'Entrance Year',
                   'Class', 'Grade', 'Drop Out')
        table = generate_table(self.page, 1, columns)

        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Student ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Button(query_frame, text='Search', command='updateFunction',
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        Button(query_frame, text='Delete', command='updateFunction',
               font=("Arial", 16)).grid(row=2, column=2, stick=W, pady=10)

        Label(query_frame).grid(row=3, stick=W)

        Button(query_frame, text='New', command='',
               font=("Arial", 16)).grid(row=5, column=1, stick=W, pady=10)
        Button(query_frame, text='Drop out', command='updateFunction',
               font=("Arial", 16)).grid(row=5, column=2, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def teachers_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Teacher ID', 'Teacher Name', 'Password', 'Course')
        table = generate_table(self.page, 1, columns)

        # course_data()
        self.page.pack()

    def courses_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Course Name', 'Teacher Name', 'Credit', 'Course Grade', 'Canceled Year')
        table = generate_table(self.page, 1, columns)

        # course_data()
        self.page.pack()

    def choosing_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Course Name', 'Teacher Name', 'Credit', 'Course Grade', 'Chosen Year', 'Score')
        table = generate_table(self.page, 1, columns)

        # scores_data()

        Label(self.page, text='Average Score: ', font=("Arial", 12)).grid(row=2, stick=E, pady=10)
        Label(self.page, text='{}'.format('ave'), font=("Arial", 12)).grid(row=2, column=1, stick=W, pady=10)
        self.page.pack()

    def query_student_page(self):  # 3\4
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        columns = ('Student ID', 'Name', 'Course ID', 'Course Name', 'Credit', 'Score')
        table = generate_table(self.page, 1, columns)
        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Student ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Course ID: ', font=("Arial", 16)).grid(row=1, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=1, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=1, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=1, column=3, stick=E + W, pady=10)

        Button(query_frame, text='Search', command='updateFunction',
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def query_course_page(self):  # 5 展示所有课程，可以没有学生信息
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        columns = ('Course ID', 'Course Name', 'Student ID', 'Student Name', 'Credit', 'Score')
        table = generate_table(self.page, 1, columns)
        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Course ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Button(query_frame, text='Search', command='updateFunction',
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def query_teacher_page(self):  # 6
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        columns = ('Teacher ID', 'Teacher Name', 'Course ID', 'Course Name', 'Credit', 'Score')
        table = generate_table(self.page, 1, columns)
        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Teacher ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Teacher Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Button(query_frame, text='Search', command='updateFunction',
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def query_score_page(self):  # 7
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        columns = ('Student ID', 'Student Name', 'Course ID', 'Course Name', 'Class', 'Score')
        table = generate_table(self.page, 1, columns)
        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Student ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Course ID: ', font=("Arial", 16)).grid(row=1, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=1, column=1, stick=E + W, pady=10)
        Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=1, column=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=1, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Class: ', font=("Arial", 16)).grid(row=2, stick=E + W, pady=10)
        Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=2, column=1, stick=E + W, pady=10)

        Button(query_frame, text='Search', command='updateFunction',
               font=("Arial", 16)).grid(row=3, column=1, stick=W, pady=10)

        Label(query_frame, text='Average Score: ', font=("Arial", 16)).grid(row=3, column=2, stick=E, pady=10)
        Label(query_frame, text='{}'.format('avg'), font=("Arial", 16)).grid(row=3, column=3, stick=W, pady=10)
        self.page.pack()

        # course_data()
        self.page.pack()


if __name__ == "__main__":
    root = Tk()
    root.title('Management Information System')
    AdminPage(root)
    root.mainloop()
