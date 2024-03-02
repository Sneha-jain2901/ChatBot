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

# from .voice_integration import voice_input, voice_output
# from rasa_sdk import Action
# # In actions.py
# import voice_integration
# print(voice_integration)  # Print the module to check if it's loaded

# class VoiceInput(Action):
#     def name(self):
#         return "voice_input"

#     def run(self, dispatcher, tracker, domain):
#         text = voice_input()
#         if text:
#             dispatcher.utter_message(text=text)
#         return []
    
# class VoiceOutput(Action):
#     def name(self):
#         return "voice_output"

#     def run(self, dispatcher, tracker, domain):
#         text = tracker.latest_message['text']
#         voice_output(text)
#         return []

# In actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher
import os
import requests
from .voice_integration import VoiceIntegrationAction

class VoiceEnabledChatbotAction(VoiceIntegrationAction):
    def name(self):
        return "voice_enabled_chatbot"

    def run(self, dispatcher, tracker, domain):
        super().run(dispatcher, tracker, domain)
        return []

class VoiceInputWrapper(Action):
    def name(self):
        return "voice_input"

    def run(self, dispatcher, tracker, domain):
        voice_input = VoiceIntegrationAction().voice_input()
        if voice_input is not None:
            dispatcher.utter_message(text=voice_input)
        return []

class VoiceOutputWrapper(Action):
    def name(self):
        return "voice_output"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message.get('text', '')
        VoiceIntegrationAction().voice_output(text)
        return []

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_goodbye")
        return []

class ActionAffirm(Action):
    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_affirm")
        return []

class ActionDeny(Action):
    def name(self) -> Text:
        return "action_deny"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_deny")
        return []

class ActionHappy(Action):
    def name(self) -> Text:
        return "action_happy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_happy")
        return []

class ActionCheerUp(Action):
    def name(self) -> Text:
        return "action_cheer_up"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_cheer_up")
        return []

class ActionDidThatHelp(Action):
    def name(self) -> Text:
        return "action_did_that_help"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_did_that_help")
        return []

class ActionBookRecommendation(Action):
    def name(self) -> Text:
        return "action_book_recommendation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_book_recommendation")
        return []

class ActionBookDetails(Action):
    def name(self) -> Text:
        return "action_book_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_book_details")
        return []

class ActionFeedbackReceived(Action):
    def name(self) -> Text:
        return "action_feedback_received"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_feedback_received")
        return []

class ActionLatestBookReleases(Action):
    def name(self) -> Text:
        return "action_latest_book_releases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_latest_book_releases")
        return []

class ActionPopularAuthors(Action):
    def name(self) -> Text:
        return "action_popular_authors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_popular_authors")
        return []

class ActionSearchBook(Action):
    def name(self) -> Text:
        return "action_Search_book"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_search_book")
        return []

class ActionWeatherInfo(Action):
    def name(self) -> Text:
        return "action_weather_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_weather_info")
        return []

class ActionBuilderInfo(Action):
    def name(self) -> Text:
        return "action_builder_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_builder_info")
        return []

class ActionRestaurantInfo(Action):
    def name(self) -> Text:
        return "action_restaurant_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_restaurant_info")
        return []

class ActionInsultResponse(Action):
    def name(self) -> Text:
        return "action_insult_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_insult_response")
        return []

class ActionJoke(Action):
    def name(self) -> Text:
        return "action_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_joke")
        return []

class ActionWhereFrom(Action):
    def name(self) -> Text:
        return "action_wherefrom"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_wherefrom")
        return []

class ActionHowOld(Action):
    def name(self) -> Text:
        return "action_howold"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_howold")
        return []

class ActionWhoAmI(Action):
    def name(self) -> Text:
        return "action_whoami"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_whoami")
        return []

class ActionLanguages(Action):
    def name(self) -> Text:
        return "action_languages"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_languages")
        return []

class ActionWhatIsMyName(Action):
    def name(self) -> Text:
        return "action_whatismyname"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_whatismyname")
        return []

class ActionSongRecommendation(Action):

    def name(self) -> Text:
        return "action_song_recommendation"

class ActionGiveDetails(Action):
    def name(self) -> Text:
        return "action_give_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Fetch the value of the book or author slot from the tracker
        book = tracker.get_slot("book")
        author = tracker.get_slot("author")
        
        if book:
            # Provide details about the book
            #details = fetch_book_details(book)
            details = "The book details"
            dispatcher.utter_message(text=details)
        elif author:
            # Provide details about the author
            details = "The author details"
            #details = fetch_author_details(author)
            dispatcher.utter_message(text=details)
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't find any details.")

        return []

class ActionLatestBookReleases(Action):
    def name(self) -> Text:
        return "action_latest_book_releases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Fetch latest book releases from your data source
        book_releases = ["Book 1", "Book 2", "Book 3"]  # Example data
        dispatcher.utter_message(template="utter_latest_book_releases", book_releases=book_releases)
        return []

class ActionPopularAuthors(Action):
    def name(self) -> Text:
        return "action_popular_authors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make a request to the Google Books API to retrieve popular authors
        api_key = "YOUR_GOOGLE_BOOKS_API_KEY"
        url = f"https://www.googleapis.com/books/v1/volumes?q=subject:fiction&key={'AIzaSyD-uUQ45ahzJXQVjOoHBWsCEclpbUIsh7U'}&maxResults=5"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            # Extract authors from the response
            popular_authors = []
            for item in data.get("items", []):
                volume_info = item.get("volumeInfo", {})
                authors = volume_info.get("authors", [])
                popular_authors.extend(authors)
                
                # Break the loop if we have collected 5 authors
                if len(popular_authors) >= 5:
                    break
            
            # Send the list of popular authors as a response
            if popular_authors:
                dispatcher.utter_message(template="utter_popular_authors", popular_authors=popular_authors)
            else:
                dispatcher.utter_message(text="Sorry, unable to retrieve popular authors at the moment.")
                
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred while retrieving popular authors: {e}")
            
        return []
    
class ActionSearchBook(Action):
    def name(self) -> Text:
        return "action_search_book"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Implement your logic to search for books here
        dispatcher.utter_message(template="utter_Search_book")
        return []

class ActionSearchBooksByGenre(Action):
    def name(self) -> Text:
        return "action_search_books_by_genre"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Extract user preferences from the tracker
            genre = tracker.get_slot("genre")
            
            # Make a request to the Google Books API to search for books based on the user's genre preference
            url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&maxResults=5&key=YOUR_GOOGLE_BOOKS_API_KEY"
            response = requests.get(url)
            
            if response.status_code == 200:
                # Parse the response and extract book recommendations
                data = response.json()
                recommended_books = [item["volumeInfo"]["title"] for item in data.get("items", [])]
                
                # Format the recommendations into a single message
                recommendation_message = f"Here are some book recommendations in the genre of {genre}:\n\n"
                for book in recommended_books:
                    recommendation_message += f"- {book}\n"
                
                # Send the recommendations back to the user
                dispatcher.utter_message(text=recommendation_message)
            else:
                dispatcher.utter_message(text="Sorry, I couldn't fetch book recommendations at the moment.")
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {e}")
        
        return []


class ActionSearchGeneralBooks(Action):
    def name(self) -> Text:
        return "action_search_general_books"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # Extract user preferences from the tracker
            books = tracker.get_slot("books")
            
            # Make a request to your API or database to search for books based on the user's query
            recommended_books = search_books(books)
            
            if recommended_books:
                # Format the recommendations into a single message
                recommendation_message = f"Here are some book recommendations based on your query:\n\n"
                for book in recommended_books:
                    recommendation_message += f"- {book}\n"
                
                # Send the recommendations back to the user
                dispatcher.utter_message(text=recommendation_message)
            else:
                dispatcher.utter_message(text="Sorry, I couldn't find any books based on your query.")
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {e}")
        
        return []

# Placeholder functions for demonstration purposes
def get_books_by_genre(genre: str) -> List[str]:
    # Dummy function to simulate retrieving books by genre
    # Replace this with your actual logic to fetch books by genre from a database or API
    return ["Book 1", "Book 2", "Book 3"]

def get_general_books() -> List[str]:
    # Dummy function to simulate retrieving general book recommendations
    # Replace this with your actual logic to fetch general book recommendations from a database or API
    return ["General Book 1", "General Book 2", "General Book 3"]

# Placeholder function for demonstration purposes
def search_books(books: str) -> List[str]:
    # Dummy function to simulate searching for books based on the user's query
    # Replace this with your actual logic to search for books from a database or API
    return ["Book 1", "Book 2", "Book 3"]

