
import json
import pytz
import sys, os
import pytz
import traceback

from datetime import datetime, timedelta
from dateutil.parser import parse

db_filename ="board.json"
sessions = [
            {
                    "start_time":"2015-07-30 18:00:00",
                    'duration': 90, 
                    "speaker": "",
                    "title" : "Intros",
                    "location" : "Academy"
              },
              {
                    "start_time":"2015-07-30 19:30:00",
                    'duration': 30, 
                    "speaker": "",
                    "title" : "Preview",
                    "location" : "Academy"
              },
              {
                    "start_time":"2015-07-30 20:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "Open BBQ and networking",
                    "location" : "Academy"
              },
              {
                    "start_time":"2015-07-30 21:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "Gadgethon + songs + werewolf + music",
                    "location" : "Academy"
              },
              #Friday
              {
                    "start_time":"2015-07-31 08:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "Breakfast",
                    "location" : ""
              },
              {
                    "start_time":"2015-07-31 09:00:00",
                    'duration': 240, 
                    "speaker": "",
                    "title" : "Offsite and H-Farm activity",
                    "location" : ""
              },
              {
                    "start_time":"2015-07-31 13:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "lunch",
                    "location" : "Green House"
              },
              {
                    "start_time":"2015-07-31 14:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Solving the venetion mosquitto problem + other fun engineering- workshop",
                    "location" : "Serra"
              },
              {
                    "start_time":"2015-07-31 14:30:00",
                    'duration': 60, 
                    "speaker": "Liat Segal",
                    "title" : "ART & TECH SHOWCASE",
                    "location" : "Convivium"
              },
              {
                    "start_time":"2015-07-31 14:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section I",
                    "location" : "Sala Mais"
              },
              {
                    "start_time":"2015-07-31 14:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section I",
                    "location" : "H-Camp"
              },
              {
                    "start_time":"2015-07-31 14:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section I",
                    "location" : "Digital Accademia"
              },
              {
                    "start_time":"2015-07-31 14:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section I",
                    "location" : "Giardino"
              },

              {
                    "start_time":"2015-07-31 15:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section II",
                    "location" : "Serra"
              },
              {
                    "start_time":"2015-07-31 15:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section II",
                    "location" : "Convivium"
              },
              {
                    "start_time":"2015-07-31 15:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section II",
                    "location" : "Sala Mais"
              },
              {
                    "start_time":"2015-07-31 15:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section II",
                    "location" : "H-Camp"
              },
              {
                    "start_time":"2015-07-31 15:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section II",
                    "location" : "Digital Accademia"
              },
              {
                    "start_time":"2015-07-31 15:30:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section II",
                    "location" : "Giardino"
              },

              {
                    "start_time":"2015-07-31 17:00:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section III",
                    "location" : "Serra"
              },
              {
                    "start_time":"2015-07-31 17:00:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section III",
                    "location" : "Convivium"
              },
              {
                    "start_time":"2015-07-31 17:00:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section III",
                    "location" : "Sala Mais"
              },
              {
                    "start_time":"2015-07-31 17:00:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section III",
                    "location" : "H-Camp"
              },
              {
                    "start_time":"2015-07-31 17:00:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section III",
                    "location" : "Digital Accademia"
              },
              {
                    "start_time":"2015-07-31 17:00:00",
                    'duration': 60, 
                    "speaker": "TBD",
                    "title" : "Section III",
                    "location" : "Giardino"
              },
              {
                    "start_time":"2015-07-31 18:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "One hour big idea",
                    "location" : "Academy"
              },
              {
                    "start_time":"2015-07-31 19:00:00",
                    'duration': 90, 
                    "speaker": "",
                    "title" : "Gala dressup",
                    "location" : "shower fast"
              },
              {
                    "start_time":"2015-07-31 20:30:00",
                    'duration': 120, 
                    "speaker": "",
                    "title" : "Gala On board",
                    "location" : "Boat"
              },
              {
                    "start_time":"2015-07-31 23:00:00",
                    'duration': 120, 
                    "speaker": "",
                    "title" : "Bus",
                    "location" : "Bus ride back"
              },


               #Saturday
               {
                    "start_time":"2015-08-01 08:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "Breakfast",
                    "location" : "Academy"
              },
              {
                    "start_time":"2015-08-01 09:00:00",
                    'duration': 240, 
                    "speaker": "",
                    "title" : "Offsite and H-Farm activity",
                    "location" : ""
              },
              {
                    "start_time":"2015-08-01 13:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "lunch",
                    "location" : "Green House"
              },
              #Sunday
               {
                    "start_time":"2015-08-02 08:00:00",
                    'duration': 60, 
                    "speaker": "",
                    "title" : "Breakfast",
                    "location" : "Academy"
              },



            ]

for session in sessions:
    session['end_time'] = str(parse(session['start_time']) + timedelta(minutes=session['duration']))


def load_json_db():
    #load the jason file
    with open(db_filename) as json_file:
        json_data = json.load(json_file)
    print(json_data)
    return json_data


def handle_request(text): 
    '''
    What now?
    What next?
    '''
    try:
        if '/start' in text: 
            return '\n'.join(['Welcome to kinnernet bot!', 
                               'To use, write: ', 
                               'What now', 
                               'What next  (for next 30 minutes)',
                               'What today',
                               'What tomorrow',
                               'help', 
                               'Made with geeky kinky love by:',
                               '    Mattan Melamed',
                               '    Yosi Taguri',
                               '    Roy Ramon'
                               ])
        if  'help' in text.lower():
            return '\n'.join(['Welcome to kinnernet bot!', 
                               'To use, write: ', 
                               'What now', 
                               'What next  (for next 30 minutes)',
                               'What tomorrow',
                               'What today' ,
                               'help', 
                               'Made with geeky kinky love by:',
                               '     Mattan Melamed',
                               '     Yosi Taguri',
                               '     Roy Ramon'
                                ])           

        if text.lower().startswith('what'):
            if 'today' in text.lower(): 
                return get_today_events("today")
            if 'tomorrow' in text.lower(): 
                return get_today_events("tomorrow")
            _time = get_time_of_requested_start_time(text)
            # return "looking for time " + str(_time)
            return get_next_events_query(text, _time)

        else: 
            return 'Say what?!?!'

    except Exception as ex:
        return ex.message
#        return ex.message + '\n' + traceback.format_exc()

def get_today_events(text):
    if text == "today":
        events = [e for e in sessions  if parse(e["start_time"]).date() == datetime.today().date()] 
    if text == "tomorrow":
        events = [e for e in sessions  if parse(e["start_time"]).date() ==  datetime.today().date() + timedelta(days=1)] 
    if len(events) == 0: 
        return "no events for the request :("


    #make this a nice string: 
    return "\n\n".join([event_to_str(e) for e in events])


def get_next_events_query(text, _time):
    # load_json_db()
    events = [e for e in sessions  if parse(e["start_time"]) <= _time  and  parse(e["end_time"]) > _time  ]

    if len(events) == 0: 
        return "no events as this time"

    #make this a nice string: 
    return "\n\n".join([event_to_str(e) for e in events])
    

def get_time_of_requested_start_time(text):

    last_start_time = roundTime(datetime.now(), 1800)
    last_start_time = last_start_time + timedelta(minutes = 120)  #move to +1 timezone

    if 'now' in text.lower():
        return last_start_time
    if 'next' in text.lower():
        return last_start_time + timedelta(minutes = 30)

    raise Exception('not sure what time is needed. use: \n"what now"  or "what next")')
    

def event_to_str(event):
    start_time_str = parse(event['start_time']).strftime('%H:%M')
    speaker_str  =  (", by %s"  % event['speaker']) if event['speaker'] else ""

    return "'{0}'{1} at {2}.\n\t\t starts at {3}".format(event['title'], speaker_str, event['location'], start_time_str)

def set_time_query(text):
    load_json_db()
    # parse
    json.loads(filename)
    events = 'naked ballet dancing at the grass'

    return events


def announce_new_event(text):
    #add event to our db
    return "your event is registered"


def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.now()
   seconds = (dt - dt.min).seconds
   # // is a floor division, not a comment on following line:
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)