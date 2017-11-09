from flask_ask import statement, audio, question
from seebesee import ask
from seebesee.utils import stream_extractor

@ask.launch
def launch():
    text = 'Welcome to See Be See Radio (Unofficial).'
    prompt = 'For example say, play Radio One Edmonton'
    '''
    return question(text).reprompt(prompt) \
        .simple_card(title='Welcome to CBC Radio (Unofficial)',
                     content='Try asking me to play a station')
    '''
    return audio(text).play('https://cbcliveradio-lh.akamaihd.net/i/CBCR1_EDM@372985/master.m3u8')

@ask.intent("SeeBeSeePlayIntent")
def play_station(station, city):
    text = "Playing CBC Radio %s %s" % (station, city)
    return statement(text)
