from __future__ import print_function

from request_receiver import receiver
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
            'content': output
        }
    }


def build_response(speechlet_response):
    return {
        'version': '1.0',
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_response(intent_name, intent_slots):
    rec = receiver(intent_name,  intent_slots)
    speech_output = rec.get_response()
    return build_response(build_speechlet_response(intent_name, speech_output))

# --------------- Events ------------------

def on_intent(intent_request):
    """ Called when the user specifies a valid intent for this skill """
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "AMAZON.FallbackIntent":
        return build_response(build_speechlet_response(intent_name, "Sorry, Case Baseball does not recognize that request. Please rephrase and ask again"))
    intent_slots = intent_request['intent']['slots']
    return get_response(intent_name, intent_slots)

def unknown_intent():
    """ Called when the intent is not valid for this skill """
    speech_output = "Sorry, but this Case Baseball Alexa skill does not support that type of request."
    return build_response(build_speechlet_response('Error', speech_output))


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" + event['session']['application']['applicationId'])

    """
    Our skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] != "amzn1.ask.skill.1790770a-d53f-4440-9d01-99f77c3ac33a"):
        raise ValueError("Invalid Application ID")
    elif (event['request']['type'] == "IntentRequest"):
        return on_intent(event['request'])
    elif (event['request']['type'] == "IntentRequest"):
        return unknown_intent()
    else:
        return unknown_intent()
