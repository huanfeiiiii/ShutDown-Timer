# -*- coding:utf-8 -*-

"""
时间:2021年10月03日
作者:幻非
"""

import os
import tkinter

player = tkinter.Tk()
player.title("定时关机")
mw, mh = player.maxsize()
player.geometry('300x200+%d+%d' % ((mw - 500) / 2, (mh - 300) / 2))  # 窗口居中
player.resizable(False, False)  # 锁定窗口大小


def start():
    if status.get() == 1:
        time = int(text.get()) * 60
        close(time)
    elif status.get() == 2:
        time = int(text.get()) * 3600
        close(time)


# 计时关机
def close(self):
    if self < 315360000:
        shutdown = "shutdown -s -t " + str(self)
        if os.system(shutdown) != 0:
            os.system('shutdown -a')
            os.system(shutdown)
    else:
        print("超出范围")


# 结束关机
def end():
    os.system('shutdown -a')


Frame1 = tkinter.Frame(player)
Frame1.pack(side="top", pady=25)

Frame2 = tkinter.Frame(player)
Frame2.pack()


text = tkinter.Entry(Frame1, width=5, font=('', '40'), justify='center')
text.pack(side="right")

status = tkinter.IntVar()
status.set(2)
tkinter.Radiobutton(Frame1, text="分钟", variable=status, value=1, font=('', '18')).pack()
tkinter.Radiobutton(Frame1, text="小时", variable=status, value=2, font=('', '18')).pack()


btn_random_video = tkinter.Button(Frame2, text="开始计时", font=('', '18'), command=start)
btn_random_video.pack(side="left", padx=5)
btn_random_video = tkinter.Button(Frame2, text="关闭计时", font=('', '18'), command=end)
btn_random_video.pack(side="right", padx=5)


player.mainloop()
