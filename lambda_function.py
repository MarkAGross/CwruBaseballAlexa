from __future__ import print_function
from RequestReciever import receiver
from response import response


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        }
    }


def build_response(speechlet_response):
    return {
        'version': '1.0',
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def recieve_request(intent):
    pass
    '''
    title = intent['name']
    input_string = ""
    for slot in intent['slots']:
        if 'value' in slot:
            input_string = input_string + ' '
            input_string = input_string + slot['value']
    rec = reciever(input_string)
    data = []
    data = rec.parse_string()
    response = response()
    speech_output = "Default Response - Error"
    if (len(data) == 28):
        speech_output = reponse.teamResponse(data)
    elif (len(data) == 33):
        speech_output = response.participantResponse(data)
    elif (len(data) == 3):
        speech_output = response.scheduleResponse(data)
    return build_response(build_speechlet_response(title, speech_output))
    '''
    return build_response(build_speechlet_response('case baseball', 'There are some games played'))


# --------------- Events ------------------

def on_intent(intent_request):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "TeamIntent":
        return recieve_request(intent)
    elif intent_name == "TeamParticipantIntent":
        return recieve_request(intent)
    elif intent_name == "ScheduleIntent":
        return recieve_request(intent)
    else:
        raise ValueError("Invalid intent")


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Our skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] != "amzn1.ask.skill.1790770a-d53f-4440-9d01-99f77c3ac33a"):
        raise ValueError("Invalid Application ID")


    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'])
