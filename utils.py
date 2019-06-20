import pymysql


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

