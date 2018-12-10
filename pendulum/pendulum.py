import nlp
import sentiment
import assemble


def main(note):
    return note_to_smartnote(note)


def note_to_smartnote(note):
    # (content, datetime) = nlp.process(note)
    smart_note = nlp.process(note)


    # smart_note = note + ' THAT IS NOW SUPER SMART'
    print(smart_note)
    return smart_note


def testPendulumLoaded():
    return 'Pendulum Loaded'
