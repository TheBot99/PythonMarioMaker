import keyboard
import time



def Manuel():
    print("This is the Manuel Level Writer only meant for dev purposes")
    print("If you entered this by accident type 'exit' to exit in the console")
    print("If you want to use this type 'start' to start the level writer")
    print("If you want to exit this at any time after starting a wirte type 'exit' to exit in the console")
    print("After you click enter the level auto matically saves")
    startinput = input("Type 'start' to start the level writer or 'exit' to exit in the console: ")
    if startinput == "start":
        Level = 1
        while Level < 31:
            Levelstr = str(Level)
            print("Level " + Levelstr)
            LevelOpened = open(f"Level1/Row{Levelstr}.mmsd", 'w')
            UserInput = input("Enter a Level: ")
            if UserInput == "exit":
                print("Exiting...")
                break
            LevelOpened.write(UserInput)
            LevelOpened.close()
            Level += 1
    elif startinput == "exit":
        print("Exiting...")
        exit()
    else:
        print("Invalid Input")
        Manuel()


def devAutomatic():
    print("This is the automatic level writer only meant for use by the game")
    print("If you are seeing this you are looking at the devleoper prompt and put the game in dev mode")
    print("If you want to exit this type 'exit' in the console")
    print("If you want to start this type 'start' in the console")
    startinput = input("Type 'start' to start the level writer or 'exit' to exit in the console: ")
    if startinput == "start" or "exit":
        if startinput == "start":
            wantDebug = True
            while wantDebug == True:
                justprintedString = "Test"
                print(justprintedString)
                debuginput = input("Type 'continue' to continue debugging or anything else to exit debugging: ")
                if debuginput == "continue":
                    wantDebug = True
                else:
                    wantDebug = False
                    exit()
        if startinput == "exit":
            print("Exiting...")
            exit()
    if startinput != "start" or "exit":
        print("Invalid Input")
        devAutomatic()

def Automatic():
    print("Automatic Level Writer")

timer = 0
while timer < 61:
    if keyboard.is_pressed('ctrl + m'):
        Manuel()
        timer = 71
    if keyboard.is_pressed('ctrl + d + a'):
        devAutomatic()
        timer = 71
    time.sleep(0.01)
    timer += 1
if timer == 61:
    Automatic()     