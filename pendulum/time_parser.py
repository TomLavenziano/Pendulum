import os
import sys
import string
import datetime
import parsedatetime
import re

# Predefined strings.
month = "(january|february|march|april|may|june|july|august|september| \
          october|november|december)"
day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
week_day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
          eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
          eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
          ninety|hundred|thousand)"
dmy = "(year|day|week|month)"
relative_day = "(today|yesterday|tomorrow|tonight|tonite)"
expression1 = "(before|after|earlier|later|ago)"
expression2 = "(this|next|last)"
iso = "\d+[/-]\d+[/-]\d+ \d+:\d+:\d+\.\d+"
year = "((?<=\s)\d{4}|^\d{4})"
regex1 = "((\d+|(" + numbers + "[-\s]?)+) " + dmy + "s? " + expression1 + ")"
regex2 = "(" + expression2 + " (" + dmy + "|" + week_day + "|" + month + "))"

reg1 = re.compile(regex1, re.IGNORECASE)
reg2 = re.compile(regex2, re.IGNORECASE)
reg3 = re.compile(relative_day, re.IGNORECASE)
reg4 = re.compile(iso)
reg5 = re.compile(year)

def mark(text):
    chrono_found = []

    # Captures 'number of days' ago, etc.
    found = reg1.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for chrono in found:
        chrono_found.append(chrono)

    # Variations of this tuesday, next week, next month, etc
    found = reg2.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for chrono in found:
        chrono_found.append(chrono)

    # today, tomorrow, etc
    found = reg3.findall(text)
    for chrono in found:
        chrono_found.append(chrono)

    # ISO
    found = reg4.findall(text)
    for chrono in found:
        chrono_found.append(chrono)

    # Year
    found = reg5.findall(text)
    for chrono in found:
        chrono_found.append(chrono)

    # Tag only datetime expressions that haven't been tagged yet.
    for chrono in chrono_found:
        text = re.sub(chrono + '(?!}}}})', '{{{{' + chrono + '}}}}', text)

    return text


def extract_parse_datetime(markedText):
    cal = parsedatetime.Calendar();
    dTime = re.search(r'\{{{{(.*)\}}}}', markedText)

    print(dTime)

    time_struct, parse_status = cal.parse(dTime.group(1))
    parsed = datetime.datetime(*time_struct[:6])

    return parsed

def extract_context(markedText):
    # cal = parsedatetime.Calendar();
    # context = re.search(r'\{(.*)\}.*', markedText)
    tempContext = re.sub('({{{{(.*)}}}})', '', markedText)
    context = re.sub('(by|on)', '', tempContext).strip()
    print(context)

    # time_struct, parse_status = cal.parse(dTime.group(1))
    # parsed = datetime.datetime(*time_struct[:6])

    return context


def demo():
    import nltk
    text = nltk.corpus.abc.raw('rural.txt')[:10000]
    text = "Bring my car in for an oil change by next monday"
    marked = mark(text)
    extracted = extract_parse_datetime(marked)
    print(marked)
    print('\n')
    print(extracted)

if __name__ == '__main__':
    demo()
