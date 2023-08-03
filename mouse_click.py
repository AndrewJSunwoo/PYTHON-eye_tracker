import autoit
import time

autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
time.sleep(5)
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[Class:#32770]", "Button2")