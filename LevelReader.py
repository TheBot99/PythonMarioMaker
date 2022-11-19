from gettext import find
from operator import indexOf
from Renderer import RenderDragon
# Path: Renderer.py used for rendering the level
from Renderer import devRenderDragon
# Path: Renderer.py used for rendering the level but also gives debug info such as coordinates and block type


def LevelReaderModule(Level, devMode):

    def FindLenght():
        # Find the lenght of the level
        fileLengthofLevel = open(f"{Level}/Length.mmsd", 'r')
        # Opens the length file
        stringLengthofLevel = "".join(fileLengthofLevel.readlines())
        # Reads the length file
        global LengthofLevel
        # Makes the LengthofLevel variable global
        LengthofLevel = int(stringLengthofLevel)
        # Converts the string to an integer
        fileLengthofLevel.close()
        # Closes the length file
        LengthofLevel = LengthofLevel - 1
        # Subtracts 1 from the length of the level
    FindLenght()

    def FindHeight():
        # Finds the height of the level
        HeightOfLevel = open(f"{Level}/Height.mmsd", 'r')
        # Opens the height file
        stringHeightofLevel = "".join(HeightOfLevel.readlines())
        # Reads the height file
        HeightOfLevel.close()
        # Closes the height file
        global Height
        # Makes the height variable global
        Height = int(stringHeightofLevel) + 1
        # Sets the height variable to the height of the level
    FindHeight()
    # Calls the FindHeight function
        


    scanned = 1
    # Sets the scanned variable to 1 changes after scanning each row
    Blocks = {"0":"Koopa", "1":"Bob-omb", "2":"Boo", "3":"DryBones", "4":"Piranah Plant",
    "5":"Goomba", "6":"Spiny", "7":"Wiggler", "8":"Yoshi", "9":"Bowser", "A":"Warp Pipe", "B":"Mushroom Platform",
    "C":"Conveyer Belt", "D":"Key door", "E":"Warp door", "F":"P Warp Door", "G":"Coin", "H":"Brick", "I":"? Block", "J":"Ground", "K":"Donut Block", "L":"Ice", "M":"Pink coin",
    "N":"Track", "O":"Rotating Block", "P":"Note Block", "Q":"Hidden Block", "R":"Vine", "S":"1-up", "T":"Big Mushroom", "U":"Cape Feather", "V":"Fire Flower", "W":"Goomba Shoe", "X":"Goomba's Stiletto",
        "Y":"Mystery Mushroom", "Z":"Propeller Mushroom", "a":"Super Leaf", "b":"Super Mushroom", "c":"Super Star", "d":"Pipe", "e":"One-Way Wall", "f":"P Switch", "g":"POW Block", "h":"Shell Helmet", "i":"Thwomp",
        "j":"Shell Helmet", "k":"Skewer", "l":"Trampoline", "m":"Unchained Chomp", "n":"Yoshi Egg", "o":"Bowser Jr.", "p":"Jelectro", "q":"Spike Trap", "r":"Cloud Block", "s":"Cannon", "t":"Chain Chomp",
        "u":"Cheep Cheep", "v":"Fire Bar", "w":"", "x":"", "y":"", "z":"", "!":"", "@":"", "#":"", "$":"", "%":"",
        "^":"", "&":"", "*":"", "(":"", ")":"", "-":"", "_":"", "+":"", "=":"", "[":"", "]":"",
            "{":"", "}":"", "|":"", ":":"", ";":"", "<":"", ">":"", "?":"", "/":"", "'":"", ",":"",
            ".":"", "~":"", "`":""}
    # Dictionary of all the blocks in the game
    # The key is the block ID and the value is the block name
    LevelBlocks = {}
    # Dictionary of all the blocks in the level after being read
    converting = False
    while scanned != Height:
        stringscanned = str(scanned)
        Row = open(f"{Level}/Row{stringscanned}.mmsd", 'r')
        stringofRow = "".join(Row.readlines())
        LevelBlocks[scanned] = stringofRow
        scanned = scanned + 1
        converting = True
    scanned = 1
    while converting == True:
        if scanned != Height:
            num1 = 0
            stringOfRow = LevelBlocks[scanned]
            makingBlock = True
            while makingBlock == True:
                numbblock1 = stringOfRow[num1]
                block1 = Blocks[numbblock1]
                if devMode == True:
                    devRenderDragon(str(num1), str(scanned), block1)
                else:
                    RenderDragon(str(num1), str(scanned), block1)
                if num1 < LengthofLevel:
                    num1 = num1+1
                else:
                    scanned = scanned +1
                    makingBlock =  False
        else:
            converting = False