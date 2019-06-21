from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
from utils import *


class AdminPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        center_window(self.root, 1000, 618)
        self.create_page()
        self.sid = StringVar()
        self.sname = StringVar()
        self.tid = StringVar()
        self.tname = StringVar()
        self.cid = StringVar()
        self.cname = StringVar()
        self.sex = StringVar()
        self.eage = StringVar()
        self.eyear = StringVar()
        self.credit = StringVar()
        self.cgrade = StringVar()
        self.cancelYear = StringVar()
        self.chosenYear = StringVar()
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

        columns = ('Student ID', 'Name', 'Sex', 'Entrance Age', 'Entrance Year',
                   'Class')
        table = generate_table(self.page, 1, columns)

        sql = 'select * from student'
        db_fetch = sql_conn(sql)
        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                        db_fetch[i][2], db_fetch[i][3],
                                        db_fetch[i][4], db_fetch[i][5]))

        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Student ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.sid, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W,
                                                                                     pady=10)
        Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.sname, font=("Arial", 16), width=20).grid(row=0, column=3, stick=E + W,
                                                                                       pady=10)

        def modify(table):
            window = Toplevel()
            window.title('Modify student info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)

            sql = 'select * from student where studentID = "{}" or name="{}"'.format(self.sid.get(), self.sname.get())
            db_fetch = sql_conn(sql)[0]
            self.sid.set(db_fetch[0])
            self.sname.set(db_fetch[1])
            self.sex.set(db_fetch[2])
            self.eage.set(db_fetch[3])
            self.eyear.set(db_fetch[4])
            self.clss.set(db_fetch[5])

            Label(window, text='Student ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.sid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Name: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.sname, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Sex(Male/Female): ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.sex, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Entrance Age: ', font=("Arial", 12)).grid(row=4, stick=E + W, pady=10)
            Entry(window, textvariable=self.eage, font=("Arial", 12), width=12).grid(row=4, column=1, stick=E + W,
                                                                                     pady=10)
            Label(window, text='Entrance Year: ', font=("Arial", 12)).grid(row=5, stick=E + W, pady=10)
            Entry(window, textvariable=self.eyear, font=("Arial", 12), width=12).grid(row=5, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Class: ', font=("Arial", 12)).grid(row=6, stick=E + W, pady=10)
            Entry(window, textvariable=self.clss, font=("Arial", 12), width=12).grid(row=6, column=1, stick=E + W,
                                                                                     pady=10)
            Label(window, text='Drop Out(Y/N): ', font=("Arial", 12)).grid(row=7, stick=E + W, pady=10)
            Entry(window, font=("Arial", 12), width=12).grid(row=7, column=1, stick=E + W, pady=10)

            Label(window).grid(row=8, stick=W)

            def save_new_student(table):

                sql = 'update student set name="{}", sex="{}", entranceAge="{}", ' \
                      'entranceYear="{}", class="{}" where studentID="{}"'\
                    .format(self.sname.get(), self.sex.get(), self.eage.get(),
                            self.eyear.get(), self.clss.get(), self.sid.get())
                sql_conn(sql)

                clear_table(table)
                sql = 'select * from student'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
                window.destroy()
                # save to database

            Button(window, text='Save', command=lambda: save_new_student(table),
                   font=("Arial", 16)).grid(row=9, column=0, stick=E, pady=10)


        Button(query_frame, text='Modify', command=lambda: modify(table),
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        def delete(table):
            studentID = ''
            # delete student
            sql = 'delete from coursechoosing where studentID="{}"'.format(self.sid.get())
            sql_conn(sql)
            sql = 'delete from user where username="{}"'.format(self.sid.get())
            sql_conn(sql)
            sql = 'delete from student where studentID="{}" or name="{}"'.format(self.sid.get(), self.sname.get())
            sql_conn(sql)

            clear_table(table)
            sql = 'select * from student'
            db_fetch = sql_conn(sql)
            for i in range(len(db_fetch)):
                table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                            db_fetch[i][2], db_fetch[i][3],
                                            db_fetch[i][4], db_fetch[i][5]))

        Button(query_frame, text='Delete', command=lambda: delete(table),
               font=("Arial", 16)).grid(row=2, column=2, stick=W, pady=10)

        Label(query_frame).grid(row=3, stick=W)

        def new_student(table):
            window = Toplevel()
            window.title('New student info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)

            self.sid.set('')
            self.sname.set('')
            self.sex.set('')
            self.eage.set('')
            self.eyear.set('')
            self.clss.set('')

            Label(window, text='Student ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.sid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Name: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.sname, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Sex(Male/Female): ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.sex, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Entrance Age: ', font=("Arial", 12)).grid(row=4, stick=E + W, pady=10)
            Entry(window, textvariable=self.eage, font=("Arial", 12), width=12).grid(row=4, column=1, stick=E + W,
                                                                                     pady=10)
            Label(window, text='Entrance Year: ', font=("Arial", 12)).grid(row=5, stick=E + W, pady=10)
            Entry(window, textvariable=self.eyear, font=("Arial", 12), width=12).grid(row=5, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Class: ', font=("Arial", 12)).grid(row=6, stick=E + W, pady=10)
            Entry(window, textvariable=self.clss, font=("Arial", 12), width=12).grid(row=6, column=1, stick=E + W,
                                                                                     pady=10)
            Label(window, text='Drop Out(Y/N): ', font=("Arial", 12)).grid(row=7, stick=E + W, pady=10)
            Entry(window, font=("Arial", 12), width=12).grid(row=7, column=1, stick=E + W, pady=10)

            Label(window).grid(row=8, stick=W)

            def save_new_student(table):

                sql = 'insert into student(studentID, name, sex, entranceAge, entranceYear, class) ' \
                      'values ("{}", "{}", "{}", "{}", "{}", "{}")' \
                    .format(self.sid.get(), self.sname.get(), self.sex.get(),
                            self.eage.get(), self.eyear.get(), self.clss.get())
                sql_conn(sql)

                sql = 'insert into user(usertype, username, password) values ("{}","{}","{}")'\
                    .format("student", self.sid.get(), self.sid.get())
                sql_conn(sql)

                clear_table(table)
                sql = 'select * from student'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
                sql_conn(sql)
                window.destroy()

            Button(window, text='Save', command=lambda: save_new_student(table),
                   font=("Arial", 16)).grid(row=9, column=0, stick=E, pady=10)

            # sql = 'insert into student(studentID, name, sex, entranceAge, entranceYear, class) ' \
            #       'values ("s03", "Cob", "Male", "20", "2017", "class 01")'

        Button(query_frame, text='New', command=lambda: new_student(table),
               font=("Arial", 16)).grid(row=5, column=1, stick=W, pady=10)

        Button(query_frame, text='Drop out', command='updateFunction',
               font=("Arial", 16)).grid(row=5, column=2, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def teachers_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)
        columns = ('Teacher ID', 'Teacher Name', 'Courses')
        table = generate_table(self.page, 1, columns)

        sql = 'select * from teacher'
        db_fetch = sql_conn(sql)
        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1], db_fetch[i][2]))


        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Teacher ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.tid, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W,
                                                                                     pady=10)
        Label(query_frame, text=' / Teacher Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.tname, font=("Arial", 16), width=20).grid(row=0, column=3, stick=E + W,
                                                                                       pady=10)

        def modify():
            window = Toplevel()
            window.title('Modify teacher info')
            center_window(window, 309, 500)

            sql = 'select * from teacher where teacherID = "{}" or name="{}"'.format(self.tid.get(), self.tname.get())
            db_fetch = sql_conn(sql)[0]
            self.tid.set(db_fetch[0])
            self.tname.set(db_fetch[1])
            self.cname.set(db_fetch[2])

            Label(window).grid(row=0, stick=W)
            Label(window, text='Teacher ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.tid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Teacher Name: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.tname, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Courses: ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.cname, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                      pady=10)

            Label(window).grid(row=4, stick=W)

            def save_new_teacher():
                sql = 'update teacher set name="{}", course="{}" where teacherID="{}"'\
                    .format(self.tname.get(), self.cname.get(), self.tid.get())
                sql_conn(sql)

                clear_table(table)
                sql = 'select * from teacher'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1], db_fetch[i][2]))
                window.destroy()

            Button(window, text='Save', command=save_new_teacher,
                   font=("Arial", 16)).grid(row=5, column=0, stick=E, pady=10)

        Button(query_frame, text='Modify', command=modify,
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        def delete():

            sql = 'delete from coursechoosing where teacherID="{}"'.format(self.tid.get())
            sql_conn(sql)

            sql = 'delete from teacher where teacherID="{}" or name="{}"'.format(self.tid.get(), self.tname.get())
            sql_conn(sql)

            clear_table(table)
            sql = 'select * from teacher'
            db_fetch = sql_conn(sql)
            for i in range(len(db_fetch)):
                table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1], db_fetch[i][2]))

        Button(query_frame, text='Delete', command=delete,
               font=("Arial", 16)).grid(row=2, column=2, stick=W, pady=10)

        Label(query_frame).grid(row=3, stick=W)

        def new_teacher():
            window = Toplevel()
            window.title('New student info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)
            Label(window, text='Teacher ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.tid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Teacher Name: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.tname, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Courses: ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.cname, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                      pady=10)

            Label(window).grid(row=4, stick=W)

            def save_new_teacher():
                sql = 'insert into teacher(teacherID, name, course) ' \
                      'values ("{}", "{}", "{}")' \
                    .format(self.tid.get(), self.tname.get(), self.cname.get())
                sql_conn(sql)

                sql = 'insert into user(usertype, username, password) ' \
                      'values ("teacher", "{}", "{}")' \
                    .format(self.tid.get(), self.tid.get())
                sql_conn(sql)


                clear_table(table)
                sql = 'select * from teacher'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2]))
                sql_conn(sql)
                window.destroy()

            Button(window, text='Save', command=save_new_teacher,
                   font=("Arial", 16)).grid(row=5, column=0, stick=E, pady=10)

        Button(query_frame, text='New', command=new_teacher,
               font=("Arial", 16)).grid(row=5, column=1, stick=W, pady=10)
        # course_data()
        self.page.pack()

    def courses_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Course ID', 'Course Name', 'Teacher ID', 'Credit', 'Course Grade', 'Canceled Year')
        table = generate_table(self.page, 1, columns)

        sql = 'select * from course'
        db_fetch = sql_conn(sql)
        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                        db_fetch[i][2], db_fetch[i][3],
                                        db_fetch[i][4], db_fetch[i][5]))

        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Course ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.cid, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W,
                                                                                     pady=10)
        Label(query_frame, text='Course Name: ', font=("Arial", 16)).grid(row=1, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.cname, font=("Arial", 16), width=20).grid(row=1, column=1, stick=E + W,
                                                                                     pady=10)
        def modify(table):
            window = Toplevel()
            window.title('Modify course info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)

            sql = 'select * from course where courseID="{}" or name="{}"'\
                .format(self.cid.get(), self.cname.get())
            db_fetch = sql_conn(sql)[0]
            self.cid.set(db_fetch[0])
            self.cname.set(db_fetch[1])
            self.tid.set(db_fetch[2])
            self.credit.set(db_fetch[3])
            self.cgrade.set(db_fetch[4])
            self.cancelYear.set(db_fetch[5])

            Label(window, text='Course ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.cid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Course Name: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.cname, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Teacher ID: ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.tid, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Credit: ', font=("Arial", 12)).grid(row=4, stick=E + W, pady=10)
            Entry(window, textvariable=self.credit, font=("Arial", 12), width=12).grid(row=4, column=1, stick=E + W,
                                                                                       pady=10)
            Label(window, text='Course Grade: ', font=("Arial", 12)).grid(row=5, stick=E + W, pady=10)
            Entry(window, textvariable=self.cgrade, font=("Arial", 12), width=12).grid(row=5, column=1, stick=E + W,
                                                                                       pady=10)
            Label(window, text='Canceled Year: ', font=("Arial", 12)).grid(row=6, stick=E + W, pady=10)
            Entry(window, textvariable=self.cancelYear, font=("Arial", 12), width=12).grid(row=6, column=1, stick=E + W,
                                                                                           pady=10)

            Label(window).grid(row=7, stick=W)

            def save_new_courses(table):
                # save to database
                sql = 'update course set name="{}", teacherID="{}", credit="{}", grade="{}", canceledYear="{}" ' \
                      'where courseID="{}"'\
                    .format(self.cname.get(), self.tid.get(), self.credit.get(),
                            self.cgrade.get(), self.cancelYear.get(), self.cid.get())
                sql_conn(sql)
                clear_table(table)
                sql = 'select * from course'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
                window.destroy()

            Button(window, text='Save', command=lambda: save_new_courses(table),
                   font=("Arial", 16)).grid(row=8, column=0, stick=E, pady=10)

        Button(query_frame, text='Modify', command=lambda: modify(table),
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        def delete(table):
            sql = 'delete from coursechoosing where courseID="{}"'.format(self.cid.get())
            sql_conn(sql)

            sql = 'delete from course where courseID="{}" or name="{}"'.format(self.cid.get(), self.cname.get())
            sql_conn(sql)
            clear_table(table)
            sql = 'select * from course'
            db_fetch = sql_conn(sql)
            for i in range(len(db_fetch)):
                table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                            db_fetch[i][2], db_fetch[i][3],
                                            db_fetch[i][4], db_fetch[i][5]))
            # delete student

        Button(query_frame, text='Delete', command=lambda: delete(table),
               font=("Arial", 16)).grid(row=2, column=2, stick=W, pady=10)

        Label(query_frame).grid(row=3, stick=W)

        def new_courses(table):
            window = Toplevel()
            window.title('New course info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)

            self.cid.set('')
            self.cname.set('')
            self.tid.set('')
            self.credit.set('')
            self.cgrade.set('')
            self.cancelYear.set('')

            Label(window, text='Course ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.cid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Course Name: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.cname, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                      pady=10)
            Label(window, text='Teacher ID: ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.tid, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Credit: ', font=("Arial", 12)).grid(row=4, stick=E + W, pady=10)
            Entry(window, textvariable=self.credit, font=("Arial", 12), width=12).grid(row=4, column=1, stick=E + W,
                                                                                       pady=10)
            Label(window, text='Course Grade: ', font=("Arial", 12)).grid(row=5, stick=E + W, pady=10)
            Entry(window, textvariable=self.cgrade, font=("Arial", 12), width=12).grid(row=5, column=1, stick=E + W,
                                                                                       pady=10)
            Label(window, text='Canceled Year: ', font=("Arial", 12)).grid(row=6, stick=E + W, pady=10)
            Entry(window, textvariable=self.cancelYear, font=("Arial", 12), width=12).grid(row=6, column=1, stick=E + W,
                                                                                           pady=10)
            Label(window).grid(row=7, stick=W)

            def save_new_courses(table):
                sql = 'insert into course(courseID, name, teacherID, credit, grade, canceledYear) ' \
                      'values ("{}", "{}", "{}", "{}", "{}", "{}")'\
                    .format(self.cid.get(), self.cname.get(), self.tid.get(),
                            self.credit.get(), self.cgrade.get(), self.cancelYear.get())

                sql_conn(sql)
                clear_table(table)
                sql = 'select * from course'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
                window.destroy()

            Button(window, text='Save', command=lambda: save_new_courses(table),
                   font=("Arial", 16)).grid(row=8, column=0, stick=E, pady=10)

        Button(query_frame, text='New', command=lambda: new_courses(table),
               font=("Arial", 16)).grid(row=5, column=1, stick=W, pady=10)

        # course_data()
        self.page.pack()

    def choosing_page(self):
        clear_frame(self.page)
        Label(self.page).grid(row=0, stick=W)

        columns = ('Student ID', 'CourseID', 'Teacher ID', 'Chosen Year', 'Score')
        table = generate_table(self.page, 1, columns)

        sql = 'select * from coursechoosing'
        db_fetch = sql_conn(sql)
        for i in range(len(db_fetch)):
            table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                        db_fetch[i][2], db_fetch[i][3],
                                        db_fetch[i][4]))

        query_frame = Frame(self.page)
        query_frame.grid(row=2, stick=W, ipady=10, ipadx=10)
        Label(query_frame, text='Student ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.sid, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W,
                                                                                     pady=10)
        Label(query_frame, text=' / Course ID: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.cid, font=("Arial", 16), width=20).grid(row=0, column=3, stick=E + W,
                                                                                     pady=10)

        def modify(table):
            window = Toplevel()
            window.title('Modify course choosing info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)

            sql = 'select * from coursechoosing where studentID="{}" and courseID="{}"'\
                .format(self.sid.get(), self.cid.get())
            db_fetch = sql_conn(sql)[0]
            self.sid.set(db_fetch[0])
            self.cid.set(db_fetch[1])
            self.chosenYear.set(db_fetch[3])

            Label(window, text='Student ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.sid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Course ID: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.cid, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Chosen Year: ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.chosenYear, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                           pady=10)

            Label(window).grid(row=4, stick=W)

            def save_new_course_choosing(table):
                sql = 'update coursechoosing set chosenYear="{}" where studentID="{}" and courseID="{}"'\
                    .format(self.chosenYear.get(), self.sid.get(), self.cid.get())
                sql_conn(sql)
                clear_table(table)
                sql = 'select * from coursechoosing'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4]))
                window.destroy()

            Button(window, text='Save', command=lambda: save_new_course_choosing(table),
                   font=("Arial", 16)).grid(row=5, column=0, stick=E, pady=10)

        Button(query_frame, text='Modify', command=lambda: modify(table),
               font=("Arial", 16)).grid(row=2, column=1, stick=W, pady=10)

        def delete(table):
            sql = 'delete from coursechoosing where courseID="{}" and studentID = "{}"'\
                .format(self.cid.get(), self.sid.get())
            sql_conn(sql)
            clear_table(table)
            sql = 'select * from coursechoosing'
            db_fetch = sql_conn(sql)
            for i in range(len(db_fetch)):
                table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                            db_fetch[i][2], db_fetch[i][3],
                                            db_fetch[i][4]))
            # delete student

        Button(query_frame, text='Delete', command=lambda: delete(table),
               font=("Arial", 16)).grid(row=2, column=2, stick=W, pady=10)

        Label(query_frame).grid(row=3, stick=W)

        def new_course_choosing(table):
            window = Toplevel()
            window.title('New student info')
            center_window(window, 309, 500)
            Label(window).grid(row=0, stick=W)
            Label(window, text='Student ID: ', font=("Arial", 12)).grid(row=1, stick=E + W, pady=10)
            Entry(window, textvariable=self.sid, font=("Arial", 12), width=12).grid(row=1, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Course ID: ', font=("Arial", 12)).grid(row=2, stick=E + W, pady=10)
            Entry(window, textvariable=self.cid, font=("Arial", 12), width=12).grid(row=2, column=1, stick=E + W,
                                                                                    pady=10)
            Label(window, text='Chosen Year: ', font=("Arial", 12)).grid(row=3, stick=E + W, pady=10)
            Entry(window, textvariable=self.chosenYear, font=("Arial", 12), width=12).grid(row=3, column=1, stick=E + W,
                                                                                           pady=10)
            Label(window).grid(row=4, stick=W)

            def save_new_course_choosing(table):

                sql = 'select teacherID from course where courseID="{}"'\
                    .format(self.cid.get())
                tid = sql_conn(sql)[0][0]

                sql = 'insert into coursechoosing(studentID, courseID, teacherID, chosenYear) ' \
                      'values ("{}", "{}", "{}", "{}")'\
                    .format(self.sid.get(), self.cid.get(), tid, self.chosenYear.get())
                sql_conn(sql)

                clear_table(table)
                sql = 'select * from coursechoosing'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4]))
                window.destroy()

            Button(window, text='Save', command=lambda: save_new_course_choosing(table),
                   font=("Arial", 16)).grid(row=5, column=0, stick=E, pady=10)

        Button(query_frame, text='New', command=lambda: new_course_choosing(table),
               font=("Arial", 16)).grid(row=5, column=1, stick=W, pady=10)

        # scores_data()

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
            if len(student) == 0 and len(course) == 0:
                sql = 'select student.studentID, student.name, course.courseID, course.name, course.credit, coursechoosing.score from ' \
                      'student, course, coursechoosing where ' \
                      '(coursechoosing.studentID=student.studentID and ' \
                      'coursechoosing.courseID=course.courseID)'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))

            elif len(student) != 0 and len(course) == 0:
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

            if len(course) == 0:
                sql = 'select course.courseID, course.name, student.studentID, student.name, course.credit, coursechoosing.score from ' \
                      'student, course, coursechoosing where ' \
                      '(coursechoosing.studentID=student.studentID and ' \
                      'coursechoosing.courseID=course.courseID)'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
            else:
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

            if len(teacher) == 0:
                sql = 'select teacher.teacherID, teacher.name, course.courseID, course.name, course.credit, course.canceledYear from ' \
                      'teacher, course where ' \
                      '(teacher.teacherID=course.teacherID)'
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
            else:
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
        Label(query_frame, text='Student ID: ', font=("Arial", 16)).grid(row=0, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.student, font=("Arial", 16), width=20).grid(row=0, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Student Name: ', font=("Arial", 16)).grid(row=0, column=2, stick=E + W, pady=10)
        # Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=0, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Course ID: ', font=("Arial", 16)).grid(row=1, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.course, font=("Arial", 16), width=20).grid(row=1, column=1, stick=E + W, pady=10)
        # Label(query_frame, text=' / Course Name: ', font=("Arial", 16)).grid(row=1, column=2, stick=E + W, pady=10)
        # Text(query_frame, font=("Arial", 16), width=20, height=1).grid(row=1, column=3, stick=E + W, pady=10)

        Label(query_frame, text='Class: ', font=("Arial", 16)).grid(row=2, stick=E + W, pady=10)
        Entry(query_frame, textvariable=self.clss, font=("Arial", 16), width=20).grid(row=2, column=1, stick=E + W, pady=10)

        avg = StringVar()

        def click7():
            clear_table(table)
            student = self.student.get()
            course = self.course.get()
            clss = self.clss.get()

            if len(student) != 0:
                sql = 'select avg(coursechoosing.score) from coursechoosing where coursechoosing.studentID="'+student+'"'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])

                sql = 'select student.studentID, student.Name, course.courseID, course.name, student.class, coursechoosing.score ' \
                      'from student, course, coursechoosing ' \
                      'where coursechoosing.studentID=student.studentID and coursechoosing.courseID=course.courseID ' \
                      'and student.studentID="{}" order by course.courseID asc'\
                    .format(student)
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
            elif len(course) != 0:
                sql = 'select avg(coursechoosing.score) from coursechoosing where coursechoosing.courseID="'+course+'"'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])

                sql = 'select student.studentID, student.Name, course.courseID, course.name, student.class, coursechoosing.score ' \
                      'from student, course, coursechoosing ' \
                      'where coursechoosing.studentID=student.studentID and coursechoosing.courseID=course.courseID ' \
                      'and course.courseID="{}" order by student.studentID asc'\
                    .format(course)
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
            elif len(clss) != 0:
                sql = 'select avg(coursechoosing.score) from coursechoosing, student where ' \
                      'student.class="'+clss+'" and coursechoosing.studentID = student.studentID'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])

                sql = 'select student.studentID, student.Name, course.courseID, course.name, student.class, coursechoosing.score ' \
                      'from student, course, coursechoosing ' \
                      'where coursechoosing.studentID=student.studentID and coursechoosing.courseID=course.courseID ' \
                      'and student.class="{}" order by student.studentID asc'\
                    .format(clss)
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))
            else:
                sql = 'select avg(coursechoosing.score) from coursechoosing'
                db_fetch = sql_conn(sql)
                avg.set(db_fetch[0][0])

                sql = 'select student.studentID, student.Name, course.courseID, course.name, student.class, coursechoosing.score ' \
                      'from student, course, coursechoosing ' \
                      'where coursechoosing.studentID=student.studentID and coursechoosing.courseID=course.courseID ' \
                      'order by student.studentID asc'\
                    .format(student)
                db_fetch = sql_conn(sql)
                for i in range(len(db_fetch)):
                    table.insert('', i, values=(db_fetch[i][0], db_fetch[i][1],
                                                db_fetch[i][2], db_fetch[i][3],
                                                db_fetch[i][4], db_fetch[i][5]))

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
