import time
import webbrowser

breaks = 2
break_count = 0

print("This program started on "+time.ctime())
while (break_count < breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=I1188GO4p1E")
    break_count - break_count + 1
