from datetime import datetime
from time import sleep
from os import system

hugeChars = {
    "PM": [
            ' █▀▀█  █▀▄▀█ ',
            ' █▄▄█  █ █ █ ',
            ' █     █   █ ',
            ],
    
    "AM": [
            ' █▀▀█  █▀▄▀█ ',
            ' █▄▄█  █ █ █ ',
            ' █  █  █   █ ',
            ],
    
    "0": [
            '█▀▀█ ',
            '█▄▀█ ',
            '█▄▄█ ',
            ],

    "1": [
            ' ▄█  ',
            '  █  ',
            ' ▄█▄ ',
            ],  

    "2": [
            ' █▀█ ',
            '  ▄▀ ',
            ' █▄▄ ',
            ],

    "3": [
            '█▀▀█ ',
            '  ▀▄ ',
            '█▄▄█ ',
            ],
    
    "4": [
            ' █▀█ ',
            '█▄▄█▄',
            '   █ ',
            ],

    "5": [
            ' █▀▀ ',
            ' ▀▀▄ ',
            ' ▄▄▀ ',
            ],
    
    "6": [
            '▄▀▀▄ ',
            '█▄▄  ',
            '▀▄▄▀ ',
            ],
    
    "7": [
            '▀▀▀█ ',
            '  █  ',
            ' ▐▌  ',
            ],
    
    "8": [
            '▄▀▀▄ ',
            '▄▀▀▄ ',
            '▀▄▄▀ ',
            ],
    
    "9": [
            '▄▀▀▄ ',
            '▀▄▄█ ',
            ' ▄▄▀ ',
            ],
    
    ":": [
            ' ▄  ',
            '    ',
            ' ▀  ',
            ],
    
    "/": [
            '   █ ', 
            '  █  ',
            ' █   ',  
            ],
    
    " ": [
            '    ',
            '    ',
            '    ',
            ],
    ".": [
            '    ',
            '    ',
            ' ▄  ',
            ],
    "|": [
            '  █  ',
            '  █  ',
            '  █  ',
            ]
}

def printHugeString(string):
    finalString = ''
    for layer in range(3):
        for char in string:
            finalString += hugeChars[char][layer]
        finalString += "\n"
    print("\n" + finalString)
    
def getTime():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    millisecond = int(now.microsecond / 1000)
    
    month = now.month
    day = now.day
    year = now.year
    
    timeMeasures = {
        'hour': hour,
        'minute': minute,
        'second': second,
        'millisecond': millisecond,
    }
    dateMeasures = {
        'month': month, 
        'day': day, 
        'year': year
    }
    return {
        'time': timeMeasures,
        'date': dateMeasures
    }
def printTime():
    date_and_time = getTime()
    PMorAM = ''
    if date_and_time['time']['hour'] > 12:
        date_and_time['time']['hour'] -= 12
        PMorAM = 'PM'
    else:
        PMorAM = 'AM'
        
    
    for i in date_and_time['time']:
        if date_and_time['time'][i] < 10:
            date_and_time['time'][i] = '0' + str(date_and_time['time'][i])
        else:
            date_and_time['time'][i] = str(date_and_time['time'][i])
    
    for i in date_and_time['date']:
        if date_and_time['date'][i] < 10:
            date_and_time['date'][i] = '0' + str(date_and_time['date'][i])
        else:
            date_and_time['date'][i] = str(date_and_time['date'][i])
    
    if len(date_and_time['time']['millisecond']) < 3:
        date_and_time['time']['millisecond'] = '0'*(3 - len(date_and_time['time']['millisecond'])) + date_and_time['time']['millisecond']
        
    if len(date_and_time['time']['hour']) < 2:
        date_and_time['time']['hour'] = '0'*(2 - len(date_and_time['time']['hour'])) + date_and_time['time']['hour']
    
    if len(date_and_time['time']['minute']) < 2:
        date_and_time['time']['minute'] = '0'*(2 - len(date_and_time['time']['minute'])) + date_and_time['time']['minute']
    
    if len(date_and_time['time']['second']) < 2:
        date_and_time['time']['second'] = '0'*(2 - len(date_and_time['time']['second'])) + date_and_time['time']['second']
        
        
    if len(date_and_time['date']['month']) < 2:
        date_and_time['date']['month'] = '0'*(2 - len(date_and_time['date']['month'])) + date_and_time['date']['month']
    
    if len(date_and_time['date']['day']) < 2:
        date_and_time['date']['day'] = '0'*(2 - len(date_and_time['date']['day'])) + date_and_time['date']['day']
    
    if len(date_and_time['date']['year']) < 4:
        date_and_time['date']['year'] = '0'*(4 - len(date_and_time['date']['year'])) + date_and_time['date']['year']
    
            
    toPrint = [str(date_and_time['time']['hour'])[0], str(date_and_time['time']['hour'])[1],
               ":",
               str(date_and_time['time']['minute'])[0], str(date_and_time['time']['minute'])[1],
               ":",
               str(date_and_time['time']['second'])[0], str(date_and_time['time']['second'])[1],
               ".",
               str(date_and_time['time']['millisecond'])[0], str(date_and_time['time']['millisecond'])[1],
               str(date_and_time['time']['millisecond'])[2],
               " ", 
               PMorAM,
               " ", " ", " ",
               str(date_and_time['date']['month'])[0], str(date_and_time['date']['month'])[1],
               "/",
               str(date_and_time['date']['day'])[0], str(date_and_time['date']['day'])[1],
               "/",
               str(date_and_time['date']['year'])[0], str(date_and_time['date']['year'])[1],
               str(date_and_time['date']['year'])[2], str(date_and_time['date']['year'])[3],
               ]
    printHugeString(toPrint)
    
def startClockLoop():    
    while True:
        system('cls')
        printTime()
        sleep(0.03875)
        



startClockLoop()