import nltk
import datetime
import time_parser
import assemble
import sentiment

def process(note):
    marked = time_parser.mark(note)
    date_time = time_parser.extract_parse_datetime(marked)
    context = time_parser.extract_context(marked)
    smart_note = assemble.assemble(context)
    emotion = sentiment.empathize(context)

    return {
            "context": context,
            "datetime": date_time,
            "sentiment": {
                "polarity": emotion.polarity,
                "confidence": emotion.subjectivity
            }
        }
