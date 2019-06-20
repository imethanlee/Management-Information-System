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
    for i in range(len(columns)):
        table.column(columns[i], width=150, anchor='center')
        table.heading(columns[i], text=columns[i])

    # ----vertical scrollbar------------
    vbar = ttk.Scrollbar(root, orient=VERTICAL, command=table.yview)
    table.configure(yscrollcommand=vbar.set)
    table.grid(row=gird_row, sticky=W + E)
    vbar.grid(row=gird_row, column=1, sticky=NS)
    return table


def handler_adaptor(fun, **kwds):
    """事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧"""
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


def set_cell_value(event, treeview, editcol=None):  # 双击进入编辑状态
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))

    if editcol != cn:
        return

    entryedit = Text(treeview, width=20, height=1)
    entryedit.place(x=(cn - 1) * 150, y=6 + rn * 20)

    def saveedit():
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        # Update to database

        entryedit.destroy()
        okb1.destroy()
        okb2.destroy()

    def quitedit():
        entryedit.destroy()
        okb1.destroy()
        okb2.destroy()

    okb1 = ttk.Button(treeview, text='OK', width=3, command=saveedit)
    okb1.place(x=(cn - 1) * 150 + 85, y=2 + rn * 20)
    okb2 = ttk.Button(treeview, text='Quit', width=4, command=quitedit)
    okb2.place(x=(cn - 1) * 150 + 115, y=2 + rn * 20)
