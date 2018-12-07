# CwruBaseballAlexa
This codebase is a CWRU Baseball Amazon Alexa Skill. It is deployed to Amazon Web Services to interact with our developed interaction model on the Amazon Developer Console.
It currently uses AWS Lambda free tier which provides up to 1,000,000 free requests per month and up to 3.2 million seconds of compute power per month.

## Relevant Documents
Inside of the directory titled "Documents" you will find the following files of relevent project documentation:
1. SRS
2. Design Document
3. Functional Test Plan
4. CWRU Baseball Alexa Skill Presentation

## Testing the Code
As outlined in our Functional Test plan, testing for this application occurs in 2 different places. 
1. Testing the recieveing and response generation of Alexa requests can be done at https://aws.amazon.com/free/
    1. Sign into the Amazon Web Services account using my account:   
      *username - mag210@case.edu  
      *password - eecs393grader!  
    2. Select or search for the "lambda" service
    3. Select the CaseBaseball lambda function
    4. At the top of the page there is a drop down menu of all tests we have configured. Select a test and press the "Test" button to run that test.
2. Testing the Fetching code can be done by running the "FullTester.py" file found in this directory.
    1. The code coverage of this Python unit testing can be found in the directory titled "htmlcov".

## Running the Code as an Alexa Skill
1. Log into my Amazon Development Console Account at https://developer.amazon.com/alexa/console/ask  
    *username - mag210@case.edu  
    *password - eecs393grader! 
2. Select the Skill titled CWRU Baseball (Unofficial)
3. At the top of the page, go to "Test"
4. On the left side of the page:
    1. Make sure that "Test is enabled for this skill"
    2. Alexa Simulator is selected
5. To input to Alexa, press and hold the microphone icon while speaking and release the icon when finished talking.
    1. If you choose to type inputs, you may do so bue please be aware, in order to have it be the same input as spoken input, ALL WORDS AND VALUES MUST BE TYPED AS YOU WOULD SAY THEM ENGLISH WORDS.  
    *Example: "5" must be typed as "five"  
    *Example: "2018" must be typed as "twenty eighteen" or "two thousand eighteen"  
    *Example "8th" must be typed as "eighth"  

## Application Functionality (What the Alexa Skill can do)
***Note: All requests must start with "Alexa ask Case Baseball..."***    
***Note 2: This application can handle requests referring to information from 2011 up to the current year***    
***Note 3: This applicaiton runs slow. Unfortunatly there was nothing we could do about this. The problem with the speed, sometimes taking up to 25 seconds to respond to a request, is due solely to the CWRU Athletics website taking so long to connect to. For example, for a request taking 20 seconds to respond, about 18 of those seconds are just waiting to connect to the website.***    
1. Ask For a Team Stat. If no year specified, defaults to current year. For a list of all supported statistics, please see the Design Document in the Documents directory.
    1. "Alexa ask Case baseball for the number of games in twenty seventeen"
    2. "Alexa ask case baseball for the team batting average"
2. Ask for player information or a statistic by player number (Alexa can not interpret player names). If no year is specified, defaults to the current year. For a list of all supported information and statistics, please see the Design Document in the Documents directory.
    1. "Alexa ask case baseball for the name of number thirty three in twenty sixteen"
    2. "Alexa ask case baseball for the number of stolen bases for number twenty nine"
3. Ask for a game/score.
    1. "Alexa ask case baseball for the next game"
    2. "Alexa ask case baseball for the previous game"
    3. "Alexa ask case baseball for the games on April first twenty eighteen"
