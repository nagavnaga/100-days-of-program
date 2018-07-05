'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re


SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join(r'C:\Program Files\JetBrains\my codes\100 days of coding', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# lines=(logline.strip() for logline in loglines if logline.strip())
def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''

    # matched = (re.split('-|:|T', line[4:25]))
    # matched = list(map(int,matched))
    matched=re.search(r'(\d){4}-(\d){2}-(\d){2}T(\d){2}:(\d){2}:(\d){2}',line).group()
    matched = re.split('-|:|T',matched)
    matched = list(map(int, matched))



    return datetime(*matched)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    shutdown=[]
    lines = (logline.strip() for logline in loglines if logline.strip())
    for line in lines:
        if re.findall(SHUTDOWN_EVENT, line):
            shutdown.append(convert_to_datetime(line))

    diff=shutdown[1]-shutdown[0]
    print(diff)

    return diff




time_between_shutdowns(loglines)


