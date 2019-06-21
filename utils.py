import time

import pymysql
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview


class GlobalVar:
    def __init__(self):
        self.login_id = 0


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    # print(size)
    root.geometry(size)


def clear_frame(root):
    for widget in root.winfo_children():
        widget.destroy()


def sql_conn(sql):
    db = pymysql.connect("localhost", "root", "46281234", "mis")
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
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        if scene == 'teacher_score':
            # Update to database
            cid = item_text[0]
            sid = item_text[2]
            new_val = entryedit.get(0.0, "end")
            sql = 'update coursechoosing set score=' + new_val + ' where courseID="' + cid + '" ' \
                                                                                             'and studentID="' + sid + '"'
            sql_conn(sql)

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
        l1 = Label(self, textvariable=self.timestr1, font=("Arial", 24))
        l2 = Label(self, textvariable=self.timestr2, font=("Arial", 24))
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
