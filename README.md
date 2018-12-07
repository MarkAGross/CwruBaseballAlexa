# CwruBaseballAlexa
This codebase is a CWRU Baseball Amazon Alexa Skill. It is deployed to Amazon Web Services to interact with our developed interaction model on the Amazon Developer Console.
It currently uses AWS Lambda free tier which provides up to 1,000,000 free requests per month and up to 3.2 million seconds of compute power per month.

## Relevant Documents
Inside of the directory titled "Documents" you will find the following files of relevent project documentation:
1) SRS
2) Design Document
3) Functional Test Plan

## Testing the Code
As outlined in our Functional Test plan, testing for this application occurs in 2 different places. 
1) Testing the recieveing and response generation of Alexa requests can be done at https://aws.amazon.com/free/
  a) Sign into the Amazon Web Services account using my account: 
      username - mag210@case.edu 
      password - grade
  b) Select or search for the "lambda" service
  c) Select the CaseBaseball lambda function
  d) At the top of the page there is a drop down menu of all tests we have configured. Select a test and press the "Test" button to run that test.
2) Testing the Fetching code can be done by running the "FullTester.py" file found in this directory.
  a) The code coverage of this Python unit testing can be found in the directory titled "htmlcov".

## Running the Code as an Alexa Skill
1) Log into my Amazon Development Console Account at https://developer.amazon.com/alexa/console/ask
    username - mag210@case.edu
    password - grade
2) Select the Skill titled CWRU Baseball (Unofficial)
3) At the top of the page, go to "Test"
4) On the left side of the page:
  a) Make sure that "Test is enabled for this skill"
  b) Alexa Simulator is selected
5) To input to Alexa, press and hold the microphone icon while speaking and release the icon when finished talking.
  a) If you choose to type inputs, you may do so bue please be aware, in order to have it be the same input as spoken input, ALL WORDS AND VALUES MUST BE TYPED AS YOU WOULD SAY THEM ENGLISH WORDS. 
    i) Example: "5" must be typed as "five"
    ii) Example: "2018" must be typed as "twenty eighteen" or "two thousand eighteen"
    iii) Example "8th" must be typed as "eighth"

