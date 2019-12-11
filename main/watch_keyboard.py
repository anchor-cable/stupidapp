import keyboard
import time
import sys
from tkinter import *
from tkinter import font,ttk

class watchKeyboard():

    def __init__(self,argv):
        super().__init__()
        if len(argv)>1 :
            self.watch_minutes = int(argv[1])
        else:
            self.watch_minutes = 5
    
    def main(self):
        print('サボりチェッカーです。' + str(self.watch_minutes) + '分キータイプが無い場合に警告します。')
        print('作業終了する場合はctrl + cを押してください')
        try:
            self.watch(0)
            self.warning()
        except KeyboardInterrupt:
            print('作業終了ですね。お疲れ様でした。')
            sys.exit(0)
    
    def watch(self,timeout_count):
        typed_pool = []
        keyboard.start_recording()
        time.sleep(60)
        typed_pool = keyboard.stop_recording()
        if len(typed_pool) == 0:
            timeout_count += 1
        else:
            timeout_count = 0
        if timeout_count < self.watch_minutes:
            self.watch(timeout_count)
        else:
            return
    
    def warning(self):
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
        root.protocol("WM_DELETE_WINDOW", self.main())

if __name__ == "__main__":
    watchKeyboard(sys.argv).main()