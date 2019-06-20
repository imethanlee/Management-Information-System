from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter.ttk import Treeview
from utils import *


class StudentPage(object):
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
        # get data from database
        sql = 'select * from student where student.studentID="'+GlobalVar.login_id+'"'
        db_fetch = sql_conn(sql)[0]
        print(db_fetch)

        # ID, Name, Sex, Entrance Age, Entrance Year, Class, Grade [7]
        info_head = ['ID', 'Name', 'Sex', 'Entrance Age', 'Entrance Year', 'Class', 'Grade']
        student_info = [db_fetch[0], db_fetch[1], db_fetch[2], db_fetch[3], db_fetch[4], db_fetch[5], 'Grade']
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

        # get data from database
        sql = 'select course.name, teacher.name, course.credit, course.grade, course.canceledYear from ' \
              'course, teacher, coursechoosing where coursechoosing.studentID="'+GlobalVar.login_id+'" and ' \
              'teacher.teacherID=coursechoosing.teacherID and course.courseID=coursechoosing.courseID'
        db_fetch = sql_conn(sql)

        columns = ('Course Name', 'Teacher Name', 'Credit', 'Course Grade', 'Canceled Year')
        table = generate_table(self.page, 1, columns)
        # course_data()
        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                        db_fetch[i][2], db_fetch[i][3],
                                        db_fetch[i][4]))
        self.page.pack()

    def scores_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        # get data from database
        sql = 'select course.name, teacher.name, course.credit, course.grade, coursechoosing.chosenYear, coursechoosing.score from ' \
              'course, teacher, coursechoosing where coursechoosing.studentID="'+GlobalVar.login_id+'" and ' \
              'teacher.teacherID=coursechoosing.teacherID and course.courseID=coursechoosing.courseID'
        db_fetch = sql_conn(sql)

        columns = ('Course Name', 'Teacher Name', 'Credit', 'Course Grade', 'Chosen Year', 'Score')
        table = generate_table(self.page, 1, columns)
        # scores_data()
        avg = 0.0
        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                        db_fetch[i][2], db_fetch[i][3],
                                        db_fetch[i][4], db_fetch[i][5]))
            avg += db_fetch[i][5] / len(db_fetch)

        Label(self.page, text='Average Score: ', font=("Arial", 12)).grid(row=2, stick=E, pady=10)
        Label(self.page, text='{}'.format(avg), font=("Arial", 12)).grid(row=2, column=1, stick=W, pady=10)
        self.page.pack()


if __name__ == "__main__":
    root = Tk()
    root.title('Management Information System')
    StudentPage(root)
    root.mainloop()
