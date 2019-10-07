from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    game = getWord ("Type an Xbox game: ", debug)
    snack = getWord("Type a snack: ", debug)
    
    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " were out playing " + sport1
    out += + freindName1 + " got tired " + friendName1
    out += " freindName and I went over my house "+ friendName1
    out += " we played Xbox "+ game
    out += " he lost and I won "
    out += "we got " + snack + " to eat"
    out +=  "we went back outside and played " + sport1
    out += " my freind decided to sleep over "
    out += " we pulled an all nighter "
    out += " during the night we played chopped "
    out += " the loser had too jump in the cold pond "
    out += " he ended up winning as my dish was terrible "
    out += " because I lost i had to jump in the pond "
    out += " the next day my freind went home and I had to get ready for a football game "
    
    
    return out
