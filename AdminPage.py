from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
from utils import *


class AdminPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        center_window(self.root, 1000, 618)
        self.create_page()
        self.student = StringVar()
        self.course = StringVar()
        self.teacher = StringVar()
        self.clss = StringVar()

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
        Label(query_frame, text='Student ID / Student Name: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.student, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        # Entry(query_frame, textvariable=self.sname, font=("Arial", 16), width=20).grid(row=0, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Course ID / Course Name: ', font=("Arial", 16)).grid(row=1, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.course, font=("Arial", 16), width=20).grid(row=1, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=1, column=2, stick=E + W, pady=10)
        # Entry(query_frame, textvariable=self.cname, font=("Arial", 16), width=20).grid(row=1, column=3, stick=E + W, pady=10)

        def click34():
            clear_table(table)
            student = self.student.get()
            course = self.course.get()

            if len(student) != 0 and len(course) == 0:
                sql = 'select student.studentID, student.name, course.courseID, course.name, course.credit, coursechoosing.score from ' \
                      'student, course, coursechoosing where ' \
                      '(coursechoosing.studentID=student.studentID and ' \
                      'coursechoosing.courseID=course.courseID) and ' \
                      '(student.studentID="' + student + '" or student.name="' + student + '")'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))

            elif len(student) != 0 and len(course) != 0:
                sql = 'select student.studentID, student.name, course.courseID, course.name, course.credit, coursechoosing.score from ' \
                      'student, course, coursechoosing where ' \
                      '(coursechoosing.studentID=student.studentID and ' \
                      'coursechoosing.courseID=course.courseID) and ' \
                      '(student.studentID="' + student + '" or student.name="' + student + '") and ' \
                      '(course.courseID="' + course + '" or course.name="' + course + '")'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))

        Button(query_frame, text='Search', command=click34,
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
        Label(query_frame, text='Course ID / Course Name: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.course, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        # Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        def click5():
            clear_table(table)
            student = self.student.get()
            course = self.course.get()

            sql = 'select course.courseID, course.name, student.studentID, student.name, course.credit, coursechoosing.score from ' \
                      'student, course, coursechoosing where ' \
                      '(coursechoosing.studentID=student.studentID and ' \
                      'coursechoosing.courseID=course.courseID) and ' \
                      '(course.courseID="' + course + '" or course.name="' + course + '")'
            db_fetch = sql_conn(sql)
            for i in range(len(db_fetch)):
                table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                            db_fetch[i][2], db_fetch[i][3],
                                            db_fetch[i][4], db_fetch[i][5]))

        Button(query_frame, text='Search', command=click5,
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def query_teacher_page(self):  # 6
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        columns = ('Teacher ID', 'Teacher Name', 'Course ID', 'Course Name', 'Credit', 'Canceled Year')
        table = generate_table(self.page, 1, columns)
        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Teacher ID / Teacher Name: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.teacher, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Teacher Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        # Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        def click6():
            clear_table(table)
            teacher = self.teacher.get()

            sql = 'select teacher.teacherID, teacher.name, course.courseID, course.name, course.credit, course.canceledYear from ' \
                  'teacher, course where ' \
                  '(teacher.teacherID=course.teacherID) and ' \
                  '(teacher.teacherID="' + teacher + '" or teacher.name="' + teacher + '")'
            db_fetch = sql_conn(sql)
            for i in range(len(db_fetch)):
                table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                            db_fetch[i][2], db_fetch[i][3],
                                            db_fetch[i][4], db_fetch[i][5]))

        Button(query_frame, text='Search', command=click6,
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
        Label(query_frame, text='Student ID / Student Name: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.student, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        # Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Course ID / Course Name: ', font=("Arial", 16)).grid(row=1, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.course, font=("Arial", 16), width=20).grid(row=1, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=1, column=2, stick=E + W, pady=10)
        # Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=1, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Class: ', font=("Arial", 16)).grid(row=2, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.clss, font=("Arial", 16), width=20).grid(row=2, column=1, stick=E + W, pady=10)

        avg = StringVar()

        def click7():
            clear_table(table)
            teacher = self.teacher.get()
            student = self.student.get()
            course = self.course.get()
            clss = self.clss.get()

            if len(student) != 0:
                sql = 'select avg(coursechoosing.score) from coursechoosing where coursechoosing.studentID="'+student+'"'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])
            elif len(course) != 0:
                sql = 'select avg(coursechoosing.score) from coursechoosing where coursechoosing.courseID="'+course+'"'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])
            elif len(clss) != 0:
                sql = 'select avg(coursechoosing.score) from coursechoosing, student where ' \
                      'student.class="'+clss+'" and coursechoosing.studentID = student.studentID'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])

        Button(query_frame, text='Search', command=click7,
               font=("Arial", 16)).grid(row=3, column=1, stick=W, pady=10)

        Label(query_frame, text='Average Score: ', font=("Arial", 16)).grid(row=3, column=2, stick=E, pady=10)
        Label(query_frame, textvariable=avg, text='{}'.format('avg'), font=("Arial", 16)).grid(row=3, column=3, stick=W, pady=10)
        self.page.pack()

        # course_data()
        self.page.pack()


if __name__ == "__main__":
    root = Tk()
    root.title('Management Information System')
    AdminPage(root)
    root.mainloop()
