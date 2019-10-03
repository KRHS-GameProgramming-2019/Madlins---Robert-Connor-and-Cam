from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    
    out = "\n"
    out += "One day me and my friend, " + friendName1
    out += " were out playing " + sport1
    out += "my freind got tired" + freindName1
    out += "my freind and I went over my house"+ friendName1
    
    
    
    return out
