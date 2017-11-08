from flask_ask import statement, audio, question
from seebesee import ask

@ask.launch
def launch():
    text = 'Welcome to See Be See Radio (Unofficial). \
            Try asking me to play Radio One or Radio Two.'
    prompt = 'For example say, play Radio One Edmonton'
    return question(text).reprompt(prompt) \
        .simple_card(title='Welcome to CBC Radio (Unofficial)',
                     content='Try asking me to play a station')

@ask.intent("SeeBeSeePlayIntent")
def play_station(station, city):
    text = "Playing CBC Radio %s %s" % (station, city)
    return statement(text)
