import time
import re
import pymysql
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Treeview


class GlobalVar:
    def __init__(self):
        self.login_id = 0


def center_window(root: object, width: object, height: object) -> object:
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.update()


def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()


def sql_conn(sql):
    # db = pymysql.connect("localhost", "root", "46281234", "mis")
    # db = pymysql.connect(host="78.141.208.185", user="root", port=33066,
    #                      password="scut-2019-DATABASE", db="mis")
    db = pymysql.connect("106.12.48.99", "root", "scut-2019-DATABASE", "mis")
    cursor = db.cursor()
    cursor.execute(sql)
    ret = cursor.fetchall()
    db.commit()
    db.close()
    return ret


def generate_table(root, gird_row, columns):
    table = Treeview(root, height=14, show="headings", columns=columns)
    if 6 < len(columns) < 9:
        wide = 120
    elif len(columns) > 8:
        wide = 100
    else:
        wide = 150
    for i in range(len(columns)):
        table.column(columns[i], width=wide, anchor='center')
        table.heading(columns[i], text=columns[i])

    # ----vertical scrollbar------------
    vbar = ttk.Scrollbar(root, orient=VERTICAL, command=table.yview)
    table.configure(yscrollcommand=vbar.set)
    table.grid(row=gird_row, sticky=W + E)
    vbar.grid(row=gird_row, column=1, sticky=NS)
    return table


def clear_table(table):
    x = table.get_children()
    for item in x:
        table.delete(item)


def handler_adaptor(fun, **kwds):
    """事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧"""
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


def set_cell_value(event, treeview, scene, editcol=None):  # 双击进入编辑状态
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行

    print(column)
    print(row)
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    print(cn)
    print(rn)

    if scene == 'teacher_score':
        wide = 150
        if editcol != cn:
            return
    elif scene == 'admin_student':
        wide = 120

    entryedit = Text(treeview, width=int(wide / 7.5), height=1)
    entryedit.place(x=(cn - 1) * wide, y=6 + rn * 20)

    def saveedit():
        if scene == 'teacher_score':
            # Update to database
            cid = item_text[0]
            sid = item_text[2]
            value = re.compile(r'^([1-9]?[0-9]\.?[0-9]?)|100|100.0$')
            new_val = entryedit.get(0.0, "end")
            result = value.match(new_val)
            if result:
                treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
                sql = 'update coursechoosing set score=' + new_val + ' where courseID="' + cid + '" ' \
                                                                                                 'and studentID="' + sid + '"'
                sql_conn(sql)
            else:
                messagebox.showinfo('Error', 'Please input a number from 0.0 to 100.0.')

        entryedit.destroy()
        okb1.destroy()
        okb2.destroy()

    def quitedit():
        entryedit.destroy()
        okb1.destroy()
        okb2.destroy()

    okb1 = ttk.Button(treeview, text='OK', width=3, command=saveedit)
    okb1.place(x=(cn - 1) * wide + wide - 65, y=2 + rn * 20)
    okb2 = ttk.Button(treeview, text='Quit', width=4, command=quitedit)
    okb2.place(x=(cn - 1) * wide + wide - 35, y=2 + rn * 20)


def newrow(treeview, columns):
    treeview.insert('', 0, values=columns)
    treeview.update()


class Watch(Frame):
    msec = 1000

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._running = False
        self.timestr1 = StringVar()
        self.timestr2 = StringVar()
        self.makeWidgets()
        self.flag = True
        self._update()
        self.grid()

    def makeWidgets(self):
        l1 = Label(self, textvariable=self.timestr1, font=("Arial", 32))
        l2 = Label(self, textvariable=self.timestr2, font=("Arial", 32))
        l1.pack()
        l2.pack()

    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)

    def _settime(self):
        today1 = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.timestr1.set(today1)
        self.timestr2.set(time1)


def student_verify(self):
    empty = re.compile(r'^$')
    blank_ver = empty.match(self.sname.get()) or empty.match(self.sex.get()) or empty.match(self.eage.get()) \
                or empty.match(self.sid.get()) or empty.match(self.eyear.get()) or empty.match(self.clss.get())
    if blank_ver:
        messagebox.showinfo('Error', 'Please input in every blank.')
        return False

    id = re.compile(r'^[0-9]{10}$')
    id_ver = id.match(self.sid.get())
    if not id_ver:
        messagebox.showinfo('Error', 'Please input ID number in length of 10.')
        return False

    sex = re.compile(r'^(Male|Female)$')
    sex_ver = sex.match(self.sex.get())
    if not sex_ver:
        messagebox.showinfo('Error', 'Please input sex by Male or Female.')
        return False

    eage = re.compile(r'^(50|[1-4][0-9])$')
    eage_ver = eage.match(self.eage.get())
    if not eage_ver:
        messagebox.showinfo('Error', 'Please input entrance age from 10 to 50.')
        return False

    eyear = re.compile(r'^20[0-9][0-9]$')
    eyear_ver = eyear.match(self.eyear.get())
    if not eyear_ver:
        messagebox.showinfo('Error', 'Please input entrance year from 2000 to 2099.')
        return False

    return True


def teacher_verify(self):
    empty = re.compile(r'^$')
    blank_ver = empty.match(self.tname.get()) or empty.match(self.tid.get()) or empty.match(self.cname.get())
    if blank_ver:
        messagebox.showinfo('Error', 'Please input in every blank.')
        return False

    id = re.compile(r'^[0-9]{5}$')
    id_ver = id.match(self.tid.get())
    if not id_ver:
        messagebox.showinfo('Error', 'Please input ID number in length of 5.')
        return False

    return True


def course_verify(self):
    empty = re.compile(r'^$')
    blank_ver = empty.match(self.cname.get()) or empty.match(self.cid.get()) or empty.match(self.credit.get()) \
                or empty.match(self.tid.get()) or empty.match(self.cgrade.get())
    if blank_ver:
        messagebox.showinfo('Error', 'Please input in every blank except canceled year.')
        return False

    cid = re.compile(r'^[0-9]{7}$')
    cid_ver = cid.match(self.cid.get())
    if not cid_ver:
        messagebox.showinfo('Error', 'Please input course ID number in length of 7.')
        return False

    tid = re.compile(r'^[0-9]{5}$')
    tid_ver = tid.match(self.tid.get())
    if not tid_ver:
        messagebox.showinfo('Error', 'Please input teacher ID number in length of 5.')
        return False

    credit = re.compile(r'^[1-9]?[0-9]\.?[0-9]?$')
    credit_ver = credit.match(self.credit.get())
    if not credit_ver:
        messagebox.showinfo('Error', 'Please input credit from 0.0 to 99.9.')
        return False

    cgrade = re.compile(r'^[1-9]$')
    cgrade_ver = cgrade.match(self.cgrade.get())
    if not cgrade_ver:
        messagebox.showinfo('Error', 'Please input course grade from 1 to 9.')
        return False

    if self.cancelYear.get():
        cyear = re.compile(r'^20[0-9][0-9]$')
        cyear_ver = cyear.match(self.cancelYear.get())
        if not cyear_ver:
            messagebox.showinfo('Error', 'Please input canceled year from 2000 to 2099.')
            return False

    return True


def choose_verify(self):
    empty = re.compile(r'^$')
    blank_ver = empty.match(self.cid.get()) or empty.match(self.sid.get()) or empty.match(self.chosenYear.get())
    if blank_ver:
        messagebox.showinfo('Error', 'Please input in every blank.')
        return False

    sid = re.compile(r'^[0-9]{10}$')
    sid_ver = sid.match(self.sid.get())
    if not sid_ver:
        messagebox.showinfo('Error', 'Please input student ID number in length of 10.')
        return False

    cid = re.compile(r'^[0-9]{7}$')
    cid_ver = cid.match(self.cid.get())
    if not cid_ver:
        messagebox.showinfo('Error', 'Please input course ID number in length of 7.')
        return False

    cyear = re.compile(r'^20[0-9][0-9]$')
    cyear_ver = cyear.match(self.chosenYear.get())
    if not cyear_ver:
        messagebox.showinfo('Error', 'Please input chosen year from 2000 to 2099.')
        return False

    current_year = int(time.strftime('%Y', time.localtime(time.time())))
    # grade checking
    sql = 'select entranceYear from student where studentID="{}"' \
        .format(self.sid.get())
    current_grade = current_year - int(sql_conn(sql)[0][0]) + 1
    sql = 'select grade from course where courseID="{}"' \
        .format(self.cid.get())
    require_grade = int(sql_conn(sql)[0][0])
    if current_grade < require_grade:
        messagebox.showinfo('Error', 'The student\'s grade {} does not meet the course\'s grade {}.'
                            .format(current_grade, require_grade))
        return False

    # canceled year checking
    sql = 'select canceledYear from course where courseID="{}"' \
        .format(self.cid.get())
    canceled_year = int(sql_conn(sql)[0][0])
    if int(self.chosenYear.get()) > canceled_year:
        messagebox.showinfo('Error', 'The choosing year {} is later than the canceled year {}.'
                            .format(int(self.chosenYear.get()), canceled_year))
        return False

    return True
