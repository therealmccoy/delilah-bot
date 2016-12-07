########################################################################################################
########################################################################################################
# This is the first python file in the process of making the telegram bot @delilah_bot.
# The author of this file is Abhishek Rai.
# The git repository for @delilah_bot is :https://github.com/therealmccoy/delilah-bot .
# PART A of this script was completed by Abhishek Rai on 7th December, 2016.
########################################################################################################
########################################################################################################




########################################################################################################
# PART A ###############################################################################################
# in this part of the script, our script doesn't listen for new messages and replies immediately.
# when we run this script, our bot will fetch only the most recent message sent to that and echo it.
# we can test this by sending our bot a message, and then running the script.
########################################################################################################


# we import the json module now
# we will use the json module to parse the json responses from Telegram into Python dictionaries, to extract the pieces of data for our use.
import json

# we now import requests module
# this module is used to make web requests using Python and would be used to interact with Telegram API
import requests

# we now define our Bot's token which is used to authenticate with the Telegram API as a global variable
TOKEN="329997160:AAF-8_DZBt7ACGQsK9BQOMAb7vYCUUnIaRc"

# this is the basic URL that weill be using in all our requests to the API
URL="https://api.telegram.org/bot{}/".format(TOKEN)


# this function downloads the content from a URL and gives the string as input
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

# this function gets the string response as above and loads it into a Python dictionary using json.loads()
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

# this function calls the getUpdates API command and retrieves a list of updates
def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

# this function provides a simple way to get the chat id and message text of the most recent message sent to our Bot.
# this function returns a tuple of the chat_id, which identifies the specific chat between our Bot and the person who sent the message, and the message.
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


# this function takes the text of the message we want to send(text) and the chat id of the chat where we want to send the message(chat_id).
# it then calls the sendMessage API command, passing both the text and the chat ID as URL parameters, thus asking Telegram to send the message to that chat.
def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
# we get the text and the chat Id from the most recent message sent to our bot.    
text, chat = get_last_chat_id_and_text(get_updates())

# here we are calling send_message using the same text that we just recieved
send_message(text, chat)


########################################################################################################
# PART A ###############################################################################################
# END
########################################################################################################




