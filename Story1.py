from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    game = getWord ("Type an Xbox game: ", debug)
    food = getWord("Type a food: ", debug)
    
    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1 
    out += ", we both got tired and " + friendName1
    out += " and I went over to my house "
    out += " to play "+ game
    out += ", he lost and I won "
    out += ", we got " + food + " to eat"
    out += " and we went back outside and played " + sport1
    out += ", my freind decided to sleep over "
    out += " so we pulled an all nighter "
    out += " during the night we played chopped "
    out += " and the loser had too jump in the cold pond "
    out += " he ended up winning as my dish was terrible, I made " + food
    out += ", because I lost i had to jump in the pond "
    out += " the next day my freind went home and I had to get ready for a football game "
    
    
    return out
