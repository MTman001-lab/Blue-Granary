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
import spacy

nlp = spacy.load("en_core_web_sm")

def perception_function(query):
    doc = nlp(query)
    extracted_keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    extracted_entities = [(ent.text, ent.label_) for ent in doc.ents]
    return extracted_keywords, extracted_entities

user_query = "My internet is not working, what should I do?"
keywords, entities = perception_function(user_query)
print("Keywords:", keywords)
print("Entities:", entities)





from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json.get('WELCOME MASTER!')
    rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "user", "message": user_message})
    return jsonify(rasa_response.json())

if __name__ == '__main__':
    app.run(port=8000)
