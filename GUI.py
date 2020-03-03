import os
from tkinter import *
from tkinter import filedialog

LEFT_BASE_LINE = 20


class Menu(object):

    def __init__(self, master, x, y, values):
        self.value = StringVar(vc_frame)
        self.value.set(values[0])
        self.value.trace("w", self.callback)

        self.menu = OptionMenu(master, self.value, *values)
        self.menu.place(x=x, y=y, anchor='nw')

    def callback(self, *args):
        print(self.value.get())


class AskDirBtn(object):

    def __init__(self, x, y, label_text):
        self.label_text = label_text
        self.folder_path = ''
        Button(vc_frame, text='選擇目錄', command=self.ask_dir_callback).place(x=x, y=y, anchor='nw')

    def ask_dir_callback(self):
        self.folder_path = filedialog.askdirectory()
        self.label_text.set('工作目錄 : {}'.format(self.folder_path))


def call_rename():
    cmd = 'python rename.py {} "{}" {} {}'.format( menu.value, btn.folder_path, replacer.get(), target.get())
    print(cmd)
    os.system(cmd)


window = Tk()
window.title('你的標題')
window.geometry('500x500') #寬x高
window.maxsize(500, 500) #寬,高
window.resizable(0, 0) #不可以更改大小

vc_frame = Frame(window).pack(side=TOP)

# selector
y = 20
Label(vc_frame, text='請選擇版控軟體').place(x=LEFT_BASE_LINE, y=y, anchor='nw')
menu = Menu(vc_frame, 250, y, ['git', 'svn'])
# menu.value

# select folder
y = 60
label_text = StringVar(vc_frame)
label_text.set('請選擇工作目錄')
Label(vc_frame, textvariable=label_text).place(x=LEFT_BASE_LINE, y=y, anchor='nw')
btn = AskDirBtn(250, y, label_text)
# btn.folder_path

# entry
y = 100
label = Label(vc_frame, text='請輸入欲修改的檔名(正則)').place(x=LEFT_BASE_LINE, y=y, anchor='nw')
replacer = Entry(vc_frame)
replacer.place(x=250, y=y, anchor='nw')
# replacer.get()

# entry
y = 140
label = Label(vc_frame, text='請輸入欲取代的字串').place(x=LEFT_BASE_LINE, y=y, anchor='nw')
target = Entry(vc_frame)
target.place(x=250, y=y, anchor='nw')
# target.get()

# exec
y = 180
Button(vc_frame, text='執行', command=call_rename).place(x=LEFT_BASE_LINE, y=y, anchor='nw')

window.mainloop()
