import nltk
import datetime
import time_parser
import assemble
import sentiment

now = datetime.datetime.now()

def process(note):
    marked = time_parser.mark(note)
    print(marked)
    dTime = time_parser.extract_parse_datetime(marked)
    context = time_parser.extract_context(marked)
    smart_note = assemble.assemble(context)
    emotion = sentiment.empathize(context)

    return {
            "context": context,
            "datetime": dTime,
            "sentiment": {
                "polarity": emotion.polarity,
                "confidence": emotion.subjectivity
            }
        }
