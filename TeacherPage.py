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
        menubar.add_command(label='Scores', command=self.scores_page)
        self.root['menu'] = menubar  # 设置菜单栏

    def home_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        # get data from database
        sql = 'select * from teacher where teacher.teacherID="'+GlobalVar.login_id+'"'
        db_fetch = sql_conn(sql)[0]

        # ID, Name, Sex, Entrance Age, Entrance Year, Class, Grade [7]
        info_head = ['ID', 'Name']
        teacher_info = [db_fetch[0], db_fetch[1]]

        Label(self.page, text='Hello, Teacher {}!'.format(teacher_info[1]), font=("Arial", 16)).grid(row=1, stick=W,
                                                                                                     pady=10)
        for i in range(2):
            Label(self.page, text=info_head[i] + ': ', font=("Arial", 12)).grid(row=i + 2, stick=E, pady=10)
            Label(self.page, text=teacher_info[i], font=("Arial", 12)).grid(row=i + 2, column=1, stick=W, pady=10)

        columns = ('Course ID', 'Course Name', 'Credit', 'Course Grade', 'Canceled Year')
        table = generate_table(self.page, 4, columns)
        # course_data()
        # get data from database
        sql = 'select course.courseID, course.name, course.credit, course.grade, course.canceledYear' \
              ' from teacher, course where teacher.teacherID="'+GlobalVar.login_id+'"'+' and ' \
              'teacher.teacherID=course.teacherID'
        db_fetch = sql_conn(sql)

        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                        db_fetch[i][2], db_fetch[i][3],
                                        db_fetch[i][4]))

        self.page.pack()

    def scores_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Course ID', 'Course Name', 'Student ID', 'Student Name', 'Chosen Year', 'Score')
        generate_table(self.page, 1, columns)
        # scores_data()

        # Label(self.page, text='Average Score: ', font=("Arial", 12)).grid(row=2, stick=E, pady=10)
        # Label(self.page, text='{}'.format('ave'), font=("Arial", 12)).grid(row=2, column=1, stick=W, pady=10)
        self.page.pack()


if __name__ == "__main__":
    root = Tk()
    root.title('Management Information System')
    TeacherPage(root)
    root.mainloop()
