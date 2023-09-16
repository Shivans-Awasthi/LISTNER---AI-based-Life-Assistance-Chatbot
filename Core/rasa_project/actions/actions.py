# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Tracker, FormValidationAction
from typing import Any, Coroutine, Dict, List, Text
from rasa_sdk.interfaces import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from twilio.rest import Client



# account_sid = 'ACe20b110aabf7992b9ed57144e9342a63'
# auth_token = '01c06a9ecb6fb755f9b3fe2d001d16eb'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body="hi hello" ,
#   to='whatsapp:+919004504615'
# )

# print(message.sid)



class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_sms_details_form"


    def validate_mobile_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'mobile_number' value."""

        return{"mobile_number": slot_value}
    
    def validate_message(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'message' value."""

        return{"mobile_number": slot_value}


class ActionSubmit(Action):


    def name(self) -> Text:
        return "action_submit"
    

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict[Any,Any]) -> Coroutine[Any, Any, List[Dict[Any, Any]]]:



        account_sid = 'ACe20b110aabf7992b9ed57144e9342a63'
        auth_token = '01c06a9ecb6fb755f9b3fe2d001d16eb'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_ = '+12727882072',
            body = tracker.get_slot("message"),
            to = tracker.get_slot("mobile_number")
        )
        # account_sid = 'ACe20b110aabf7992b9ed57144e9342a63'
        # auth_token = '01c06a9ecb6fb755f9b3fe2d001d16eb'
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #             messaging_service_sid='MG9dffe795c8f70344098fe790cc6ff5af',
        #             body=tracker.get_slot("message"),
        #             to=tracker.get_slot("mobile_number")
        #     )
        # print(message.sid)

        dispatcher.utter_message(text="Message has been sent successfully to {}".format(tracker.get_slot("mobile_number")))

        return []

