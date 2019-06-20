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


def set_cell_value(event, treeview, root):  # 双击进入编辑状态
    for item in treeview.selection():
        # item = I001
        item_text = treeview.item(item, "values")
        # print(item_text[0:2])  # 输出所选行的值
    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    entryedit = Text(root, width=10 + (cn - 1) * 16, height=1)
    entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

    def saveedit():
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()

    okb = ttk.Button(root, text='OK', width=4, command=saveedit)
    okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)
