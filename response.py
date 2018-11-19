
from error import LACK_OF_TEAM_INFORMATION_ERROR
from error import LACK_OF_PARTICIPANT_INFORMATION_ERROR
class response(object):

    #create mock list of player info
    #creat func that takes list and outputs sentance

   
    

    testTeamStat = [None] * 27
    testTeamStat[2] = "15"
    testTeamStat[26] = "2018"
    testPlayerStat = [None] * 33
    testPlayerStat[5] = "SR."
    testPlayerStat[32] = "2017"


    #function to format and return information about team stats
    def teamResponse(self, keyList):
        teamStatList = ["Games","At Bats", "Runs", "Hits", "Doubles", "Triples", "Home runs"
                    "RBIs", "Extra Base Hits", "Total Bases", "Walks", "Hit by pitches",
                    "Strikeouts", "Sacrifice flies", "Sacrifice hits", "Hits into double play",
                    "Stolen bases", "Caught stealing", "Batting average", "On base percentage",
                    "Slugging percentage", "ERA", "Shutouts", "At bats against",
                    "Batting average against", "Home attendance", "Home attendance average", "Year","Year"]
        count = 0
        statArray = []
        indexList = []
        nameStatArray = []
        statString = ""
        statNumString = ""
        yearString = ""

       
        for i in range(len(keyList)):
            if keyList[i] is not None:
                statArray.append(keyList[i])
                indexList.append(i)
                count +=1
        #if statement to be removed later when exception handling works
        print(indexList)
        print(statArray)
        if(count<=1):
            print("Unable to retrieve sufficent information")
        else:
            for i in range(len(indexList)):
                
                nameStatArray.append(teamStatList[indexList[i]])
                

        
            statString = nameStatArray[0]
            statNumString = statArray[0]
            yearString = str(statArray[1])
            print("The CWRU Baseball team has "+ statNumString +" "+ statString + " in " + yearString)

       # except:
            #raise LACK_OF_TEAM_INFORMATION_ERROR

        #print(statArray)
        #print(indexList)
        #print(nameStatArray)

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

        #try:
        for i in range(len(keyList)):
            if keyList[i] is not None:
                statArray.append(keyList[i])
                indexList.append(i)
                count +=1
        #if statement to be removed later when exception handling works
        if(count<=2):
            print("Unable to retrieve sufficent information")

        for i in range(len(indexList)):
            nameStatArray.append(participantStatList[indexList[i]])
        else:
            statString = nameStatArray[0]
            statNumString = statArray[0]
            yearString = str(statArray[2])
            playerString = statArray[1]
            print(statArray)

            print("Player No." + playerString + " has " + statNumString + " " + statString + " in " + yearString)
        
        #except:
            #raise LACK_OF_PARTICIPANT_INFORMATION_ERROR
            
        #print(statArray)
        #print(indexList)
        #print(nameStatArray)

    #function to format and return information about team schedule
    def scheduleResponse(self, keyList):
        scheduleStatList = ["Next game", "Previous game", "Year"]
        count = 0
        statArray = []
        indexList = []
        nameStatArray = []
        statString = ""
        statNumString = ""
        playerString = ""
        yearString = ""

        for i in range(len(keyList)):
            if keyList[i] is not None:
                statArray.append(keyList[i])
                indexList.append(i)
                count +=1
                print(statArray)

        for i in range(len(indexList)):
            nameStatArray.append(scheduleStatList[indexList[i]])

        statString = nameStatArray[0]
        #statNumString = statArray[0]
        yearString = statArray[0]
        

        print("inside schedule response")
        
        





    #response(testTeamStat)
    #response(testPlayerStat)
    #response(testError)
    #teamResponse(testTeamStat)
    #participantResponse(testPlayerStat)
