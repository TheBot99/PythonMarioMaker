import keyboard
from LevelReader import LevelReaderModule

timer = 60

while timer < 61:
    if keyboard.is_pressed('ctrl + l + r'):
        LevelReaderModule("TestLevel", True)
        timer = 65