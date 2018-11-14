

class response(object):

    #create mock list of player info
    #creat func that takes list and outputs sentance

    teamGamesPlayedCurr = ["The CWRU Baseball team has played" , "games this year"]
    teamGamesPlayed = ["The CWRU Baseball team played" , "in"]
    teamAtBatsCurr = []
    teamAtBats = []
    team = []

    testTeamStat = ["RBIs", "52", "2018"]
    testPlayerStat = ["12", "RBIs", "17", "2018"]
    testError = ["x"]

    def response(keyList):
        statString = ""
        playerString = ""
        statNumString = ""
        yearString = ""
        

        count = len(keyList)
            
        print(count)

        if(count == 3):
            
            for x in range(len(keyList)):
              statString = keyList[0] 
              statNumString = keyList[1] 
              yearString = keyList[2]

            print("The CWRU Baseball team has "+ statNumString +" "+ statString + " in " + yearString)

        elif(count == 4):
          for x in range(len(keyList)):
              playerString = keyList[0]
              statString = keyList[1] 
              statNumString = keyList[2] 
              yearString = keyList[3]

          print("Player No." +playerString+ " has " + statNumString + " " + statString + " in " + yearString)

        elif(count <= 2):
          print("Sorry I did not retrieve enough infomation to answer your question")


    response(testTeamStat)
    response(testPlayerStat)
    response(testError)