import nltk
import datetime
import time_parser

now = datetime.datetime.now()

def process(note):
    marked = time_parser.mark(note)
    print(marked)
    dTime = time_parser.extract_parse_datetime(marked)
    context = time_parser.extract_context(marked)
    print(dTime)
    print(context)
    return {"context": context, "dTime": dTime}
    # return marked
