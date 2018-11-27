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

def recieve_bad_request(intent):
    return build_response(build_speechlet_response('case baseball', "Sorry, Case Baseball could not find what you asked."))

def recieve_team_request(intent):
    title = intent['name']
    input_string = ""
    if 'team_stat_type' in intent['slots']:
        if 'value' in intent['slots']['team_stat_type']:
            input_string = intent['slots']['team_stat_type']['value']
            input_string = input_string + " "
    if 'year' in intent['slots']:
        if 'value' in intent['slots']['year']:
            input_string = input_string + intent['slots']['year']['value']
    return get_output(title, input_string)


def recieve_team_participant_request(intent):
    title = intent['name']
    input_string = ""
    if 'team_participant_stat_type' in intent['slots']:
        if 'value' in intent['slots']['team_participant_stat_type']:
            input_string = intent['slots']['team_participant_stat_type']['value']
            input_string = input_string + " "
    if 'player_number'in intent['slots']:
        if 'value' in intent['slots']['player_number']:
            input_string = input_string + intent['slots']['player_number']['value']
            input_string = input_string + " "
    if 'year' in intent['slots']:
        if 'value' in intent['slots']['year']:
            input_string = input_string + intent['slots']['year']['value']
    return get_output(title, input_string)

def recieve_schedule_request(intent):
    title = intent['name']
    input_string = ""
    if 'month' in intent['slots']:
        if 'value' in intent['slots']['month']:
            input_string = intent['slots']['month']['value']
            input_string = input_string + " "
    if 'day'in intent['slots']:
        if 'value' in intent['slots']['day']:
            input_string = input_string + intent['slots']['day']['value']
            input_string = input_string + " "
    if 'year' in intent['slots']:
        if 'value' in intent['slots']['year']:
            input_string = input_string + intent['slots']['year']['value']
            input_string = anser + " "
    if 'previous_game_or_next_game' in intent['slots']:
        if 'value' in intent['slots']['previous_game_or_next_game']:
            input_string = input_string + intent['slots']['previous_game_or_next_game']['value']
    return get_output(title, input_string)

def get_output(title, input_string):
    rec = receiver(input_string)
    data = []
    data = rec.parse_string()
    res = response()
    speech_output = "Default Response - Error"
    if (len(data) == 28):
        speech_output = res.teamResponse(data)
    elif (len(data) == 33):
        speech_output = res.participantResponse(data)
    elif (len(data) == 3):
        speech_output = res.scheduleResponse(data)
    return build_response(build_speechlet_response(title, speech_output))
# --------------- Events ------------------

def on_intent(intent_request):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "TeamIntent":
        return recieve_team_request(intent)
    elif intent_name == "TeamParticipantIntent":
        return recieve_team_participant_request(intent)
    elif intent_name == "ScheduleIntent":
        return recieve_schedule_request(intent)
    else:
        return recieve_bad_request(intent)


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
