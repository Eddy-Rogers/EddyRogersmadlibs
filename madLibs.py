#I made this on a topic that people may not know by heart, so ive included all of the correct answers below.
#Easy: 1 = Jazz, 2 = 1967, 3 = Pulitzer, 4 = Davis
#Medium: 1 = Navy, 2 = Melody, 3 = Pearl, 4 = 1946
#Hard: 1 = Giant, 2 = Coltrane, 3 = Major, 4 = Augmented

#Text for the game, with an array of answers below each

easyText =  """            John Coltrane was one of the world's most renowned __(1)__ musicians known for being one of, if not the
            best, tenor saxophone players in history. Coltrane was born on September 23, 1926, and died
            on July 17, __(2)__. He received various honors throughout his life, including a special __(3)__ prize
            in 2007. He had a strong rivalry with Miles __(4)__, and the two musicians strove to play better than
            each other.
            """

easyans = ["jazz","1967","pulitzer","davis"]

medText =   """           To avoid being drafted by the US Army, Coltrane joined the US __(1)__ in 1945. His musical talent was
            quickly recognized, and he joined the Navy swing band, the __(2)__ Masters, while he was stationed in
            __(3)__ Harbor, Hawaii. His first recordings were informal tapes, recorded while he was in Hawaii.
            He was discharged from the Navy in __(4)__.
            """

medans = ["navy","melody","pearl","1946"]

hardText =  """            __(1)__ Steps was Coltrane's first album as a leader for Atlantic Records, recorded in 1959. It involved
            __(2)__ changes, which involves substitution for rather common ii-V-i chord progressions. It also utilized
            cyclical chordal root movements in ascending or descending __(3)__ thirds. The root of each chord combined
            forms a(n) __(4)__ triad.
            """

hardans = ["giant","coltrane","major","augmented"]

blanks = ["__(1)__","__(2)__","__(3)__","__(4)__"]

global limit_attempts

limit_attempts = 0

def getChances():
    #Retrieves the number of desired chances from the user, and checks that numbers validity.
    global chances
    chancesStr = raw_input("How many chances would you like to have to correct a wrong answer?\n")
    chances = int(chancesStr)
    check = True
    while(check):
        if (chances > limit_attempts):
            print ("Excellent. You now have " + chancesStr + " chances.\n")
            check = False
            break
        if (chances == limit_attempts):
            print ("Bold move. Good Luck.\n")
            check = False
            break
        else:
            print ("Please enter a valid number\n.")
            getChances()

               
def selectDif():
    #Allows the user to select difficulty and while the input is not one of the choices, asks to user to input a valid difficulty.
    global difChoice
    difChoice = raw_input("What would you like your game difficulty to be? Enter 'Easy', 'Medium', or 'Hard'.\n").lower()
    while difChoice not in ["easy","medium","hard"]:
        print "Sorry, " + difChoice + " is not an option!"
        difChoice = raw_input("What would you like your game difficulty to be? Enter 'Easy', 'Medium', or 'Hard'.\n").lower()

def replace_blanks(quiz,answers,blanks,chances):
    index = 0
    #If index = 4, the game is finished.
    end_game = 4
    print quiz
    while chances > limit_attempts:
        if (index == end_game):
            #Checks if the game should be over
            print "Congratulations! You won!\n"
            play_game()
        userinput = raw_input("What is the correct answer in place of blank " + str(index + 1) + "? ").lower()
        if userinput == answers[index]:
            print "Correct!"
            #replaces a blank with the correct answer
            new_quiz = quiz.replace(blanks[index],answers[index])
            quiz = new_quiz
            print new_quiz
            index += 1
        else:
            print "Incorrect."
            chances -= 1
            print "You have " + str(chances) + " chances left."
    


def playGame():
    #Executes the game based on the selection made by the user.
    selectDif()
    getChances()
    if difChoice == "easy":
        replace_blanks(easyText,easyans,blanks,chances)
    if difChoice == "medium":
        replace_blanks(medText,medans,blanks,chances)
    if difChoice == "hard":
        replace_blanks(hardText,hardans,blanks,chances)

playGame()
