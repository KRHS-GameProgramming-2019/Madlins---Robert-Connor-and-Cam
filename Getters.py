def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Plese select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or 
            option == "exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "one" or 
            option == "story 1" or 
            option == "story1"):
                option = "1"
                goodInput = True
            
        else:
            print("Plese make a valid choice")
            
    return option

def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        
    return word
    
def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False
    
    sports = ["soccer",
              "football",
              "hockey",
              "wrestling",
              "rugby",
              "cheese rolling",
              "toe wrestling",
              "basketball",
              "swimming",
              "cricket",
              "tennis",
              "volleyball",
              "track",
              "waterbottle flipping",
              "motorcross",
              "skateboard",
              "archery",
              "fishing",
              "gaming",
              "hunting",
              "badmitten",
              "kickball",
              "ping pong",
              "baseball",
              "Golf",
              "handball",
              "roeing",
              
              
              
              
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print("Don't use language like that")
        elif word.lower() not in sports:
            goodInput = False
            print("Sorry, I don't know that one.")
        
        
    return word
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False


swearList = ["poop",
             "pee",
             "shit",
              "fuck",
              "ass",
              "asshole",
              "dick",
              "bitch",
              "matt chruch",
              "cunt",
              "nigga",
              "nigger",
              "fag",
              "dick",
              "motherfucker"
              "slut"
              "hoe"
              "bastard"
              "damn"
              "holy shit"
              "hell"
              "horseshit"
              "goddamn"
              "bastard"
              "asshole"
              "jesus christ"
              "christ on a bike"
              "child-fucker"
              "christ on a cracker"
              "jesus fuck"
              "prick"
              "shithead"
              "shitface"
              "shitass"
              "wiseass"
              "whore"
              "retard"
              "Fagot"
              "douchebag"
              "twat"
              "bastard"
              
              
              

