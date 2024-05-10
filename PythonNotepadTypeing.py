import pyautogui

# Open Notepad (adjust the path if needed)
pyautogui.hotkey('win', 'r')  # Open Run dialog
import os

# Open D drive
os.startfile("D:")

pyautogui.write('notepad')  # Type "notepad"
pyautogui.press('enter')  # Press Enter to open

# Type some text into Notepad
myStr=input("Type something you want to write : ")
pyautogui.typewrite("This text is typed using Python!")

# Close Notepad (feel free to modify for saving)
# pyautogui.hotkey('alt', 'f4') 