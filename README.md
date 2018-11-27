# CwruBaseballAlexa
This codebase is a CWRU Baseball Amazon Alexa Skill. It is deployed to Amazon Web Services to interact with our developed interaction model.

## Getting Started
All necissary back end code is provided in this github project. To run it with Alexa, an interaction model must also be developed on the Alexa Development Console and paired with this github project while this github project is being hosted as a lambda function on AWS. For additional information on how it was deployed, see the Deployment section below.

## How It Works
The Interaction model developed on the Alexa Developer Console recieves voice input and pulls out keywords and values. These values are then sent to a lambda function on AWS which passes this information onto our Python code. Our Python code, using BeautifulSoup, scrapes the requested information from the Case Western Reserve University Athletics baseball website, formulates a sentence response, and sends the response back to Alexa.

## Deployment

### Alexa Developer Console Interaction Model
For access to the Interaction Model used to pull key words and values from verbal input to Alexa, please contact mag210@case.edu. (Unfortunatly these models cannot be easily placed on GitHub)

### Deploying to AWS
1) Create a directory with the all non-testing or code coverage files. (This is mostly python files and BeautifulSoup files)
2) Zip all contents of the directory. ***NOTE: Do not zip the directory itself***
3) Upload the zipped directory as a lambda funciton to AWS.
4) Ensure that your lambda funciton is linked with the interaction model and vice versa
