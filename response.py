
from error import LACK_OF_TEAM_INFORMATION_ERROR
from error import LACK_OF_PARTICIPANT_INFORMATION_ERROR
from schedule import game
class response(object):

    #create mock list of player info
    #creat func that takes list and outputs sentance

   
    

    testTeamStat = [None] * 28
    testTeamStat[2] = "15"
    testTeamStat[26] = "2018"
    testPlayerStat = [None] * 33
    testPlayerStat[7] = 42
    testPlayerStat[31] = 29
    testPlayerStat[32] = "2018"
    data = []
    gameObj = game(data)
    gameObj.month = "April"
    gameObj.day = 25
    gameObj.opponent_name = "#2 Wooster"
    gameObj.result = "L, 11-6"
    testSchedule = [None] * 3
    testSchedule[1] = gameObj
    testSchedule[2] = "2018"


    #function to format and return information about team stats
    def teamResponse(self, keyList):
        teamStatList = ["Games","At Bats", "Runs", "Hits", "Doubles", "Triples", "Home runs",
                    "RBIs", "Extra Base Hits", "Total Bases", "Walks", "Hit by pitches",
                    "Strikeouts", "Sacrifice flies", "Sacrifice hits", "Hits into double play",
                    "Stolen bases", "Caught stealing", "Batting average", "On base percentage",
                    "Slugging percentage", "ERA", "Shutouts", "At bats against",
                    "Batting average against", "Home attendance", "Home attendance average", "YearFirst","YearSecond"]
        count = 0
        statArray = []
        indexList = []
        nameStatArray = []
        statString = ""
        statNumString = ""
        yearString = ""
        printString = ""
       
        for i in range(len(keyList)):
            if keyList[i] is not None:
                statArray.append(keyList[i])
                indexList.append(i)
                count +=1



        
        try:
            for i in range(len(indexList)):
                nameStatArray.append(teamStatList[indexList[i]])

            statString = nameStatArray[0]
            statNumString = str(statArray[0])
            yearString = str(statArray[1])

            
            printString = "The CWRU Baseball team has "+ statNumString +" "+ statString + " in " + yearString
            print("The CWRU Baseball team has "+ statNumString +" "+ statString + " in " + yearString)
        except IndexError:
            print("Unable to retrieve sufficient information for this team stat")
            
            #raise LACK_OF_TEAM_INFORMATION_ERROR("Unable to retrieve sufficient information for this team stat")
            

        
        

        
        return(printString)

       

        

    #function to format and return information about individual participant stats
    def participantResponse(self, keyList):
        participantStatList = ["Name", "Position", "Bats and throws", "Height", "Weight", "Academic Year",
                           "Hometown and high school", "Games played", "At bats", "Runs", "Hits",
                           "Doubles", "Triples", "Home runs", "RBIs", "Walks", "Strikeouts",
                           "Stolen Bases", "Batting Average", "On base percentage", "Slugging percentage",
                           "Appearances", "Game starts", "Wins", "Losses", "Saves", "Complete games",
                           "Innings pitched", "Strikeouts per 9 innings", "Earned runs", "ERA", "Player number", "Year"]
        count = 0
        statArray = []
        indexList = []
        nameStatArray = []
        statString = ""
        statNumString = ""
        playerString = ""
        yearString = ""
        printString = ""
        
        for i in range(len(keyList)):
            if keyList[i] is not None:
                statArray.append(keyList[i])
                indexList.append(i)
                count +=1

            
        
        try:
            for i in range(len(indexList)):
                nameStatArray.append(participantStatList[indexList[i]])

            statString = nameStatArray[0]
            statNumString = str(statArray[0])
            yearString = str(statArray[2])
            playerString = str(statArray[1])
            printString = "Player No." + playerString + " has " + statNumString + " " + statString + " in " + yearString
            print("Player No." + playerString + " has " + statNumString + " " + statString + " in " + yearString)
            
        except IndexError:
            print("Unable to retrieve sufficient information for this team stat")
            #raise LACK_OF_PARTICIPANT_INFORMATION_ERROR("Unable to retrieve sufficient information for this team stat")


        
        return(printString)
        
            
            
        

    #function to format and return information about team schedule
    def scheduleResponse(self, keyList):
        scheduleStatList = ["Next game", "Previous game", "Year"]
        count = 0
        statArray = []
        indexList = []
        nameStatArray = []
        printString = ""

        if keyList[2] is None:
            keyList[2] = "2018"

        for i in range(len(keyList)):
            if keyList[i] is not None:
                statArray.append(keyList[i])
                indexList.append(i)
                count +=1
            elif keyList[i] is None:
                statArray.append(-1)
                
        
        try:
            for i in range(len(indexList)):
                nameStatArray.append(scheduleStatList[indexList[i]])
        
            
        

            printString =""
            
            if(statArray[0] == -1):
                
                empty = []
                gameObj = game(empty)
                gameObj  = statArray[1]
                monthString = str(gameObj.month)
                dayString = str(gameObj.day)
                oppString = gameObj.opponent_name
                resultString = gameObj.result
                yearString = statArray[1]
                printString = "CWRU baseball team played " + oppString+ " on the " +dayString+ " of "+monthString+ ", and the result was " + resultString+ "." 
                print("CWRU baseball team played " + oppString+ " on the " +dayString+ " of "+monthString+ ", and the result was " + resultString+ "." )
            elif(statArray[1] == -1):
                empty = []
                gameObj = game(empty)
                gameObj  = statArray[0][0]
                monthString = gameObj.month
                dayString = str(gameObj.day)
                oppString = gameObj.opponent_name
                resultString = gameObj.result
                yearString = statArray[1]
                printString = "CWRU baseball team will play " + oppString+ " on the " +dayString+ " of "+monthString+ "." 
                print("CWRU baseball team will play " + oppString+ " on the " +dayString+ " of "+monthString+ "." )


        except (IndexError , AttributeError):
            printprint("Unable to retrieve sufficient information for this team stat")
            #raise LACK_OF_TEAM_INFORMATION_ERROR("Unable to retrieve sufficient information for this schedule inquiry")
        

        


        return(printString)
        


    #Make if statement to check if previous game or next game


    
    #teamResponse(testTeamStat)
    #participantResponse(testPlayerStat)
    #scheduleResponse(testSchedule)

