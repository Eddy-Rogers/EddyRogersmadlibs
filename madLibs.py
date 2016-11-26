#I made this on a topic that people may not know by heart, so ive included all of the correct answers below.
#Easy: 1 = Jazz, 2 = 1967, 3 = Pulitzer, 4 = Davis
#Medium: 1 = Navy, 2 = Melody, 3 = Pearl, 4 = 1946
#Hard: 1 = Giant, 2 = Coltrane, 3 = Major, 4 = Augmented

#Text for the game
global easyText
easyText = "\n\n"
easyText += "John Coltrane was one of the world's most renowned __(1)__ musicians known for being one of, if not the\n"
easyText += "best, tenor saxophone players in history. Coltrane was born on September 23, 1926, and died\n"
easyText += "on July 17, __(2)__. He received various honors throughout his life, including a special __(3)__ prize\n"
easyText += "in 2007. He had a strong rivalry with Miles __(4)__, and the two musicians strove to play better than\n"
easyText += "each other.\n"

#Subdivided sentences for the easy text.
global eaSent1
eaSent1 = "John Coltrane was one of the world's most renowned __(1)__ musicians known for being one of, if not the "
eaSent1 += "best, tenor saxophone players in history."

global eaSent2
eaSent2 = "Coltrane was born on September 23, 1926, and died on July 17, __(2)__."

global eaSent3
eaSent3 = "He received various honors throughout his life, including a special __(3)__ prize in 2007."

global eaSent4
eaSent4 = "He had a strong rivalry with Miles __(4)__, and the two musicians strove to play better than "
eaSent4 += "each other."

global medText
medText = "\n\n"
medText += "To avoid being drafted by the US Army, Coltrane joined the US __(1)__ in 1945. His musical talent was\n"
medText += "quickly recognized, and he joined the Navy swing band, the __(2)__ Masters, while he was stationed in\n"
medText += "__(3)__ Harbor, Hawaii. His first recordings were informal tapes, recorded while he was in Hawaii.\n"
medText += "He was discharged from the Navy in __(4)__.\n\n"

#Subdivided sentences for the medium text.
global medSent1
medSent1 = "To avoid being drafted by the US Army, Coltrane joined the US __(1)__ in 1945."

global medSent2
medSent2 = "His musical talent was quickly recognized, and he joined the Navy swing band, the __(2)__ Masters, while he was stationed in __(3)__ Harbor, Hawaii."

global medSent3
medSent3 = "He was discharged from the Navy in __(4)__."

global hardText
hardText = "\n\n"
hardText += "__(1)__ Steps was Coltrane's first album as a leader for Atlantic Records, recorded in 1959. It involved\n"
hardText += "__(2)__ changes, which involves substitution for rather common ii-V-i chord progressions. It also utilized\n"
hardText += "cyclical chordal root movements in ascending or descending __(3)__ thirds. The root of each chord combined\n"
hardText += "forms a(n) __(4)__ triad.\n"

#Subdivided sentences for the medium text.

global haSent1
haSent1 = "__(1)__ Steps was Coltrane's first album as a leader for Atlantic Records, recorded in 1959."

global haSent2
haSent2 = "It involved __(2)__ changes, which includes substitution for rather common ii-V-i chord progressions."
global haSent3
haSent3 = "It also utilized cyclical chordal root movements in ascending or descending __(3)__ thirds."

global haSent4
haSent4 = "The root of each chord combined forms a(n) __(4)__ triad."

global userPrompt
userPrompt = "What is the correct answer in place of blank"

def getChances():
    #Retrieves the number of desired chances from the user, and checks that numbers validity.
    global chances
    chancesStr = raw_input("How many chances would you like to have to correct a wrong answer?\n")
    chances = int(chancesStr)
    check = True
    while(check):
        if (chances > 0):
            print ("Excellent. You now have " + chancesStr + " chances.")
            check = False
            break
        if (chances == 0):
            print ("Bold move. Good Luck.")
            check = False
            break
        else:
            print ("Please enter a valid number\n.")
            getChances()

               
def selectDif():
    #Allows the user to select difficulty and while the input is not one of the choices, asks to user to input a valid difficulty.
    global difChoice
    difChoice = raw_input("What would you like your game difficulty to be? Enter 'Easy', 'Medium', or 'Hard'.\n").lower()
    check = True
    while(check):
        if(difChoice == "easy" or difChoice == "medium" or difChoice == "hard"):
            flag = False
            break
        else:
            print "Sorry, " + difChoice + " is not an option!"
            difChoice = raw_input("What would you like your game difficulty to be? Enter 'Easy', 'Medium', or 'Hard'\n").lower()

def getAnswer(numLoc):
    #Retrieves the user's answer based on the number it is given.
    global difChoice
    if difChoice == "easy":
        if numLoc == 1:
            ansLoc = raw_input(userPrompt + " 1?\n").lower()
        if numLoc == 2:
            ansLoc = raw_input(userPrompt + " 2?\n").lower()
        if numLoc == 3:
            ansLoc = raw_input(userPrompt + " 3?\n").lower()
        if numLoc == 4:
            ansLoc = raw_input(userPrompt + " 4?\n").lower()
    if difChoice == "medium":
        if numLoc == 1:
            ansLoc = raw_input(userPrompt + " 1?\n").lower()
        if numLoc == 2:
            ansLoc = raw_input(userPrompt + " 2?\n").lower()
        if numLoc == 3:
            ansLoc = raw_input(userPrompt + " 3?\n").lower()
        if numLoc == 4:
            ansLoc = raw_input(userPrompt + " 4?\n").lower()
    if difChoice == "hard":
        if numLoc == 1:
            ansLoc = raw_input(userPrompt + " 1?\n").lower()
        if numLoc == 2:
            ansLoc = raw_input(userPrompt + " 2?\n").lower()
        if numLoc == 3:
            ansLoc = raw_input(userPrompt + " 3?\n").lower()
        if numLoc == 4:
            ansLoc = raw_input(userPrompt + " 4?\n").lower()
    global ans
    ans = ansLoc
    global num
    num = numLoc

def checkAnswer(correctAns):
    #Checks if the user's input is correct based on the correct answer, continues the program if it does, and restarts the process if it doesn't.
    #It also checks if the user still has lives left.
    global chances
    check = True
    while(check):
        if(ans == correctAns):
            print ("Correct!\n")
            break
        else:
            print("Sorry, " + ans + " is not the correct answer!\n")
            if (chances == 0):
                print ("You are out of chances.\n\nGAME OVER")
                playGame()
            else:
                chances = chances - 1
                print ("You have " + str(chances) + " chances left.\n")
            getAnswer(num)

def easyGame():
    #Code for if "Easy" difficulty is chosen.
    print easyText
    print eaSent1 + "\n"
    getAnswer(1)
    checkAnswer("jazz")
    correct1 = eaSent1[:51] + "jazz" + eaSent1[58:]
    print correct1 + "\n"
    print eaSent2 + "\n"
    getAnswer(2)
    checkAnswer("1967")
    correct2 = eaSent2[:61] + "1967."
    print correct2 + "\n"
    print eaSent3 + "\n"
    getAnswer(3)
    checkAnswer("pulitzer")
    correct3 = eaSent3[:68] + "Pulitzer" + eaSent3[75:]
    print correct3 + "\n"
    print eaSent4 + "\n"
    getAnswer(4)
    checkAnswer("davis")
    correct4 = eaSent4[:35] + "Davis" + eaSent4[42:]
    print correct4 + "\n"
    print "Well Done! You have filled out all of the blanks.\n"
    print correct1 + " " + correct2 + " " + correct3 + " " + correct4 + "\n"

def medGame():
    #Code for if "Medium" difficulty is chosen.
    print medText
    print medSent1 + "\n"
    getAnswer(1)
    checkAnswer("navy")
    correct1 = medSent1[:62] + "Navy" + medSent1[69:]
    print correct1 + "\n"
    print medSent2 + "\n"
    getAnswer(2)
    checkAnswer("melody")
    print medSent2[:82] + "Melody" + medSent2[89:] + "\n"
    getAnswer(3)
    checkAnswer("pearl")
    correct2 = medSent2[:82] + "Melody" + medSent2[89:125] + "Pearl" + medSent2[132:]
    print correct2 + "\n"
    print medSent3 + "\n"
    getAnswer(4)
    checkAnswer("1946")
    correct3 = medSent3[:35] + "1946" + medSent3[42:]
    print correct3 + "\n"
    print "Well Done! You have filled out all of the blanks.\n"
    print correct1 + " " + correct2 + " " + correct3 + "\n"

def hardGame():
    #Code for if "Hard" difficulty is chosen.
    print hardText
    print haSent1 + "\n"
    getAnswer(1)
    checkAnswer("giant")
    correct1 = "Giant" + haSent1[7:]
    print correct1 + "\n"
    print haSent2 + "\n"
    getAnswer(2)
    checkAnswer("coltrane")
    correct2 = haSent2[:12] + "Coltrane" + haSent2[19:]
    print correct2 + "\n"
    print haSent3 + "\n"
    getAnswer(3)
    checkAnswer("major")
    correct3 = haSent3[:76] + " major" + haSent3[83:]
    print correct3 + "\n"
    print haSent4 + "\n"
    getAnswer(4)
    checkAnswer("augmented")
    correct4 = haSent4[:42] + "augmented" + haSent4[50:] + "\n"
    print correct4
    print "Well Done! You have filled out all of the blanks.\n"
    print correct1 + " " + correct2 + " " + correct3 + " " + correct4 + "\n"

def playGame():
    #Executes the game based on the selection made by the user.
    selectDif()
    getChances()
    if difChoice == "easy":
        easyGame()
        playGame()
    if difChoice == "medium":
        medGame()
        playGame()
    if difChoice == "hard":
        hardGame()
        playGame()

playGame()
