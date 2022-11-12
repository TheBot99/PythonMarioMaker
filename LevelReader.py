from gettext import find
from operator import indexOf
from Renderer import RenderDragon
from Renderer import devRenderDragon

Height = 31



def FindHeight():
    HeightOfLevel = open("Level1/Height.mmsd", 'r')
    stringHeightofLevel = "".join(HeightOfLevel.readlines())
    HeightOfLevel.close()
    global Height
    Height = int(stringHeightofLevel) + 1
FindHeight()
    


scanned = 1
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
DictofBlocks = {}
LevelBlocks = {}
LengthofLevel = open("Level1/Length.mmsd", 'r')
stringLengthofLevel = "".join(LengthofLevel.readlines())
intLengthofLevel = int(stringLengthofLevel)
LengthofLevel.close()
intLengthofLevel = intLengthofLevel - 1
converting = False
while scanned != Height:
    stringscanned = str(scanned)
    Row = open(f"Level1/Row{stringscanned}.mmsd", 'r')
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
            devRenderDragon(str(num1), str(scanned), block1)
            if num1 < intLengthofLevel:
                num1 = num1+1
            else:
                scanned = scanned +1
                makingBlock =  False
    else:
        converting = False