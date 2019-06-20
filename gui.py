from tkinter import *
import tkinter.font as tkFont
from tkinter.ttk import Treeview
import tkinter.messagebox

tk = Tk()
tk.title("Management Information System")
tk.maxsize(700, 500)  # 设置窗口最大尺寸
Label(tk, text='欢迎使用学生管理系统', font=tkFont.Font(size=18), width=60, height=2,
      bg='#FFE7BA').grid(row=0, sticky=W + E)

columns = ('姓名', '学号', '成绩')
table = Treeview(tk, height=14, show="headings", columns=columns)
table.column('姓名', width=150, anchor='center')
table.column('学号', width=150, anchor='center')
table.column('成绩', width=150, anchor='center')
table.heading('姓名', text="姓名")
table.heading('学号', text="学号")
table.heading('成绩', text="成绩")
# all_data()
table.grid(row=1, sticky=W + E)

frame = Frame()
frame.grid(row=2, pady=20)
names = StringVar()
ids = StringVar()
grades = StringVar()
Label(frame, text="姓名：").grid(row=0, column=0)
Entry(frame, textvariable=names).grid(row=0, column=1)
Label(frame, text="学号：").grid(row=1, column=0)
Entry(frame, textvariable=ids).grid(row=1, column=1)
Label(frame, text="成绩：").grid(row=2, column=0)
Entry(frame, textvariable=grades).grid(row=2, column=1)

tk.mainloop()
