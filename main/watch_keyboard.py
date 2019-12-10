import keyboard
import time
import sys
from tkinter import *
from tkinter import font,ttk

def main():
    timeout_count = [0]

    def watchKeyboard():
        typed_pool = []
        keyboard.start_recording()
        time.sleep(5)
        typed_pool = keyboard.stop_recording()
        if len(typed_pool) == 0:
            timeout_count[0] += 1
        else:
            timeout_count[0] = 0
        if timeout_count[0] <= 5:
            watchKeyboard()
    
    watchKeyboard()

    # サボり認定！
    # 基本情報
    root = Tk()
    root.title(u"サボってる人チェッカー")
    root.geometry("400x200")

    # メッセージ情報
    msg_txt = StringVar()
    msg_txt.set('サボりか？')
    msg_font = font.Font(family='Helvetica', size=80, weight='bold')
    msg = Label(root,textvariable=msg_txt,font=msg_font)
    msg.pack()
    root.mainloop()

    root.protocol("WM_DELETE_WINDOW", main())

if __name__ == "__main__":
    main()